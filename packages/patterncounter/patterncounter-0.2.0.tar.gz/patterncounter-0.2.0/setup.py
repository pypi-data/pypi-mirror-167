# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['patterncounter']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1']

entry_points = \
{'console_scripts': ['patterncounter = patterncounter.__main__:main']}

setup_kwargs = {
    'name': 'patterncounter',
    'version': '0.2.0',
    'description': 'PatternCounter',
    'long_description': '# PatternCounter\n\n[![PyPI](https://img.shields.io/pypi/v/patterncounter.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/patterncounter.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/patterncounter)][python version]\n[![License](https://img.shields.io/pypi/l/patterncounter)][license]\n\n[![Read the documentation at https://patterncounter.readthedocs.io/](https://img.shields.io/readthedocs/patterncounter/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/JoaoFelipe/patterncounter/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/JoaoFelipe/patterncounter/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/patterncounter/\n[status]: https://pypi.org/project/patterncounter/\n[python version]: https://pypi.org/project/patterncounter\n[read the docs]: https://patterncounter.readthedocs.io/\n[tests]: https://github.com/JoaoFelipe/patterncounter/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/JoaoFelipe/patterncounter\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\nThis tool allows to count patterns in lists of sequential groups using [rules](rules.md) and [variables](variables.md).\n\nFor the following examples, consider the following file (`sequences.txt`):\n\n```\nA -1 -2\nB -1 -2\nA B -1 -2\nA -1 B C -1 -2\nB -1 A B -1 A -1 C -1 -2\n```\n\nExample 1: Count how many sequences contain both the elements A and B:\n\n```bash\n$ patterncounter count "A B" -n -f sequences.txt\nSupp((A B)) = 0.6 | 3 lines: 2, 3, 4\n```\n\nExample 2: Count how many sequences contain elements A and B at the same group:\n\n```bash\n$ patterncounter count "A & B" -n -f sequences.txt\nSupp(A & B) = 0.4 | 2 lines: 2, 4\n```\n\nExample 3: Count how many sequences have an element B that after after A:\n\n```bash\n$ patterncounter count "A -> B" -n -f sequences.txt\nSupp(A -> B) = 0.2 | 1 lines: 3\n```\n\nExample 4: Count in how many sequences the element B was removed within an interval of A:\n\n```bash\n$ patterncounter count "[A OutB]" -n -f sequences.txt\nSupp([A OutB]) = 0.2 | 1 lines: 4\n```\n\nExample 5: Count in how many sequences there is an element C that occurs after an interval of A:\n\n```bash\n$ patterncounter count "[A] -> C" -n -f sequences.txt\nSupp([A] -> C) = 0.4 | 2 lines: 3, 4\n```\n\nExample 6: Show results even when the pattern does not exist:\n\n```bash\n$ patterncounter count "Z" -n -f sequences.txt -z\nSupp(Z) = 0.0 | 0 lines\n```\n\nIn addition to using simple rules, it is possible to define multiple rules and calculated association rules metrics among them:\n\nExample 7: Count both how many sequences have an interval of A, and how many sequences have an interval of A with an element B inside:\n\n```bash\n$ patterncounter count "[A]" "[A B]" -n -f sequences.txt\nSupp([A], [A B]) = 0.4 | 2 lines: 2, 4\nAssociation Rule: [A] ==> [A B]\n  Supp([A]) = 0.8 | 4 lines: 0, 2, 3, 4\n  Supp([A B]) = 0.4 | 2 lines: 2, 4\n  Conf = 0.5\n  Lift = 1.25\nAssociation Rule: [A B] ==> [A]\n  Supp([A B]) = 0.4 | 2 lines: 2, 4\n  Supp([A]) = 0.8 | 4 lines: 0, 2, 3, 4\n  Conf = 1.0\n  Lift = 1.25\n```\n\nIt is also possible to define variables.\n\nExample 8: Count how many sequences have groups with two distinct elements:\n\n```bash\n$ patterncounter count "x & y" -v "x" -v "y" -n -f sequences.txt -z\nSupp(x & y) = 0.6 | 3 lines: 2, 3, 4\n\n[BINDING: x = B; y = A]\n  Supp(B & A) = 0.4 | 2 lines: 2, 4\n\n[BINDING: x = A; y = B]\n  Supp(A & B) = 0.4 | 2 lines: 2, 4\n\n[BINDING: x = B; y = C]\n  Supp(B & C) = 0.2 | 1 lines: 3\n\n[BINDING: x = A; y = C]\n  Supp(A & C) = 0.0 | 0 lines\n\n[BINDING: x = C; y = B]\n  Supp(C & B) = 0.2 | 1 lines: 3\n\n[BINDING: x = C; y = A]\n  Supp(C & A) = 0.0 | 0 lines\n```\n\nNote that the result first shows the combined metrics (union).\n\nFinally, given a file of sequences, it is also possible to select its lines (0-indexes):\n\n```bash\n$ patterncounter select -f sequences.txt -n 4\n0| A -1 -2\n2| A B -1 -2\n4| B -1 A B -1 A -1 C -1 -2\n```\n\n## Installation\n\nYou can install _PatternCounter_ via [pip] from [PyPI]:\n\n```console\n$ pip install patterncounter\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_PatternCounter_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/JoaoFelipe/patterncounter/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/JoaoFelipe/patterncounter/blob/main/LICENSE\n[contributor guide]: https://github.com/JoaoFelipe/patterncounter/blob/main/CONTRIBUTING.md\n[command-line reference]: https://patterncounter.readthedocs.io/en/latest/usage.html\n',
    'author': 'Joao Felipe Pimentel',
    'author_email': 'joaofelipenp@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JoaoFelipe/patterncounter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
