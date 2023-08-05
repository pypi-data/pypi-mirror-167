import numpy as np
from modelo_regressao.processamento import gerenciador_dados
from config.core import config
from pipeline import preco_pipe
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

def executar_treinamento() -> None:
    gerenciador_dados.download_datasets()
    # ler arquivo de treino do modelo
    data = gerenciador_dados.carregar_dataset(nome_arq=config.app_config.arquivo_treinamento)
    # dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.modelo_config.atributos],
        data[config.modelo_config.alvo],
        test_size=config.modelo_config.tam_teste,
        random_state=config.modelo_config.estado, #random_state para reproducibilidade
    )
    
    preco_pipe.fit(X_train, y_train)


    # salvar modelo treinado
    gerenciador_dados.salvar_pipeline(pipeline_a_persistir=preco_pipe)


if __name__ == "__main__":
    executar_treinamento()
