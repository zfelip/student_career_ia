# Avaliação comparativa de modelos de inteligência artificial

Disciplina: DCT1401 - Inteligência Artificial, UFRN, período 2026.2.

Dataset: Student Career Success Prediction - https://www.kaggle.com/datasets/mobeenfatimah/student-career-success-prediction-dataset

Aluno: Felipe Erik Brito Costa da Silva  |  Matrícula: 20240028504

Repositório: https://github.com/zfelip/student_career_ia

## Objetivo

Comparação de quatro abordagens de modelagem: Sistema Especialista, Árvore de Decisão, Random Forest e Gradient Boosting, aplicadas à previsão de empregabilidade e colocação profissional de estudantes. O conjunto de dados contém 50.000 observações.

## Organização

- data/raw: conjunto de dados original.
- data/processed: dados preparados para regressão e classificação.
- notebooks/01_eda.ipynb e 02_preprocessing.ipynb: análise exploratória e preparação.
- notebooks/03_expert_system.ipynb: construção da base de conhecimento, inferência e análise das regras.
- notebooks/04_decision_tree.ipynb: treinamento e ajuste das árvores.
- notebooks/05_ensemble.ipynb: treinamento e ajuste dos ensembles.
- notebooks/06_evaluation_metrics.ipynb: métricas preditivas.
- notebooks/07_generalization.ipynb: validação cruzada e generalização.
- notebooks/08_computational_efficiency.ipynb: tempo, memória, complexidade, energia e CO₂.
- src: funções compartilhadas de modelagem, inferência, métricas, perfil e visualização.
- rules: regras de classificação e regressão.
- logs: registros de elaboração das regras.
- reports: resultados tabulares e gráficos.
- docs: metodologia e premissas energéticas.

## Procedimento experimental

Os dados são divididos em 80% de treinamento e 20% de teste, com semente aleatória 42 e estratificação na classificação. A validação cruzada possui cinco folds e o ajuste do pré-processamento é realizado apenas no treinamento.

Os experimentos dos notebooks 04 e 05 são executáveis independentemente e salvam os modelos ajustados. Os notebooks 06 a 08 recalculam as métricas e as avaliações a partir dos modelos treinados, além de apresentar os resultados consolidados. O ambiente de execução utiliza as dependências especificadas em requirements.txt.

## Instalação e limitação dos experimentos

O projeto foi desenvolvido em Python e utiliza as bibliotecas descritas em requirements.txt. Os arquivos dos modelos treinados (.pkl) não são versionados devido ao tamanho, mas podem ser reproduzidos a partir dos códigos disponibilizados. 

### Preparação do ambiente

Após clonar o repositório, criar e ativar um ambiente virtual no terminal PowerShell:
- git clone https://github.com/zfelip/student_career_ia.git
- cd student_career_ia

- python -m venv .venv.\.venv\Scripts\Activate.ps1
- python -m pip install -r requirements.txt

### Ordem de execução

Os notebooks devem ser executados no VS Code ou Jupyter, utilizando o ambiente Python configurado.

| Ordem | Notebook | Descrição |
|---|---|---|
| 1 | `01_eda.ipynb` | Análise exploratória dos dados |
| 2 | `02_preprocessing.ipynb` | Preparação dos conjuntos de dados |
| 3 | `03_expert_system.ipynb` | Avaliação do Sistema Especialista |
| 4 | `04_decision_tree.ipynb` | Treinamento e otimização das árvores de decisão |
| 5 | `05_ensemble.ipynb` | Treinamento do Random Forest e Gradient Boosting |
| 6 | `06_evaluation_metrics.ipynb` | Avaliação das métricas preditivas |
| 7 | `07_generalization.ipynb` | Análise da generalização dos modelos |
| 8 | `08_computational_efficiency.ipynb` | Análise de tempo, memória e eficiência energética |

Os notebooks 04 e 05 podem ser executados independentemente entre si, desde que os dados processados estejam disponíveis. A implementação do treinamento está concentrada em src/training.py, com as configurações dos algoritmos definidas em src/models.py. O processo utiliza divisão de 80% para treinamento e 20% para teste, semente aleatória 42 e validação cruzada com cinco folds. 

### Arquivos gerados

Durante a execução dos notebooks 04 e 05, os modelos ajustados são armazenados automaticamente na pasta models/ em arquivos .pkl. 
Esses arquivos não são necessários para consultar os notebooks e seus resultados salvos, mas são necessários para executar as etapas posteriores que carregam modelos treinados. 
Os resultados de execuções individuais são registrados em reports/tables/. As tabelas e figuras consolidadas incluídas no repositório documentam os experimentos realizados.

### Observações sobre reprodutibilidade

O tempo de treinamento depende das características do computador utilizado. Diferenças nas versões das bibliotecas também podem afetar os resultados. 
Os notebooks incluem resultados de execuções anteriores, permitindo a consulta às análises sem a necessidade de repetir imediatamente os treinamentos.

## Resultados

Na regressão, o menor RMSE no teste foi obtido por Random Forest (2,7751). Na classificação, Gradient Boosting obteve F1 de 0,8909. As diferenças entre modelos próximos devem ser interpretadas juntamente com os resultados de validação cruzada.

## Limitações

A disponibilidade temporal de Employability_Score para a previsão de Placement_Status não é especificada na base original. A análise de energia utiliza uma referência de potência de 15 W para o processador, não uma medição elétrica direta. As medições de memória efetuadas com tracemalloc representam as alocações rastreadas pela biblioteca.
