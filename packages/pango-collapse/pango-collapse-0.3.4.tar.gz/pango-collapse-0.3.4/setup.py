# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pango_collapse']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21,<=1.23.2',
 'pandas>=1.3,<=1.4.4',
 'pango-aliasor>=0.2.0,<0.3.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['pango-collapse = pango_collapse.main:app']}

setup_kwargs = {
    'name': 'pango-collapse',
    'version': '0.3.4',
    'description': '',
    'long_description': '# Pango-collapse \n\n[![](https://img.shields.io/pypi/v/pango-collapse.svg)](https://pypi.org/project/pango-collapse/)\n[![tests](https://github.com/MDU-PHL/pango-collapse/actions/workflows/tests.yaml/badge.svg)](https://github.com/MDU-PHL/pango-collapse/actions/workflows/tests.yaml)\n\nCLI to collapse Pango linages for reporting\n\n[![](collapse.gif)](https://mdu-phl.github.io/pango-watch/tree/)\n\n## Install \n\nInstall from pypi with pip.\n\n```\npip install pango-collapse\n```\n\n## Usage\n\n`pango-collapse` takes a CSV file of SARS-CoV-2 samples (`input.csv`) with a column (default `Lineage`) indicating the pango lineage of the samples (e.g. output from pangoLEARN, nextclade, USHER, etc). \n\n```\n# input.csv\nLineage\nBA.5.2.1\nBA.4.6\nBE.1\n```\n\n`pango-collapse` will collapse lineages up to the first user defined parent lineage (specified in a text file with `--collapse-file`). If the sample lineage has no parent lineage in the user defined collapse file the lineage will be collapsed up to either `A` or `B`. By default `pango-collapse` uses the collapse file found [here](https://github.com/MDU-PHL/pango-collapse/blob/main/pango_collapse/collapse.txt).\n\n```\n# collapse.txt\nBA.5\nBE.1\n```\n\n`pango-collapse` will produce an output file which is a copy of the input file plus `Lineage_full` (the uncompressed lineage) and `Lineage_family` (the lineage compressed up to) columns. \n\n\n```bash\npango-collapse input.csv --collapse-file collapse.txt -o output.csv \n```\n\n```\n# output.csv \nLineage,Lineage_full,Lineage_family\nBA.5.2.1,B.1.1.529.5.2.1,BA.5\nBA.4.6,B.1.1.529.4.6,B\nBE.1,B.1.1.529.5.3.1.1,BE.1\n```\n',
    'author': 'wytamma',
    'author_email': 'wytamma.wirth@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
