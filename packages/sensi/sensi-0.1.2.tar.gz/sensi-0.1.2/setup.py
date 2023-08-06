# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sensi', 'sensi.database', 'sensi.resources', 'sensi.tests']

package_data = \
{'': ['*'],
 'sensi.resources': ['nltk_data/corpora/*',
                     'nltk_data/corpora/stopwords/*',
                     'nltk_data/tokenizers/*',
                     'nltk_data/tokenizers/punkt/*',
                     'nltk_data/tokenizers/punkt/PY3/*']}

install_requires = \
['SQLAlchemy>=1.4.40,<2.0.0',
 'Sastrawi>=1.0.1,<2.0.0',
 'nltk>=3.7,<4.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['sensi = sensi:main']}

setup_kwargs = {
    'name': 'sensi',
    'version': '0.1.2',
    'description': 'analisis sentimen bahasa Indonesia menggunakan Naive-Bayes',
    'long_description': '<p align=center>Framework analisis sentiment teks Bahasa Indonesia, menggunakan Klasifikasi Naive-Bayes</p>\n\n## Dependensi\n\n```python\nsastrawi nltk numpy pandas sqlalchemy\n```\n\n## Instalasai\nBelum ada setup.py, install secara manual.\n1. copy isi repository kedalam directory proyek anda\n1. gunakan fungsi-fungsi yang diinginkan dengan meng-impor fungsi-2 tsb.\n\n## Penggunaan\n- Contoh penerapan dapat dilihat pada directory \'apis\' pada repository [flask-sk](https://github.com/GazDuckington/flask-sk)\n\n- Contoh sederhana:\n  ```python\n  from database.query import read_log_likelihood, read_log_prior\n  from resources.sentiment import predict_nbc\n  \n  logprior = read_log_prior()\n  loglikelihood = read_log_likelihood()\n  text = "contoh text yang ingin di analisis."\n  \n  print(predict_nbc(text, logprior, loglikelihood))\n  ```\nbaca ```resources/predictor.py``` untuk berbagai contoh lainnya.\n',
    'author': 'GazDuckington',
    'author_email': 'dianghazy@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/GazDuckington/nbc-sentimen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
