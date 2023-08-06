# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pege']

package_data = \
{'': ['*']}

install_requires = \
['pandas', 'pdbmender>=0.5.4,<0.6.0', 'torch>=1.9.0']

setup_kwargs = {
    'name': 'pege',
    'version': '1.2.1',
    'description': 'Protein embeddings to describe local electrostic enviroments',
    'long_description': '# Protein Environment Graph Embeddings (PEGE)\n\nProtein embeddings to describe local electrostic environments\n\n# Installation & Basic Usage\n\nPEGE is installable from the Pypi repo:\n```bash\npython3 -m pip install pege\n```\n\n[Pytorch Geometry](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html) also needs to be installed\n\nIn order for the structure preprocessing to work python2 and gawk need to installed.\n```bash\napt install python2 gawk\n```\n\nPege can be used to obtain protein embeddings as well as descriptors for specific `atom_numbers` from a `pdb` file:\n```python\nfrom pege import Pege\n\nprotein = Pege(<pdb>)\nprotein_emb = protein.get_protein()\nall_res_embs = protein.get_all_res_embs(chain="A")\n```\n\n# Documentation\nTBA\n\n# License\nThis source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.\n\n# Contacts\nPlease submit a github issue to report bugs and to request new features. Alternatively, you may email the developer [directly](mailto:pedro.reis@bayer.com).\n\n',
    'author': 'Pedro Reis',
    'author_email': 'pdreis@fc.ul.pt',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bayer-science-for-a-better-life/pege',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
