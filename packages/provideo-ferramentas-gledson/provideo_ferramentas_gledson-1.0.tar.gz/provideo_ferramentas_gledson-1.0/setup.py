from importlib.resources import read_text
from setuptools import setup,find_packages
from pathlib import Path

setup(
    name='provideo_ferramentas_gledson',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de video',
    long_description=Path('README.md').read_text(), # chamar a descrição do arquivo README.md
    author='Gledson Silva',
    author_email='gle1984@gmail.com',
    keywords=['camera','video','processamento'], # palavras chaves para ajudar na busca pela biblioteca
    packages=find_packages() # para quando o usuario instalar todas as dependencias que seu pacote precisa
)