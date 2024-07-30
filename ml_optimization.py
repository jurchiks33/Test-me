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
    
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(x, y)
    return grid_search.best_params_

if __name__ == "__main":
    df = pd.read_csv('AAPL_data_with_signals.csv')
    best_params = optimize_strategy(df)
    print(best_params)