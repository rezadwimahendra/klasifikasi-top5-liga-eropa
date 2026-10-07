import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_football_data(filepath='data top 5 liga.csv', test_size=0.2, random_state=42):
    """
    Memuat dan membersihkan dataset pertandingan sepak bola Top 5 Liga Eropa Musim 2025/2026.
    Memisahkan fitur statistik pertandingan dan target FTR (Full Time Result).
    """
    # Read CSV with semicolon delimiter
    df = pd.read_csv(filepath, sep=';')
    
    # Filter header duplicates
    df = df[df['Date'] != 'Date'].copy()
    df = df.dropna(subset=['FTR'])

    # Select numerical match statistics features
    feature_cols = ['HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
    
    for col in feature_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df = df.dropna(subset=feature_cols)

    X = df[feature_cols].copy()
    y = df['FTR'].copy()

    # Encode target labels (H=0, D=1, A=2)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=test_size, random_state=random_state, stratify=y_encoded
    )

    # Standard Scaling
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=feature_cols)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=feature_cols)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, feature_cols, le, df
