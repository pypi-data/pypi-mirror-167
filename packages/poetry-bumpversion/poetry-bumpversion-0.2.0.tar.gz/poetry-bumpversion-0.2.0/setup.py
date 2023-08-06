# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_bumpversion']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0a1,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['poetry_bumpversion = '
                               'poetry_bumpversion.plugin:BumpVersionPlugin']}

setup_kwargs = {
    'name': 'poetry-bumpversion',
    'version': '0.2.0',
    'description': 'Poetry plugin to update project version strings on poetry version command',
    'long_description': '####################\npoetry-bumpversion\n####################\n\nThe ``poetry version`` command only updates version in ``pyproject.toml`` file.\nThis plugin updates version in other files when ``poetry version <version>``\ncommand is executed.\n\n|  |build-status| |pyversions| |pypi-version| |license|\n\n********************\nGetting Started\n********************\n\n++++++++++++++++++++\nPrerequisites\n++++++++++++++++++++\n\n- poetry = ^1.2.0a1\n\n++++++++++++++++++++\nInstall\n++++++++++++++++++++\n\nInstall the plugin by poetry plugin command.\n\n::\n\n    poetry self add poetry-bumpversion\n\n++++++++++++++++++++++++++++++\nConfigure version replacements\n++++++++++++++++++++++++++++++\n\nSay you have ``__version__`` variable set at ``your_package/__init__.py`` file\n\n.. code:: python\n\n    __version__ = "0.1.0" # It MUST match the version in pyproject.toml file\n\n\nAdd the following to your ``pyproject.toml`` file.\n\n.. code:: toml\n\n    [tool.poetry_bumpversion.file."your_package/__init__.py"]\n\nNow run ``poetry version patch`` to check if version in both ``pyproject.toml`` and\n``your_package/__init__.py`` file has been updated.\n\nYou can add more files following the steps above. You can also fine define\nsearch and replace terms to be more precise\n\n.. code:: toml\n\n    [tool.poetry_bumpversion.file."your_package/__init__.py"]\n    search = \'__version__ = "{current_version}"\'\n    replace = \'__version__ = "{new_version}"\'\n\nYou can also define replacements if you have same search/replace patterns across multiple files.\n\n.. code:: toml\n\n    [[tool.poetry_bumpversion.replacements]]\n    files = ["your_package/__init__.py", "your_package/version.py"]\n    search = \'__version__ = "{current_version}"\'\n    replace = \'__version__ = "{new_version}"\'\n\n    [[tool.poetry_bumpversion.replacements]]\n    files = ["README.md"]\n    search = \'version: {current_version}\'\n    replace = \'version: {new_version}\'\n\n\n********************\nLicense\n********************\n\nThis project is licensed under MIT License - see the\n`LICENSE <https://github.com/monim67/poetry-bumpversion/blob/master/LICENSE>`_ file for details.\n\n\n.. |build-status| image:: https://github.com/monim67/poetry-bumpversion/actions/workflows/build.yml/badge.svg?event=push\n    :target: https://github.com/monim67/poetry-bumpversion/actions/workflows/build.yml\n    :alt: Build Status\n    :height: 20px\n\n.. |pyversions| image:: https://img.shields.io/pypi/pyversions/poetry-bumpversion.svg\n    :target: https://pypi.python.org/pypi/poetry-bumpversion\n    :alt: Python Versions\n    :height: 20px\n\n.. |pypi-version| image:: https://badge.fury.io/py/poetry-bumpversion.svg\n    :target: https://pypi.python.org/pypi/poetry-bumpversion\n    :alt: PyPI version\n    :height: 20px\n\n.. |license| image:: https://img.shields.io/pypi/l/poetry-bumpversion.svg\n    :target: https://pypi.python.org/pypi/poetry-bumpversion\n    :alt: Licence\n    :height: 20px\n',
    'author': 'Munim Munna',
    'author_email': '6266677+monim67@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/monim67/poetry-bumpversion',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
