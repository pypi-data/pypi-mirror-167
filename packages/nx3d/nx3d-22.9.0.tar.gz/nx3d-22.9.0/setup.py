# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nx3d_ekalosak']

package_data = \
{'': ['*'], 'nx3d_ekalosak': ['data/*']}

install_requires = \
['Panda3D>=1.10.12,<2.0.0', 'networkx>=2.8.6,<3.0.0', 'numpy>=1.23.3,<2.0.0']

setup_kwargs = {
    'name': 'nx3d',
    'version': '22.9.0',
    'description': 'The missing 3D plotting functionality for networkx',
    'long_description': "# nx3d\n\nThe missing 3D plotting functionality for the excellent `networkx` Python package.\n\n![frucht graph](./data/frucht.gif)\n\n# Installation\nIn your shell:\n```sh\npip install nx3d\n```\n\n# Test\nIn your Python REPL:\n```python\nimport nx3d\nnx3d.demo()\n```\n\n# Usage\nIn your Python code:\n```python\nimport networkx as nx\nimport nx3d\n\ng = nx.frucht_graph()\nnx3d.plot(g)\n```\n\nFor more customization, use the `nx3d.plot_nx3d()` function.\n\n# Contribute\nThank you for considering contributing to `nx3d`.\n\nCurrently, there's no testing or enforced formatting with CI to keep this young project lightweight.\nWith that in mind, the pre-commit hooks defined in `.pre-commit-config.yaml` apply linting and formatting to keep the\nproject clean. Please use the pre-commit hooks before making a PR.\n\n## Set up pre-commit\nFrom this project's root, initialize pre-commit as follows:\n\n```sh\npre-commit install\npre-commit run -a\n```\n",
    'author': 'Eric Kalosa-Kenyon',
    'author_email': 'helloateric@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
