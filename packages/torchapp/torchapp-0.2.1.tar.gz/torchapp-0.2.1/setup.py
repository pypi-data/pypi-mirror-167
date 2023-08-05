# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchapp',
 'torchapp.callbacks',
 'torchapp.cookiecutter.tests',
 'torchapp.cookiecutter.{{cookiecutter.project_slug}}.docs',
 'torchapp.cookiecutter.{{cookiecutter.project_slug}}.tests',
 'torchapp.cookiecutter.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}',
 'torchapp.examples',
 'torchapp.tuning']

package_data = \
{'': ['*'],
 'torchapp': ['bibtex/*',
              'cookiecutter/*',
              'cookiecutter/.github/ISSUE_TEMPLATE/*',
              'cookiecutter/.github/workflows/*',
              'cookiecutter/{{cookiecutter.project_slug}}/*',
              'cookiecutter/{{cookiecutter.project_slug}}/.github/ISSUE_TEMPLATE/*',
              'cookiecutter/{{cookiecutter.project_slug}}/.github/workflows/*']}

install_requires = \
['Pillow>=9.0.1,<10.0.0',
 'PyYAML>=6.0,<7.0',
 'click==8.0.4',
 'cookiecutter>=2.1.1,<3.0.0',
 'fastai>=2.5.3,<3.0.0',
 'mlflow>=1.25.1,<2.0.0',
 'numpy>=1.22.0,<2.0.0',
 'optuna>=2.10.0,<3.0.0',
 'pandas>=1.3.5,<2.0.0',
 'pybtex>=0.24.0,<0.25.0',
 'pybtexnbib>=0.1.1,<0.2.0',
 'pyjwt>=2.4.0',
 'rich>=10.16.1,<11.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scikit-optimize>=0.9.0,<0.10.0',
 'scipy>=1.9.1,<2.0.0',
 'torch>=1.12.1,<2.0.0',
 'torchvision>=0.13.1,<0.14.0',
 'typer>=0.4.0,<0.5.0',
 'wandb>=0.12.9,<0.13.0']

entry_points = \
{'console_scripts': ['torchapp = torchapp.main:app',
                     'torchapp-imageclassifier = '
                     'torchapp.examples.image_classifier:ImageClassifier.main']}

