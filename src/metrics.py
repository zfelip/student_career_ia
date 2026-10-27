"""Metricas de regressao e classificacao."""
import numpy as np
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score, median_absolute_error, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, average_precision_score)

def eval_metric(y,p,task,score=None):
    if task=='regression':
        return dict(MAE=mean_absolute_error(y,p),MSE=mean_squared_error(y,p),RMSE=np.sqrt(mean_squared_error(y,p)),MAPE=float(np.mean(np.abs((np.array(y)-p)/np.where(np.array(y)==0,np.nan,np.array(y))))*100),R2=r2_score(y,p),MedAE=median_absolute_error(y,p))
    d=dict(Accuracy=accuracy_score(y,p),Precision=precision_score(y,p,zero_division=0),Recall=recall_score(y,p,zero_division=0),F1=f1_score(y,p,zero_division=0))
    if score is not None: d.update(ROC_AUC=roc_auc_score(y,score),PR_AUC=average_precision_score(y,score))
    return d
