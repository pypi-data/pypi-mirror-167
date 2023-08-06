# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['relsad',
 'relsad.StatDist',
 'relsad.energy',
 'relsad.examples.CINELDI',
 'relsad.examples.IEEE16_modified',
 'relsad.examples.IEEE33',
 'relsad.examples.IEEE69',
 'relsad.examples.RBTS2',
 'relsad.examples.RBTS6',
 'relsad.examples.TEST10',
 'relsad.examples.load',
 'relsad.load',
 'relsad.loadflow.ac',
 'relsad.network',
 'relsad.network.components',
 'relsad.network.containers',
 'relsad.network.systems',
 'relsad.reliability.indices',
 'relsad.results.storage',
 'relsad.simulation',
 'relsad.simulation.monte_carlo',
 'relsad.simulation.sequence',
 'relsad.topology',
 'relsad.topology.ICT',
 'relsad.topology.load_flow',
 'relsad.utils',
 'relsad.visualization.plotting']

package_data = \
{'': ['*'], 'relsad.examples.load': ['data/*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0', 'pandas>=1.4.1,<2.0.0', 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'relsad',
    'version': '0.2.4',
    'description': 'A package that facilitates reliability investigations of power systems',
    'long_description': '\n|language tab| |code coverage tab| |contributors tab| |python version tab| |relsad version tab| |build tab| |license tab|\n\n######\nRELSAD\n######\n\n.. overview_start\n\n`RELSAD` -- RELiability tool for Smart and Active Distribution networks,\nis a Python-based reliability assessment tool that aims to function as\na foundation for reliabilitycalculation of modern distribution systems.\nThe tool allows for Monte Carlo simulation based reliability analysis of modern\ndistribution networks, and sequential simulation of the network\nbehavior with user-defined loading and failure evolution to investigate the impact\nof the introduction of for instance ICT components.\n\n\nThe package supports user-selected time steps over a user-defined time period.\nIn the tool, active components such as microgrids, distributed generation,\nbatteries, and electrical vehicles are implemented.\nTo evaluate smart power systems, ICT (Information and Communication Technology)\ncomponents such as automated switches, sensors, and control systems\nfor the power grid are also implemented.\nIn addition to component implementation, in order to evaluate the reliability\nof such complex systems, the complexity, dependencies within a system, and interdependencies between systems and components are accounted for.\n\nThe tool can be used in modern distribution network development to evaluate\nthe influence of active components on the network reliability. Relevant use cases\ninclude investigating how:\n\n1. The introduction of microgrids with active generation\n   affects the customers in the distribution network and vice versa\n2. Vehicle\\-to\\-grid strategies might mitigate load peaks and\n   improve the distribution network reliability\n3. The reliability of the ICT network impacts the\n   distribution network reliability\n\n.. overview_end\n\n============\nInstallation\n============\n\nSee https://relsad.readthedocs.io/en/latest/installation.html.\n\n========\nFeatures\n========\n\n- Monte Carlo simulation based reliability analysis of modern distribution networks\n- Sequential simulation of the network behavoir with user-defined loading and failure evolution\n\n============\nDependencies\n============\n\nThe package dependencies can be found in `pyproject.toml`.\n\n=====\nUsage\n=====\n\nExamples using well known test networks are included and presented in\nhttps://relsad.readthedocs.io/en/latest/usage.html.\n\n=============\nDocumentation\n=============\n\nThe official documentation is hosted on Read the Docs: https://relsad.readthedocs.io/en/latest/\n\n============\nContributors\n============\n\nWe welcome and recognize all contributions. You can see a list of current contributors in the contributors tab.\n\n\n====\nHelp\n====\n\nIf you have questions, feel free to contact the author.\n\n\n.. |contributors tab| image:: https://img.shields.io/github/contributors/stinefm/relsad\n   :target: https://github.com/stinefm/relsad/graphs/contributors\n\n.. |language tab| image:: https://img.shields.io/github/languages/top/stinefm/relsad\n   :target: https://www.python.org/\n\n.. |code coverage tab| image:: https://img.shields.io/codecov/c/github/stinefm/relsad\n   :target: https://app.codecov.io/github/stinefm/relsad\n\n.. |python version tab| image:: https://img.shields.io/pypi/pyversions/relsad\n\n.. |relsad version tab| image:: https://img.shields.io/pypi/v/relsad\n   :target: https://pypi.org/project/relsad/\n\n.. |build tab| image:: https://img.shields.io/github/workflow/status/stinefm/relsad/ci-cd\n   :target: https://github.com/stinefm/relsad/actions\n\n.. |docs tab| image:: https://readthedocs.org/projects/relsad/badge/?version=latest\n   :target: https://relsad.readthedocs.io/en/latest/\n\n.. |license tab| image:: https://img.shields.io/github/license/stinefm/relsad\n   :target: https://github.com/stinefm/relsad/blob/main/LICENSE\n',
    'author': 'Stine Fleischer Myhre',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stinefm/relsad',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
