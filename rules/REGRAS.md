# Base de conhecimento do sistema especialista
A base de conhecimento reúne cinco regras heurísticas de regressão e seis de classificação, representadas por condições SE–ENTÃO. As regras são armazenadas em arquivos de texto e interpretadas pelo motor de inferência implementado em src/expert_system.py.

## Regressão
As cinco regras estabelecem faixas da variável Interview_Score para estimar Employability_Score. Os intervalos cobrem os valores possíveis sem sobreposição: abaixo de 67, de 67 a menos de 75, de 75 a menos de 82, de 82 a menos de 88, e a partir de 88. Cada faixa está associada a uma estimativa numérica.

## Classificação
As seis regras combinam condições sobre Interview_Score, Programming_Skill e Employability_Score para estimar Placement_Status. A avaliação segue a ordem das regras registradas. A regra C1 tem prioridade sobre as demais em situações nas quais mais de uma condição é satisfeita.

## Inferência e representação numérica
O motor avalia sequencialmente as condições e retorna a consequência da primeira regra aplicável. A separação entre o motor e a base de conhecimento permite consultar e manter as regras independentemente do algoritmo de inferência.

As previsões de regressão são exibidas com duas casas decimais na exposição dos resultados. Os arquivos de regras preservam os valores utilizados nos cálculos experimentais.

## Protocolo de avaliação
Os conjuntos de treinamento e teste seguem a divisão experimental de 80% e 20%. A definição e a revisão dos parâmetros das regras consideram os dados de treinamento, e o conjunto de teste é reservado para avaliar o desempenho preditivo. A comparação utiliza as mesmas partições aplicadas às demais abordagens.
