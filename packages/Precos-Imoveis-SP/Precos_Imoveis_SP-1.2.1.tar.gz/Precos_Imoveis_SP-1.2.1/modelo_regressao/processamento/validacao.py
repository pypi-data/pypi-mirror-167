from typing import List, Tuple, Optional

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from modelo_regressao.config.core import config

# Modelos pydantic para garantir os tipos das variáveis a entrarem no modelo
class HouseDataInputSchema(BaseModel):
    area: Optional[float]
    quartos: Optional[float]
    banheiros: Optional[float]
    vagas: Optional[float]
    valor: Optional[float]
    V001: Optional[float]
    V002: Optional[float]
    V003: Optional[float]
    V004: Optional[float]
    V005: Optional[float]
    V006: Optional[float]
    V007: Optional[float]
    V008: Optional[float]
    V009: Optional[float]
    V010: Optional[float]
    V011: Optional[float]
    V012: Optional[float]

class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
