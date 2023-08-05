# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['corgi']

package_data = \
{'': ['*']}

install_requires = \
['PyMySQL>=1.0.2,<2.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'biopython>=1.79,<2.0',
 'cryptography>=36.0.1,<37.0.0',
 'dask>=2021.7.1,<2022.0.0',
 'fastai>=2.4.1,<3.0.0',
 'h5py>=3.1.0,<4.0.0',
 'httpx>=0.20.0,<0.21.0',
 'humanize>=3.10.0,<4.0.0',
 'optuna>=2.10.0,<3.0.0',
 'plotly>=5.3.1,<6.0.0',
 'progressbar2>=3.53.1,<4.0.0',
 'pyarrow>=4.0.1,<5.0.0',
 'termgraph>=0.5.3,<0.6.0',
 'torchapp>=0.2.3,<0.3.0',
 'wandb>=0.12.9,<0.13.0']

entry_points = \
{'console_scripts': ['corgi = corgi.apps:Corgi.inference_only_main',
                     'corgi-train = corgi.apps:Corgi.main']}

setup_kwargs = {
    'name': 'bio-corgi',
    'version': '0.2.2',
    'description': 'Classifier for ORganelle Genomes Inter alia',
    'long_description': '.. image:: https://raw.githubusercontent.com/rbturnbull/corgi/main/docs/images/corgi-banner.svg\n\n.. start-badges\n\n|testing badge| |coverage badge| |docs badge| |black badge| |git3moji badge| |torchapp badge|\n\n.. |testing badge| image:: https://github.com/rbturnbull/corgi/actions/workflows/testing.yml/badge.svg\n    :target: https://github.com/rbturnbull/corgi/actions\n\n.. |docs badge| image:: https://github.com/rbturnbull/corgi/actions/workflows/docs.yml/badge.svg\n    :target: https://rbturnbull.github.io/corgi\n    \n.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    \n.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/ee1b52dd314d6441e0aabc0e1e50dc2c/raw/coverage-badge.json\n    :target: https://rbturnbull.github.io/corgi/coverage/\n\n.. |git3moji badge| image:: https://img.shields.io/badge/git3moji-%E2%9A%A1%EF%B8%8F%F0%9F%90%9B%F0%9F%93%BA%F0%9F%91%AE%F0%9F%94%A4-fffad8.svg\n    :target: https://robinpokorny.github.io/git3moji/\n\n.. |torchapp badge| image:: https://img.shields.io/badge/MLOpps-torchapp-B1230A.svg\n    :target: https://rbturnbull.github.io/torchapp/\n        \n.. end-badges\n\n.. start-quickstart\n\nInstallation\n============\n\nThe software can be installed using ``pip``\n\n.. code-block:: bash\n\n    pip install bio-corgi\n\n.. warning ::\n\n    Do not try just `pip install corgi` because that is a different package.\n\nTo install the latest version from the repository, you can use this command:\n\n.. code-block:: bash\n\n    pip install git+https://github.com/rbturnbull/corgi.git\n\n.. note ::\n\n    Soon corgi will be able to be installed using conda.\n\n\nUsage\n============\n\nTo make predictions, run the ``corgi`` command line tool:\n\n.. code-block:: bash\n\n    corgi --fasta <input fasta file> --output-csv <results>\n\nFor more information about the other options, see the help with:\n\n.. code-block:: bash\n\n    corgi --help\n\nFor help on training a model with corgi, run:\n\n.. code-block:: bash\n\n    corgi-train --help\n\n\n.. end-quickstart\n\n\nCredits\n==================================\n\n* Robert Turnbull <robert.turnbull@unimelb.edu.au>\n* Created using torchapp (https://github.com/rbturnbull/torchapp)\n\n',
    'author': 'Robert Turnbull',
    'author_email': 'robert.turnbull@unimelb.edu.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rbturnbull/corgi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
