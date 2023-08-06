# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkquartodocs']

package_data = \
{'': ['*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0', 'mkdocs>=1.3.1,<2.0.0', 'nbformat>=5.5.0,<6.0.0']

entry_points = \
{'mkdocs.plugins': ['mkquartodocs = mkquartodocs.plugin:MkDocstringPlugin']}

setup_kwargs = {
    'name': 'mkquartodocs',
    'version': '0.2.0',
    'description': '',
    'long_description': "# mkquartodocs\n\n**Make gorgeous reproducible documentation with quarto and mkdocs**\n\nIt is a plugin for [mkdocs](https://www.mkdocs.org/) that renders [quarto](https://quarto.org) markdown documents into\ngithub, so they are built with the rest of the documentation.\n\n### Why?\n\nIn many instances the documentation contains runnable code, and it makes sense that you verify that the code runs and\nkeep the output of the code in sync with the current status of the document and software packages involved.\n\n**But mainly** I really got tired of manually rendering documents and copying outpus.\n\n## Usage\n\n1. Install the dependencies: [Installation](#installation)\n1. Add the plugin to your configuration: [Configuration](#configuration)\n1. Add `.qmd` files to your `./docs/` directoy\n1. Run `mkdocs build`\n\n## Installation\n\n1. Make sure you have quarto installed in your computer.\n\n   - https://quarto.org/docs/get-started/\n\n1. Install `mkquartodocs`\n\n```shell\npip install mkquartodocs\n```\n\n## Configuration\n\nAdd `mkquartodocs` to your plugins in your `mkdocs.yml`\n\n```yaml\n# Whatever is in your mkdocs.yml configuration file....\n# ...\n\nplugins:\n  - mkquartodocs\n\n```\n\nAvailable configuration options:\n\n- **quarto_path**: Specifies where to look for the quarto executable.\n- **keep_output**: If true it will skip the cleanup step in the directory.\n- **ignore**: a python regular expressions that if matched will mark the file to not be rendered. Note that they need to\n  be full matches\n\n```yaml\n# Whatever is in your mkdocs.yml configuration file....\n# ...\n\nplugins:\n  - mkquartodocs:\n      quarto_path: /home/my_folder/some/weird/place/to/have/executables/quarto\n      keep_output: true\n      ignore: (.*broken.*.qmd)|(.*page[0-9].qmd)\n\n```\n\n## Running\n\n**NOTHING !!! you do not have to run it manually!!**\n\nWhen you call `mkdocs build`, it should automatically find your `.qmd` files, render them, generate the output and clean\nafter itself.\n\n# TODO\n\nThe things that need to/could be added to the project:\n\n- [ ] quarto project support\n- [ ] render in temporary directory, posibly with a 'safe' argument\n- [ ] addition of files not in the docs directory, 'include' argument\n",
    'author': 'J. Sebastian Paez',
    'author_email': 'jspaezp@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>3.8,<3.12',
}


setup(**setup_kwargs)
