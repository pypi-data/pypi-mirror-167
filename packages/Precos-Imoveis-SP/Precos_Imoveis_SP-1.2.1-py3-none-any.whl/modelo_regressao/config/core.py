from pathlib import Path
from typing import Dict, List, Sequence, Union

from pydantic import BaseModel
from strictyaml import YAML, load

import modelo_regressao

# Diretorios do projeto
PACKAGE_ROOT = Path(modelo_regressao.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "modelos_treinados"

# As classes a seguir armazenarão 
# As configurações do projeto 
# Essas classes, chamadas modelos, 
# herdam da classe BaseModel do pydantic 
# Ele assegura a tipagem de saída dos dados

class AppConfig(BaseModel):
    """
    conf de aplicação.
    """

    nome_package: str
    arquivo_treinamento: str
    arquivo_teste: str
    arq_salvamento_pipeline: str


class ModeloConfig(BaseModel):
    """
    Todas configurações referentes ao modelo e feature engineering
    """

    alvo: str
    chave_de_API: str
    ID_pasta: str
    arquivos_drive: Dict[str, str]
    atributos: List[str]
    capping_params: Dict[str, Union[float, str]]
    regressao_params: Dict[str, Union[int, float, str]]
    tam_teste: float
    estado: int


class Config(BaseModel):
    """Objeto central de configuração."""

    app_config: AppConfig
    modelo_config: ModeloConfig


def localizar_arq_config() -> Path:
    """Localizar arquivo de config."""
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config não encontrada em {CONFIG_FILE_PATH!r}")


def pegar_config_yaml(caminho_config: Path = None) -> YAML:
    """Analisar YAML contendo a configuração do package."""

    if not caminho_config:
        caminho_config = localizar_arq_config()

    if caminho_config:
        with open(caminho_config, "r") as arq_conf:
            parseada_config = load(arq_conf.read())
            return parseada_config
    raise OSError(f"arquivo de configuação em {caminho_config} não encontrado.")


def criar_validar_config(parseada_config: YAML = None) -> Config:
    """validar arquivos de config."""
    if parseada_config is None:
        parseada_config = pegar_config_yaml()

    """retirar, dos dados do YAML obtido, as variáveis de cada Modelo pydantic"""
    _config = Config(
        app_config=AppConfig(**parseada_config.data),
        modelo_config=ModeloConfig(**parseada_config.data),
    )

    return _config


config = criar_validar_config()
