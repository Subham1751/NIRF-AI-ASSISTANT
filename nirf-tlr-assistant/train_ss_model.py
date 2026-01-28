import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_validate
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

def train_ss_model(input_path: str, model_output_path: str):
    # STEP 1: Load data
    print("\nSTEP 1: Loading data...")
    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} records")
    
    feature_cols = [
        "NT_total",
        "NE_total",
        "NP_total",
    ]
    
    # STEP 2: Check for missing values
    print("\nSTEP 2: Checking for missing values...")
    X = df[feature_cols]
    y = df["SS_Score"]
    
    print(f"Missing values per feature:")
    missing_counts = X.isnull().sum()
    for col, count in missing_counts.items():
        if count > 0:
            print(f"{col}: {count} missing")
    
    print(f"\nMissing values in target (SS_Score): {y.isnull().sum()}")
    
    # STEP 3: Handle missing values
    print("\nSTEP 3: Handling missing values...")
    # Drop rows where target is missing
    valid_idx = y.notna()
    X = X[valid_idx]
    y = y[valid_idx]
    
    # Drop rows with missing NT, NE, NP
    missing_before = len(X)
    df_clean = pd.concat([X, y], axis=1).dropna()
    X = df_clean[feature_cols]
    y = df_clean["SS_Score"]

    print(f"Dropped {missing_before - len(X)} rows due to missing core values.")
    
    print(f"Data cleaned. Shape: {X.shape}")
    print(f"Remaining NaN values: {X.isnull().sum().sum()}")
    
    print(f"Data cleaned. Shape: {X.shape}")
    print(f"Remaining NaN values: {X.isnull().sum().sum()}")
    
    # # STEP 4: Split data
    # print("\nSTEP 4: Splitting data...")
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=0.25, random_state=42
    # )
    # print(f"Training set: {len(X_train)} samples")
    # print(f"Test set: {len(X_test)} samples")






    # Cross-validation setup

    
    cv = KFold(n_splits=5, shuffle=True, random_state=42)

    gbr_pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("gbr", GradientBoostingRegressor(random_state=42))
    ])

    gbr_param_grid = {
        "gbr__n_estimators": [200, 400, 600],
        "gbr__learning_rate": [0.03, 0.05, 0.1],
        "gbr__max_depth": [2, 3],
        "gbr__min_samples_leaf": [1, 2, 4],
        "gbr__loss": ["absolute_error", "huber"]
    }

    gbr_grid = GridSearchCV(
        estimator=gbr_pipeline,
        param_grid=gbr_param_grid,
        cv=cv,
        scoring="neg_mean_absolute_error",
        n_jobs=-1
    )
    gbr_grid.fit(X, y)

    best_gbr = gbr_grid.best_estimator_

    cv_results = cross_validate(
    best_gbr,
    X,
    y,
    cv=cv,
    scoring={
        "mae": "neg_mean_absolute_error",
        "r2": "r2"
    }
    )    
    print("SS Best Parameters:", gbr_grid.best_params_)
    print(f"MAE: {-cv_results['test_mae'].mean():.3f} "
      f"(± {cv_results['test_mae'].std():.3f})")
    print(f"R²: {cv_results['test_r2'].mean():.3f} "
      f"(± {cv_results['test_r2'].std():.3f})")




    # # Creating GBR pipeline for Grid Search

    # gbr_pipeline = Pipeline([
    #     ("gbr_model", GradientBoostingRegressor())
    # ])

    # gbr_param_grid = {
    #     "gbr_model__n_estimators": [100, 200, 300],
    #     "gbr_model__learning_rate": [0.01, 0.05, 0.1],
    #     "gbr_model__max_depth": [3, 5, 7],
    #     "gbr_model__min_samples_split": [2, 5],
    #     "gbr_model__min_samples_leaf": [1, 2],
    #     "gbr_model__loss": ["squared_error", "absolute_error", "huber"]

    # }


    # gbr_grid_search = GridSearchCV(
    #     estimator= gbr_pipeline,
    #     param_grid= gbr_param_grid,
    #     cv = KFold(n_splits =3 , shuffle = True, random_state = 42),
    #     scoring='neg_mean_absolute_error',
    #     n_jobs= -1
    # )

    # gbr_grid_search.fit(X_train, y_train)
    # print("Best parameters found: ", gbr_grid_search.best_params_)
    # print("Best cross-validation score: ", gbr_grid_search.best_score_)

    # best_model = gbr_grid_search.best_estimator_
    # y_pred = best_model.predict(X_test)
    # mae = mean_absolute_error(y_test, y_pred)
    # r2 = r2_score(y_test, y_pred)

    # print(f"MAE: {mae:.3f}")
    # print(f"R2 Score: {r2:.3f}")



    # # STEP 5: Train model
    # print("\nSTEP 5: Training model...")
    # model = GradientBoostingRegressor(
    #     n_estimators=300,
    #     learning_rate=0.05,
    #     max_depth=3
    # )
    
    # model.fit(X_train, y_train)
    # print("Model trained successfully!")
    
    # # STEP 6: Evaluate
    # print("\nSTEP 6: Evaluating model...")
    # y_pred = model.predict(X_test)
    
    # mae = mean_absolute_error(y_test, y_pred)
    # r2 = r2_score(y_test, y_pred)
    
    # print("\n--- SS Model Performance ---")
    # print(f"MAE: {mae: .3f}")
    # print(f"R2 Score: {r2: .3f}")
    
    joblib.dump(best_gbr, model_output_path)
    print(f"Model saved to {model_output_path}")
    
    

if __name__ == "__main__":
    train_ss_model(
        input_path="data/Engineering/ss_feature_engineered.csv",
        model_output_path="model/ss_model.pkl"
    )


