# Metodologia experimental

O estudo compara sistemas especialistas, árvores de decisão, Random Forest e Gradient Boosting em regressão e classificação, com o dataset Student Career Success Prediction (50.000 registros).

A divisão dos dados é de 80% para treinamento e 20% para teste, com semente aleatória 42 e estratificação na classificação. O pré-processamento está encapsulado em pipelines ajustados somente com o conjunto de treinamento. A seleção de hiperparâmetros utiliza validação cruzada de cinco folds.

O Sistema Especialista utiliza bases estáticas de regras SE–ENTÃO nos arquivos da pasta rules, interpretadas pelo motor de inferência de src/expert_system.py. A primeira regra satisfeita determina a consequência. Na classificação, a pontuação de empregabilidade é considerada atributo preditor, com a ressalva de que sua disponibilidade anterior à colocação não foi estabelecida pelos metadados.

Os registros das sessões de elaboração das regras estão em logs/cronometro_regras.csv. A coluna de interrupções distingue os dados não registrados de ocorrências efetivamente observadas. O esforço humano de elaboração não se soma ao tempo de inferência computacional.

As métricas e visualizações constam dos notebooks 03 a 08 e das pastas reports/tables e reports/figures. A comparação utiliza MAE, MSE, RMSE, MAPE, R² e MedAE em regressão; Accuracy, Precision, Recall, F1, ROC-AUC e PR-AUC em classificação.
