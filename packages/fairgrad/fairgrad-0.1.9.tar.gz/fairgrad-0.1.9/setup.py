# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fairgrad', 'fairgrad.torch']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20', 'torch>=1.0']

setup_kwargs = {
    'name': 'fairgrad',
    'version': '0.1.9',
    'description': '',
    'long_description': '# FairGrad: Fairness Aware Gradient Descent\n[![Documentation Status](https://readthedocs.org/projects/fairgrad/badge/?version=latest)](https://fairgrad.readthedocs.io/en/latest/?badge=latest)\n[![PyPI version](https://badge.fury.io/py/fairgrad.svg)](https://badge.fury.io/py/fairgrad)\n[![GitHub Actions (Tests)](https://github.com/saist1993/fairgrad/actions/workflows/build.yaml/badge.svg)](https://github.com/saist1993/fairgrad/actions/workflows/build.yaml)\n<a href="https://arxiv.org/abs/2206.10923"><img src="http://img.shields.io/badge/Paper-PDF-red.svg"></a>\n\nFairGrad, is an easy to use general purpose approach to enforce fairness for gradient descent based methods. \n\n# Getting started: \nYou can get ```fairgrad``` from pypi, which means it can be easily installed via ```pip```:\n```\npip install fairgrad\n```\n\n# Documentation\nThe documenation can be found at [read the docs](https://fairgrad.readthedocs.io/en/latest/index.html)\n\n# Example usage \nTo use fairgrad simply replace your pytorch cross entropy loss with fairgrad cross entropy loss. \nAlongside, regular pytorch cross entropy arguments, it expects following extra arguments.\n\n```\ny_train (np.asarray[int], Tensor, optional): All train example\'s corresponding label\ns_train (np.asarray[int], Tensor, optional): All train example\'s corresponding sensitive attribute. This means if there\n        are 2 sensitive attributes, with each of them being binary. For instance gender - (male and female) and\n        age (above 45, below 45). Total unique sentive attributes are 4.\nfairness_measure (string): Currently we support "equal_odds", "equal_opportunity", "accuracy_parity", and \n                           "demographic_parity". Note that demographic parity is only supported for binary case.\nepsilon (float, optional): The slack which is allowed for the final fairness level.\nfairness_rate (float, optional): Parameter which intertwines current fairness weights with sum of previous fairness rates.\n```\n\n```python\n# Note this is short snippet. One still needs to models and iterators.\n# Full worked out example is available here - @TODO\n\nfrom fairgrad.torch import CrossEntropyLoss\n\n# define cross entropy loss \ncriterion = CrossEntropyLoss(fairness_related_meta_data=fairness_related_meta_data)\n\n# Train loop\n\nfor inputs, labels, protected_attributes in train_iterator:\n    model.train()\n    optimizer.zero_grad()\n    output = model(inputs)\n    loss = criterion(output, labels, protected_attributes, mode=\'train\')\n    loss.backward()\n    optimizer.step()\n```\n\n\nWe highly recommend to **standardize features** by removing the mean and scaling to unit variance.\nThis can be done using standard scalar module in sklearn.\n\n# Citation\n```\n@article{maheshwari2022fairgrad,\n  title={FairGrad: Fairness Aware Gradient Descent},\n  author={Maheshwari, Gaurav and Perrot, Micha{\\"e}l},\n  journal={arXiv preprint arXiv:2206.10923},\n  year={2022}\n}\n```\n',
    'author': 'gmaheshwari',
    'author_email': 'gaurav.maheshwari@inria.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
