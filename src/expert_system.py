"""Sistema especialista: base SE-ENTAO armazenada em rules/, inferencia separada."""
from __future__ import annotations
import ast
from pathlib import Path
import re
import numpy as np

BASE = Path(__file__).resolve().parent.parent / "rules"

class Rules:
    """Motor de inferencia deterministico por encadeamento para frente.

    Prioridade: primeira regra satisfeita; default usado se nenhuma se aplica.
    """
    def __init__(self, task, defaults, rules):
        self.task = task
        self.defaults = defaults
        self.rules = rules

    def predict(self, X):
        result = []
        for values in X.itertuples(index=False, name=None):
            row = dict(zip(X.columns, values))
            prediction = self.defaults
            for rule in self.rules:
                matched = True
                for col, op, threshold in rule["conditions"]:
                    value = row[col]
                    if op == ">=": ok = value >= threshold
                    elif op == "<": ok = value < threshold
                    elif op == "==": ok = value == threshold
                    else: raise ValueError(f"Operador desconhecido: {op}")
                    if not ok:
                        matched = False
                        break
                if matched:
                    prediction = rule["value"]
                    break
            result.append(prediction)
        return np.asarray(result)

def load_rules(task, rules_directory=BASE):
    """Carrega as regras fixas em texto; nao estima limites usando dados de teste.

    Os valores padrao explicitamente definidos no arquivo de configuracao sao usados
    apenas quando nenhuma regra corresponde. Em classificacao C1 tem prioridade.
    """
    if task not in ("classification", "regression"):
        raise ValueError("Tarefa invalida")
    folder = Path(rules_directory)
    file = folder / ("regras_classificacao.txt" if task == "classification" else "regras_regressao.txt")
    rules=[]
    line_re = re.compile(r"^\s*\d+\.\s*Tipo\s+(.+?)\s*\|\s*SE\s+(.+?)\s+ENTÃO\s+(.+?)\s*$")
    cond_re = re.compile(r"\([^()]+\)")
    for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match=line_re.match(line)
        if not match: raise ValueError(f"Regra mal formatada na linha {number}: {line}")
        typ,conditions_txt,output_txt=match.groups()
        conditions=[ast.literal_eval(piece) for piece in cond_re.findall(conditions_txt)]
        if not conditions or any(not isinstance(c,tuple) or len(c)!=3 for c in conditions):
            raise ValueError(f"Condicoes invalidas na linha {number}")
        output=ast.literal_eval(output_txt)
        rules.append({"type":typ.strip(),"conditions":conditions,"value":output})
    if not rules: raise ValueError("Base de regras vazia")
    # Na base atual, as faixas cobrem todos os casos; o default e defensivo.
    default=0 if task == "classification" else rules[0]["value"]
    return Rules(task, default, rules)
