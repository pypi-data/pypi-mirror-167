# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snakypy',
 'snakypy.dotctrl',
 'snakypy.dotctrl.actions',
 'snakypy.dotctrl.config',
 'snakypy.dotctrl.utils']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0',
 'snakypy-helpers>=0.3.1,<0.4.0',
 'tomlkit>=0.11.1,<0.12.0']

entry_points = \
{'console_scripts': ['dotctrl = snakypy.dotctrl.dotctrl:main']}

setup_kwargs = {
    'name': 'dotctrl',
    'version': '2.0.0',
    'description': 'Dotctrl is a package for managing your dotfiles on Linux.',
    'long_description': '.. image:: https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/images/dotctrl-transparent.png\n    :width: 441 px\n    :align: center\n    :alt: Dotctrl\n\n_________________\n\n.. image:: https://github.com/snakypy/dotctrl/workflows/Tests/badge.svg\n    :target: https://github.com/snakypy/dotctrl\n    :alt: Tests\n\n.. image:: https://img.shields.io/pypi/v/dotctrl.svg\n    :target: https://pypi.python.org/pypi/dotctrl\n    :alt: PyPI - Dotctrl\n\n.. image:: https://img.shields.io/pypi/wheel/dotctrl\n    :target: https://pypi.org/project/wheel/\n    :alt: PyPI - Wheel\n\n.. image:: https://img.shields.io/pypi/pyversions/dotctrl\n    :target: https://pyup.io/repos/github/snakypy/dotctrl/\n    :alt: Python versions\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    :alt: Black\n\n.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336\n    :target: https://pycqa.github.io/isort/\n    :alt: Isort\n\n.. image:: http://www.mypy-lang.org/static/mypy_badge.svg\n    :target: http://mypy-lang.org/\n    :alt: Mypy\n\n.. image:: https://pyup.io/repos/github/snakypy/dotctrl/shield.svg\n   :target: https://pyup.io/repos/github/snakypy/dotctrl/\n   :alt: Updates\n\n.. image:: https://img.shields.io/github/issues-raw/snakypy/dotctrl\n   :target: https://github.com/snakypy/dotctrl/issues\n   :alt: GitHub issues\n\n.. image:: https://img.shields.io/github/license/snakypy/dotctrl\n    :alt: GitHub license\n    :target: https://github.com/snakypy/dotctrl/blob/master/LICENSE\n\n_________________\n\nInitially, `Dotctrl` was created just to control "dotfiles files", however, in the course, it became more than that.\n`Dotctrl` is now a maintainer of any file and folder type within its own private repository.\n\nThis is too much!\n\n`Dotctrl` will manage the elements of the user\'s HOME directory; running on top of a configuration file (`dotctrl.json`) that contains the paths to the origin location of the elements.\n\nAll elements managed by `Dotctrl` are kept in the repository/folder "`dotctrl`".\n\nFeatures\n--------\n\n* Language support: American English and Brazilian Portuguese;\n* Create (or not) multiple repositories for your elements;\n* Abandon the creation of huge manual symlinks;\n* O armazenará a mesma estrutura de caminho que seu local (`$HOME`) original;\n* Manage single or bulk elements;\n* Restore repository elements to their original location with a single command;\n* And much more :)\n\nRequirements\n------------\n\nTo work correctly, you will first need:\n\n* Linux or macOS.\n* `python`_ (v3.9 or recent) must be installed.\n* `pip`_ (v19.3 or recent) must be installed.\n* `git`_ (v2.0 or recent) must be installed.\n\nInstalling\n----------\n\n.. code-block:: shell\n\n    $ python3 -m pip install dotctrl --user\n\n\nUsing\n-----\n\nTo know the commands of `Dotctrl`, run the command:\n\n.. code-block:: shell\n\n    $ dotctrl -h\n\nAlso visit the Dotctrl `home page`_ and see more about settings and usability.\n\nLinks\n-----\n\n* Code: https://github.com/snakypy/dotctrl\n* Documentation: https://github.com/snakypy/dotctrl/blob/main/README.md\n* Releases: https://pypi.org/project/dotctrl/#history\n* Issue tracker: https://github.com/snakypy/dotctrl/issues\n\nDonation\n--------\n\nClick on the image below to be redirected the donation forms:\n\n.. image:: https://raw.githubusercontent.com/snakypy/donations/main/svg/donate/donate-hand.svg\n    :width: 160 px\n    :height: 100px\n    :target: https://github.com/snakypy/donations/blob/main/README.md\n\nLicense\n-------\n\nThe gem is available as open source under the terms of the `MIT License`_ ©\n\nCredits\n-------\n\nSee, `AUTHORS`_.\n\n.. _`AUTHORS`: https://github.com/snakypy/dotctrl/blob/main/AUTHORS.rst\n.. _`home page`: https://github.com/snakypy/dotctrl\n.. _`python`: https://python.org\n.. _pip: https://pip.pypa.io/en/stable/quickstart/\n.. _git: https://git-scm.com/downloads\n.. _MIT License: https://github.com/snakypy/dotctrl/blob/main/LICENSE\n.. _William Canin: http://williamcanin.github.io\n',
    'author': 'William C. Canin',
    'author_email': 'william.costa.canin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/snakypy/dotctrl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
