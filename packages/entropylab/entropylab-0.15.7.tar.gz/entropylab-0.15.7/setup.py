# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['entropylab',
 'entropylab.cli',
 'entropylab.components',
 'entropylab.dashboard',
 'entropylab.dashboard.pages',
 'entropylab.dashboard.pages.components',
 'entropylab.dashboard.pages.params',
 'entropylab.dashboard.pages.results',
 'entropylab.pipeline',
 'entropylab.pipeline.api',
 'entropylab.pipeline.params',
 'entropylab.pipeline.params.persistence',
 'entropylab.pipeline.params.persistence.sqlalchemy',
 'entropylab.pipeline.params.persistence.sqlalchemy.alembic',
 'entropylab.pipeline.params.persistence.sqlalchemy.alembic.versions',
 'entropylab.pipeline.params.persistence.tinydb',
 'entropylab.pipeline.results_backend',
 'entropylab.pipeline.results_backend.sqlalchemy',
 'entropylab.pipeline.results_backend.sqlalchemy.alembic',
 'entropylab.pipeline.results_backend.sqlalchemy.alembic.versions',
 'entropylab.quam']

package_data = \
{'': ['*'],
 'entropylab': ['flame/*'],
 'entropylab.dashboard': ['assets/*', 'assets/images/*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'alembic>=1.6.5,<2.0.0',
 'asyncpg>=0.25,<0.26',
 'bokeh>=2.3.0,<3.0.0',
 'celery>=5.2.3,<6.0.0',
 'dash-bootstrap-components>=1.0.0,<2.0.0',
 'dash>=2.4.1,<3.0.0',
 'dill>=0.3.3,<0.4.0',
 'distro>=1.7.0,<2.0.0',
 'dynaconf>=3.1.4,<4.0.0',
 'fastapi>=0.75,<0.78',
 'filelock>=3.7.1,<4.0.0',
 'graphviz>=0.16,<0.17',
 'h5py>=3.3.0,<4.0.0',
 'hiredis>=2.0.0,<3.0.0',
 'hupper>=1.10.3,<2.0.0',
 'jsonpickle>=2.0.0,<3.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'msgpack>=1.0.3,<2.0.0',
 'munch>=2.5.0,<3.0.0',
 'networkx>=2.6.0,<3.0.0',
 'numpy>=1.19,<2.0',
 'pandas>=1.2.3,<2.0.0',
 'param>=1.10.1,<2.0.0',
 'pika>=1.2.0,<2.0.0',
 'psutil>=5.9.0,<6.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pytz>=2021.3,<2023.0',
 'pyzmq>=22.3,<24.0',
 'qualang-tools>=0.12.0,<0.13.0',
 'redis>=4.1.0,<5.0.0',
 'requests>=2.27.1,<3.0.0',
 'sqlalchemy>=1.4.0,<2.0.0',
 'tenacity>=8.0.1,<9.0.0',
 'tinydb>=4.5.2,<5.0.0',
 'tzlocal>=4.1,<5.0',
 'waitress>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['entropy = entropylab.cli.main:main',
                     'n3p = entropylab.cli.main:main']}

setup_kwargs = {
    'name': 'entropylab',
    'version': '0.15.7',
    'description': '',
    'long_description': '![PyPI](https://img.shields.io/pypi/v/entropylab)\n[![discord](https://img.shields.io/discord/806244683403100171?label=QUA&logo=Discord&style=plastic)](https://discord.gg/7FfhhpswbP)\n\n[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4785097.svg)](https://doi.org/10.5281/zenodo.4785097)\n\n# Entropy\n\nEntropy is a lab workflow management package built for, but not limited-to, streamlining the process of running quantum information processing experiments. \n\nCheck out our [docs](https://docs.entropy-lab.io) for more information\n\nEntropy is built to solve a few major hurdles in experiment design: \n\n1. Building, maintaining and executing complex experiments\n2. Data collection\n3. Device management\n4. Calibration automation\n\nTo tackle these problems, Entropy is built around the central concept of a graph structure. The nodes of a graph give us a convenient way \nto brake down experiments into stages and to automate some tasks required in each node. For example data collection is automated, at least in part, \nby saving node data and code to a persistent database. \n\nDevice management is the challenge of managing the state and control of a variety of different resources. These include, but are not limited to, lab instruments. \nThey can also be computational resources, software resources or others. Entropy is built with tools to save such resources to a shared database and give nodes access to \nthe resources needed during an experiment. \n\nPerforming automatic calibration is an important reason why we built Entropy. This could be though of as the use case most clearly benefiting from shared resources, persistent \nstorage of different pieced of information and the graph structure. If the final node in a graph is the target experiment, then all the nodes between the root and that node are often \ncalibration steps. The documentation section will show how this can be done. \n\nThe Entropy system is built with concrete implementations of the various parts (database backend, resource management and others) but is meant to be completely customizable. Any or every part of the system can be tailored by end users. \n\n## Modules \n\n- ***Pipeline*** : A simple execution engine for a collection of nodes. Allows passing data between nodes and saving results to a database. Also includes a dashboard for viewing results. \n- ***Flame*** : An actor model execution engine \n- ***QuAM*** : The Quantum Abstract Machine. An abstraction layer above QPU to simplify experiment authoring and parameter management.\n \n\n## Installation\n\nInstallation is done from pypi using the following command\n\n```shell\npip install entropylab\n```\n\n## Versioning and the Alpha release \n\nThe current release of Entropy is version 0.x.x. You can learn more about the Entropy versioning scheme in the versioning\ndocument. There will more than likely be breaking changes to the API for a while until we learn how things should be done.\n\n',
    'author': 'Tal Shani',
    'author_email': 'tal@quantum-machines.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/entropy-lab/entropy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