setup_kwargs = {
    'name': 'torchapp',
    'version': '0.2.1',
    'description': 'A wrapper for fastai projects to create easy command-line inferfaces and manage hyper-parameter tuning.',
    'long_description': '==========\ntorchapp\n==========\n\n.. image:: https://raw.githubusercontent.com/rbturnbull/torchapp/master/docs/images/torchapp-banner.svg\n\n.. start-badges\n\n|torchapp badge| |testing badge| |coverage badge| |docs badge| |black badge| |git3moji badge|\n\n\n.. |torchapp badge| image:: https://img.shields.io/badge/MLOpps-torchapp-B1230A.svg\n    :target: https://rbturnbull.github.io/torchapp/\n\n.. |testing badge| image:: https://github.com/rbturnbull/torchapp/actions/workflows/testing.yml/badge.svg\n    :target: https://github.com/rbturnbull/torchapp/actions\n\n.. |docs badge| image:: https://github.com/rbturnbull/torchapp/actions/workflows/docs.yml/badge.svg\n    :target: https://rbturnbull.github.io/torchapp\n    \n.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    \n.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/506563cd9b49c8126284e34864c862d0/raw/coverage-badge.json\n    :target: https://rbturnbull.github.io/torchapp/coverage/\n\n.. |git3moji badge| image:: https://img.shields.io/badge/git3moji-%E2%9A%A1%EF%B8%8F%F0%9F%90%9B%F0%9F%93%BA%F0%9F%91%AE%F0%9F%94%A4-fffad8.svg\n    :target: https://robinpokorny.github.io/git3moji/\n\n.. end-badges\n\nA wrapper for PyTorch projects to create easy command-line inferfaces and manage hyper-parameter tuning.\n\nDocumentation at https://rbturnbull.github.io/torchapp/\n\n.. start-quickstart\n\nInstallation\n=======================\n\nThe software can be installed using ``pip``\n\n.. code-block:: bash\n\n    pip install torchapp\n\nTo install the latest version from the repository, you can use this command:\n\n.. code-block:: bash\n\n    pip install git+https://github.com/rbturnbull/torchapp.git\n\n\nWriting an App\n=======================\n\nInherit a class from :code:`TorchApp` to make an app. The parent class includes several methods for training and hyper-parameter tuning. \nThe minimum requirement is that you fill out the dataloaders method and the model method.\n\nThe :code:`dataloaders` method requires that you return a fastai Dataloaders object. This is a collection of dataloader objects. \nTypically it contains one dataloader for training and another for testing. For more information see https://docs.fast.ai/data.core.html#DataLoaders\nYou can add parameter values with typing hints in the function signature and these will be automatically added to the train and show_batch methods.\n\nThe :code:`model` method requires that you return a pytorch module. Parameters in the function signature will be added to the train method.\n\nHere\'s an example for doing logistic regression:\n\n.. code-block:: Python\n   \n    #!/usr/bin/env python3\n    from pathlib import Path\n    import pandas as pd\n    from torch import nn\n    from fastai.data.block import DataBlock, TransformBlock\n    from fastai.data.transforms import ColReader, RandomSplitter\n    import torchapp as ta\n    from torchapp.blocks import BoolBlock\n\n\n    class LogisticRegressionApp(ta.TorchApp):\n        """\n        Creates a basic app to do logistic regression.\n        """\n\n        def dataloaders(\n            self,\n            csv: Path = ta.Param(help="The path to a CSV file with the data."),\n            x: str = ta.Param(default="x", help="The column name of the independent variable."),\n            y: str = ta.Param(default="y", help="The column name of the dependent variable."),\n            validation_proportion: float = ta.Param(\n                default=0.2, help="The proportion of the dataset to use for validation."\n            ),\n            batch_size: int = ta.Param(\n                default=32,\n                help="The number of items to use in each batch.",\n            ),\n        ):\n\n            datablock = DataBlock(\n                blocks=[TransformBlock, BoolBlock],\n                get_x=ColReader(x),\n                get_y=ColReader(y),\n                splitter=RandomSplitter(validation_proportion),\n            )\n            df = pd.read_csv(csv)\n\n            return datablock.dataloaders(df, bs=batch_size)\n\n        def model(self) -> nn.Module:\n            """Builds a simple logistic regression model."""\n            return nn.Linear(in_features=1, out_features=1, bias=True)\n\n        def loss_func(self):\n            return nn.BCEWithLogitsLoss()\n\n\n    if __name__ == "__main__":\n        LogisticRegressionApp.main()\n   \n\nProgrammatic Interface\n=======================\n\nTo use the app in Python, simply instantiate it:\n\n.. code-block:: Python\n\n   app = LogisticRegressionApp()\n\nThen you can train with the method:\n\n.. code-block:: Python\n\n   app.train(training_csv_path)\n\nThis takes the arguments of both the :code:`dataloaders` method and the :code:`train` method. The function signature is modified so these arguments show up in auto-completion in a Jupyter notebook.\n\nPredictions are made by simply calling the app object.\n\n.. code-block:: Python\n\n    app(data_csv_path)\n\nCommand-Line Interface\n=======================\n\nCommand-line interfaces are created simply by using the Poetry package management tool. Just add a line like this in :code:`pyproject.toml`\n\n.. code-block:: toml\n\n    logistic = "logistic.apps:LogisticRegressionApp.main"\n\nNow we can train with the command line:\n\n.. code-block:: bash\n\n    logistic train training_csv_path\n\nAll the arguments for the dataloader and the model can be set through arguments in the CLI. To see them run\n\n.. code-block:: bash\n\n    logistic train -h\n\nPredictions are made like this:\n\n.. code-block:: bash\n\n    logistic predict data_csv_path\n\nHyperparameter Tuning\n=======================\n\nAll the arguments in the dataloader and the model can be tuned using Weights & Biases (W&B) hyperparameter sweeps (https://docs.wandb.ai/guides/sweeps). In Python, simply run:\n\n.. code-block:: python\n\n    app.tune(runs=10)\n\nOr from the command line, run\n\n.. code-block:: bash\n\n    logistic tune --runs 10\n\nThese commands will connect with W&B and your runs will be visible on the wandb.ai site.\n\nProject Generation\n=======================\n\nTo use a template to construct a package for your app, simply run:\n\n.. code-block:: bash\n\n    torchapp\n\n.. end-quickstart\n\nCredits\n=======================\n\n.. start-credits\n\ntorchapp was created created by Robert Turnbull with contributions from Jonathan Garber and Simone Bae.\n\nCitation details to follow.\n\nLogo elements derived from icons by `ProSymbols <https://thenounproject.com/icon/flame-797130/>`_ and `Philipp Petzka <https://thenounproject.com/icon/parcel-2727677/>`_.\n\n.. end-credits',
    'author': 'Robert Turnbull',
    'author_email': 'robert.turnbull@unimelb.edu.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rbturnbull/torchapp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
