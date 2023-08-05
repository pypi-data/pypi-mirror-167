from __future__ import print_function
import io
import sys
import pprint
import shutil
import joblib
import google.auth
import typing as t
import numpy as np
import pandas as pd
from pathlib import Path
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from sklearn.pipeline import Pipeline
from modelo_regressao.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def requerimento_download(id_arq, nome_arq) -> None:
    """ Criar o requerimento do serviço de download da API do Google Drive
        Usando chave de API como autenticação"""
    try:
        servico = build('drive', 'v3', developerKey=config.modelo_config.chave_de_API)
        requerimento = servico.files().get_media(fileId=id_arq)
        arquivo = io.BytesIO()
        downloader = MediaIoBaseDownload(arquivo, requerimento)
        terminado = False
        
        while terminado is False:
            status, terminado = downloader.next_chunk()
            
        caminho = DATASET_DIR / nome_arq
        arquivo.seek(0)
        
        with open(caminho, 'wb') as f:
            shutil.copyfileobj(arquivo, f)

    except HttpError as erro:
        print(F'Ocorreu um erro: {erro}')
        arquivo = None
        

def download_datasets() -> None:
    """Baixar os Datasets necessários ao projeto armazenados na pasta pública da conta do Drive"""
    for nome_arquivo, id_arquivo in config.modelo_config.arquivos_drive.items():
        requerimento_download(id_arquivo, nome_arquivo)



def carregar_dataset(nome_arq: str) -> pd.DataFrame:
    """Carregar o dataset na pasta de destino do download"""  
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{nome_arq}"))
    
    return dataframe
    
    
def salvar_pipeline(*, pipeline_a_persistir: Pipeline) -> None:
    """
    Persistir a pipeline.
    Salvamento do modelo versionado 
    substitui o antigo
    """

    nome_arq_salvamento = f"{config.app_config.arq_salvamento_pipeline}1.2.1.pkl"
    caminho_salvamento = TRAINED_MODEL_DIR / nome_arq_salvamento

    remover_pipelines_antigas(arquivos_a_manter=[nome_arq_salvamento])
    joblib.dump(pipeline_a_persistir, caminho_salvamento)


def carregar_pipeline(*, nome_arquivo: str) -> Pipeline:
    """carregar uma pipeline persistida"""

    caminho_arquivo = TRAINED_MODEL_DIR / nome_arquivo
    modelo_treinado = joblib.load(filename=caminho_arquivo)
    return modelo_treinado


def remover_pipelines_antigas(*, arquivos_a_manter: t.List[str]) -> None:
    """
    Remove pipelines antigas
    para assegurar que haja
    uma versão de pacotes
    para um modelo
    """
    nao_deletar = arquivos_a_manter + ["__init__.py"]
    for arquivo_modelo in TRAINED_MODEL_DIR.iterdir():
        if arquivo_modelo.name not in nao_deletar:
            arquivo_modelo.unlink()
