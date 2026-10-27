"""Pre-processadores e familias de modelos. Ajustar usando dados de treino."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor

def transformer(X):
    cats=[c for c in X.columns if pd.api.types.is_object_dtype(X[c]) or pd.api.types.is_string_dtype(X[c])]; nums=[c for c in X if c not in cats]
    return ColumnTransformer([('num',SimpleImputer(strategy='median'),nums),('cat',Pipeline([('imp',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore',sparse_output=False))]),cats)],sparse_threshold=0)

def model_specs(is_classification, search_mode='standard'):
    tree = DecisionTreeClassifier if is_classification else DecisionTreeRegressor
    forest = RandomForestClassifier if is_classification else RandomForestRegressor
    boost = GradientBoostingClassifier if is_classification else GradientBoostingRegressor
    if search_mode == 'quick':
        rf_grid={'model__n_estimators':[40], 'model__max_depth':[10], 'model__min_samples_leaf':[2]}
        gb_grid={'model__n_estimators':[60], 'model__learning_rate':[.07], 'model__max_depth':[2]}
    else:
        rf_grid={'model__n_estimators':[40,100], 'model__max_depth':[10,16], 'model__min_samples_leaf':[2]}
        gb_grid={'model__n_estimators':[60,100], 'model__learning_rate':[.05,.1], 'model__max_depth':[2]}
    return {
        'Arvore_sem_limite': (tree(random_state=42), None),
        'Arvore_ajustada': (tree(random_state=42), {'model__max_depth':[6,12], 'model__min_samples_leaf':[10,20], 'model__criterion':['gini','entropy'] if is_classification else ['squared_error','absolute_error']}),
        'Random_Forest': (forest(random_state=42,n_jobs=2), rf_grid),
        'Gradient_Boosting': (boost(random_state=42), gb_grid),
    }
