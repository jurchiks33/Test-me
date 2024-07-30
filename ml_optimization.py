# ml_optimization.py
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

def optimize_strategy(df):
    x = df[['feature1', 'feature2', 'feature3']]  # Here will be features for ML
    y = df[['signal']] #target variable

    model = RandomForestClassifier()
    param_grid = {
        'n_estimator': [100, 200],
        'max_depth': [5, 10]
    }
    