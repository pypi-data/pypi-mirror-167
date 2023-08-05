from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from feature_engine.outliers import Winsorizer
from modelo_regressao.config.core import config

# Feature_engine oferece várias ferramentas de feature engineering
# Winsorizer faz uma limitação dos valores que as variáveis podem assumir
preco_pipe = Pipeline([("outliers", Winsorizer(**config.modelo_config.capping_params)),
                       ("scaler", StandardScaler()),
                       ("GBR", GradientBoostingRegressor(**config.modelo_config.regressao_params))])
