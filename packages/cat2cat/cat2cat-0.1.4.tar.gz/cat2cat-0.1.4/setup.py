# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cat2cat', 'cat2cat.data']

package_data = \
{'': ['*']}

install_requires = \
['importlib-resources>=5.9.0,<6.0.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'scikit-learn>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'cat2cat',
    'version': '0.1.4',
    'description': 'Unifying an inconsistently coded categorical variable in a panel/longtitudal dataset.',
    'long_description': '# cat2cat \n\n<a href=\'https://github.com/polkas/py-cat2cat\'>\n<img src=\'https://raw.githubusercontent.com/Polkas/cat2cat/master/man/figures/cat2cat_logo.png\'  style="display:block;margin-left:auto;margin-right:auto;width:200px;" width="200px" alt="cat2cat logo"/>\n</a>\n\n<hr>\n\n<div>\n<a href="https://github.com/polkas/py-cat2cat/actions">\n<img src="https://github.com/polkas/py-cat2cat/workflows/ci/badge.svg" alt="Build Status">\n</a>\n<a href="https://codecov.io/gh/Polkas/py-cat2cat">\n<img src="https://codecov.io/gh/Polkas/py-cat2cat/branch/main/graph/badge.svg" alt="codecov">\n</a>\n<a href="https://pypi.org/project/cat2cat/">\n<img src="https://img.shields.io/pypi/v/cat2cat.svg" alt="pypi">\n</a>\n<div>\n\n<br>\n\n### Unifying an inconsistently coded categorical variable in a panel/longtitudal dataset\n\nThere is offered the cat2cat procedure to map a categorical variable according to a mapping (transition) table between two different time points. The mapping (transition) table should to have a candidate for each category from the targeted for an update period. The main rule is to replicate the observation if it could be assigned to a few categories, then using simple frequencies or statistical methods to approximate probabilities of being assigned to each of them.\n\nThis algorithm was invented and implemented in the paper by (Nasinski, Majchrowska and Broniatowska (2020) doi:10.24425/cejeme.2020.134747).\n\n## Installation\n\n```bash\n$ pip install cat2cat\n```\n\n## Usage\n\nFor more examples and descriptions please vist [**the example notebook**](https://py-cat2cat.readthedocs.io/en/latest/example.html)\n\n### load example data\n\n```python\n# cat2cat datasets\nfrom cat2cat.datasets import load_trans, load_occup\ntrans = load_trans()\noccup = load_occup()\n```\n\n### Low-level functions\n\n```python\nfrom cat2cat.mappings import get_mappings, get_freqs, cat_apply_freq\n\n# convert the mapping table to two association lists\nmappings = get_mappings(trans)\n# get a variable levels freqencies\ncodes_new = occup.code[occup.year == 2010].values\nfreqs = get_freqs(codes_new)\n# apply the frequencies to the (one) association list\nmapp_new_p = cat_apply_freq(mappings["to_new"], freqs)\n\n# mappings for a specific category\nmappings["to_new"][\'3481\']\n# probability mappings for a specific category\nmapp_new_p[\'3481\']\n```\n\n### cat2cat function\n\n```python\nfrom cat2cat import cat2cat\nfrom cat2cat.dataclass import cat2cat_data, cat2cat_mappings, cat2cat_ml\n\nfrom pandas import concat\n\n# split the panel by the time variale\n# here only two periods\no_old = occup.loc[occup.year == 2008, :].copy()\no_new = occup.loc[occup.year == 2010, :].copy()\n\n# dataclasses, core arguments for the cat2cat function\ndata = cat2cat_data(\n    old = o_old, \n    new = o_new,\n    cat_var_old = "code", \n    cat_var_new = "code", \n    time_var = "year"\n)\nmappings = cat2cat_mappings(trans = trans, direction = "backward")\n\n# apply the cat2cat procedure\nc2c = cat2cat(data = data, mappings = mappings)\n# pandas.concat used to bind per period datasets\ndata_final = concat([c2c["old"], c2c["new"]])\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`cat2cat` was created by Maciej Nasinski. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`cat2cat` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Maciej Nasinski',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/polkas/py-cat2cat',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
