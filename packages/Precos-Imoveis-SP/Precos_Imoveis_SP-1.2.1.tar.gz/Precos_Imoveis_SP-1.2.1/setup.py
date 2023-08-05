from pathlib import Path

from setuptools import find_packages, setup


# O arquivo setup.py primariamente tem dois propósitos:
# Inclui escolhas e metadados sobre o programa, como nome do package, versão, autor, conjuntos de dados, etc...
# Segundo, serve de interface de linha de comando por onde os comandos de packaging serão executados
NAME = "Precos_Imoveis_SP"
DESCRIPTION = "package contendo modelo de regressao para predicao de precos de imoveis"
URL = "https://github.com/GHM-ML"
EMAIL = "gabe.hm.ml@gmail.com"
AUTHOR = "GHM-ML"
REQUIRES_PYTHON = ">=3.6.0"

long_description = DESCRIPTION

about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / "requerimentos"
PACKAGE_DIR = ROOT_DIR / "modelo_regressao"


def list_reqs(fname="requerimentos.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()

setup(
    name=NAME,
    version="1.2.1",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"modelo_regressao": ["VERSAO"]},
    install_requires=list_reqs(),
    extras_require={},
    license = "MIT",
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
