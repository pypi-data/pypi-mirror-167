import typing as t

import numpy as np
import pandas as pd

from modelo_regressao.config.core import config
from modelo_regressao.processamento.gerenciador_dados import carregar_pipeline

nome_arq_pipeline = f"{config.app_config.arq_salvamento_pipeline}1.2.1.pkl"
_preco_pipe = carregar_pipeline(nome_arquivo=nome_arq_pipeline)

# Função para fazer predição com a pipeline
def predizer(*,dados_entrada: t.Union[pd.DataFrame, dict],) -> dict:
    dados = pd.DataFrame(dados_entrada)
    predicoes = _preco_pipe.predict(X=dados[config.modelo_config.atributos])
    results = {"predicoes": [pred for pred in predicoes], 
               "versao": "1.2.1"}
    return results
