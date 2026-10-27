"""Rotinas compartilhadas para o treinamento realizado nos notebooks 04 e 05."""
from pathlib import Path
import json, pickle, time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from src.models import model_specs, transformer
from src.metrics import eval_metric

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'processed'
TABLES = ROOT / 'reports' / 'tables'
MODELS = ROOT / 'models'


def prepare(task):
    metadata = json.loads((DATA / 'metadata.json').read_text(encoding='utf-8'))
    target = metadata[task]['target']
    df = pd.read_csv(DATA / f'dataset_{task}.csv')
    X = df.drop(columns=[target])
    y = (df[target] == 'Placed').astype(int) if task == 'classification' else df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42,
                            stratify=y if task == 'classification' else None)


def train_group(task, names, search_mode='standard'):
    X_train, X_test, y_train, y_test = prepare(task)
    classification = task == 'classification'
    specs = model_specs(classification, search_mode)
    cv = StratifiedKFold(5, shuffle=True, random_state=42) if classification else KFold(5, shuffle=True, random_state=42)
    scoring = 'f1' if classification else 'neg_root_mean_squared_error'
    metrics, folds, times, parameters = [], [], [], {}
    MODELS.mkdir(exist_ok=True);TABLES.mkdir(parents=True, exist_ok=True)
    for name in names:
        estimator, grid = specs[name]
        pipeline = Pipeline([('prep', transformer(X_train)), ('model', estimator)])
        started = time.perf_counter()
        if grid is not None:
            search = GridSearchCV(pipeline, grid, cv=cv, scoring=scoring, refit=True, n_jobs=1)
            search.fit(X_train, y_train)
            fitted = search.best_estimator_
            parameters[name] = search.best_params_
        else:
            fitted = pipeline.fit(X_train, y_train)
            parameters[name] = {}
        seconds = time.perf_counter() - started
        with (MODELS / f'{task}_{name}.pkl').open('wb') as f:pickle.dump(fitted, f)
        for split, X, y in [('train', X_train, y_train), ('test', X_test, y_test)]:
            predictions = fitted.predict(X)
            scores = fitted.predict_proba(X)[:,1] if classification else None
            metrics.append({'task':task,'model':name,'split':split,
                            **eval_metric(y,predictions,task,scores)})
        scores_cv = cross_val_score(fitted, X_train, y_train, cv=cv, scoring=scoring, n_jobs=1)
        folds.append({'task':task, 'model':name, 'cv_mean':float(np.mean(scores_cv)),
                      'cv_std':float(np.std(scores_cv)), 'scoring':scoring})
        times.append({'task':task,'model':name,'train_seconds':seconds})
        print(f'{task}: {name} | ajuste {seconds:.2f} s')
    # These outputs refer to the current run; previous aggregate results are kept in reports/tables.
    prefix = 'arvores' if all(n.startswith('Arvore') for n in names) else 'ensembles'
    pd.DataFrame(metrics).to_csv(TABLES/f'{task}_{prefix}_metricas_execucao.csv',index=False)
    pd.DataFrame(folds).to_csv(TABLES/f'{task}_{prefix}_validacao_execucao.csv',index=False)
    pd.DataFrame(times).to_csv(TABLES/f'{task}_{prefix}_tempos_execucao.csv',index=False)
    (TABLES/f'{task}_{prefix}_parametros_execucao.json').write_text(json.dumps(parameters,indent=2),encoding='utf-8')
    return pd.DataFrame(metrics)
