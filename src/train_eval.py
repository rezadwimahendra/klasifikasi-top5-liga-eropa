import os
import pandas as pd
import numpy as np
import optuna
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
try:
    from src.preprocess import load_and_preprocess_football_data
except ModuleNotFoundError:
    from preprocess import load_and_preprocess_football_data

# Suppress Optuna logging messages during optimization
optuna.logging.set_verbosity(optuna.logging.WARNING)

def evaluate_multi_class(model, X_test, y_test, model_name, le):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test) if hasattr(model, "predict_proba") else None
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    auc = roc_auc_score(y_test, y_proba, multi_class='ovr') if y_proba is not None else np.nan

    return {
        'Model / Metode': model_name,
        'Accuracy': round(acc, 4),
        'Precision (Weighted)': round(prec, 4),
        'Recall (Weighted)': round(rec, 4),
        'F1-Score (Weighted)': round(f1, 4),
        'ROC-AUC (OVR)': round(auc, 4)
    }

def run_experiments():
    print("==========================================================================")
    print(" KLASIFIKASI HASIL PERTANDINGAN TOP 5 LIGA EROPA MUSIM 2025/2026 ")
    print("      MENGGUNAKAN RANDOM FOREST & OPTIMASI HYPERPARAMETER BAYESIAN       ")
    print("==========================================================================")
    
    X_train, X_test, y_train, y_test, scaler, feature_names, le, raw_df = load_and_preprocess_football_data()
    print(f"\n[INFO] Jumlah Data Latih: {X_train.shape[0]} | Jumlah Data Uji: {X_test.shape[0]}")
    print(f"[INFO] Fitur Statistik ({len(feature_names)}): {list(feature_names)}")
    print(f"[INFO] Kelas Target FTR: {list(le.classes_)} (0: Home Win, 1: Draw, 2: Away Win)\n")

    results = []

    # 1. Baseline Random Forest
    print("--- 1. Melatih Baseline Random Forest ---")
    rf_base = RandomForestClassifier(random_state=42)
    rf_base.fit(X_train, y_train)
    res_rf_base = evaluate_multi_class(rf_base, X_test, y_test, 'Random Forest (Baseline)', le)
    results.append(res_rf_base)

    # 2. Grid Search Optimization for Random Forest
    print("--- 2. Optimasi Hyperparameter Random Forest (Grid Search CV) ---")
    param_grid_rf = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 8, None],
        'min_samples_split': [2, 5, 10],
        'criterion': ['gini', 'entropy']
    }
    grid_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)
    grid_rf.fit(X_train, y_train)
    rf_grid = grid_rf.best_estimator_
    print(f"    Best Params (Grid Search): {grid_rf.best_params_}")
    res_rf_grid = evaluate_multi_class(rf_grid, X_test, y_test, 'Random Forest (GridSearch)', le)
    results.append(res_rf_grid)

    # 3. Bayesian Optimization for Random Forest using Optuna
    print("--- 3. Optimasi Hyperparameter Random Forest (Bayesian Optimization via Optuna) ---")
    def objective(trial):
        n_estimators = trial.suggest_int('n_estimators', 20, 300)
        max_depth = trial.suggest_int('max_depth', 2, 20)
        min_samples_split = trial.suggest_int('min_samples_split', 2, 15)
        min_samples_leaf = trial.suggest_int('min_samples_leaf', 1, 10)
        criterion = trial.suggest_categorical('criterion', ['gini', 'entropy'])
        max_features = trial.suggest_categorical('max_features', ['sqrt', 'log2', None])

        clf = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            criterion=criterion,
            max_features=max_features,
            random_state=42
        )
        score = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1).mean()
        return score

    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=50)

    best_params_bayes = study.best_params
    print(f"    Best Params (Bayesian Optimization): {best_params_bayes}")

    rf_bayes = RandomForestClassifier(**best_params_bayes, random_state=42)
    rf_bayes.fit(X_train, y_train)
    res_rf_bayes = evaluate_multi_class(rf_bayes, X_test, y_test, 'Random Forest (Bayesian Opt)', le)
    results.append(res_rf_bayes)

    # 4. XGBoost (Pembanding Model Ensemble Lain)
    print("--- 4. Melatih XGBoost Classifier (Pembanding) ---")
    xgb = XGBClassifier(random_state=42, eval_metric='mlogloss')
    xgb.fit(X_train, y_train)
    res_xgb = evaluate_multi_class(xgb, X_test, y_test, 'XGBoost (Baseline)', le)
    results.append(res_xgb)

    # Summary Results Table
    df_results = pd.DataFrame(results)
    print("\n==========================================================================")
    print("          TABEL HASIL EVALUASI MODEL KLASIFIKASI MATCH OUTCOME            ")
    print("==========================================================================")
    print(df_results.to_string(index=False))

    # Feature Importance Analysis (Random Forest Bayesian)
    print("\n=== ANALISIS FEATURE IMPORTANCE (Random Forest + Bayesian Opt) ===")
    importances = rf_bayes.feature_importances_
    df_imp = pd.DataFrame({'Fitur Statistik': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
    print(df_imp.to_string(index=False))

    return df_results, df_imp

if __name__ == '__main__':
    run_experiments()
