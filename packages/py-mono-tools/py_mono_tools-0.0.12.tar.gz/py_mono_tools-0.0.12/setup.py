# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py_mono_tools', 'py_mono_tools.backends', 'py_mono_tools.goals']

package_data = \
{'': ['*'],
 'py_mono_tools': ['.mypy_cache/*',
                   '.mypy_cache/3.10/*',
                   '.mypy_cache/3.10/_typeshed/*',
                   '.mypy_cache/3.10/click/*',
                   '.mypy_cache/3.10/collections/*',
                   '.mypy_cache/3.10/ctypes/*',
                   '.mypy_cache/3.10/email/*',
                   '.mypy_cache/3.10/importlib/*',
                   '.mypy_cache/3.10/importlib/metadata/*',
                   '.mypy_cache/3.10/importlib_metadata/*',
                   '.mypy_cache/3.10/logging/*',
                   '.mypy_cache/3.10/os/*',
                   '.mypy_cache/3.10/py_mono_tools/*',
                   '.mypy_cache/3.10/py_mono_tools/backends/*',
                   '.mypy_cache/3.10/py_mono_tools/goals/*',
                   '.mypy_cache/3.10/urllib/*',
                   '.pytest_cache/*',
                   '.pytest_cache/v/cache/*',
                   'templates/*',
                   'templates/dockerfiles/*']}

install_requires = \
['click>=8,<9', 'pydocstyle[toml]>=6.1.1,<7.0.0', 'pytest>=7.1.3,<8.0.0']

extras_require = \
{':extra == "linters_python"': ['bandit>=1.7.4,<2.0.0',
                                'black>=22.8.0,<23.0.0',
                                'flake8>=5.0.4,<6.0.0',
                                'isort>=5.10.1,<6.0.0',
                                'mypy>=0.971,<0.972',
                                'pydocstringformatter>=0.7.2,<0.8.0',
                                'pylint>=2.15.2,<3.0.0']}

entry_points = \
{'console_scripts': ['pmt = py_mono_tools.main:cli',
                     'py_mono_tools = py_mono_tools.main:cli']}

setup_kwargs = {
    'name': 'py-mono-tools',
    'version': '0.0.12',
    'description': 'A CLI designed to make it easier to work in a python mono repo',
    'long_description': 'For more information, please go the GitHub page. https://peterhoburg.github.io/py_mono_tools/\n',
    'author': 'Peter Hoburg',
    'author_email': 'peterHoburg@users.noreply.github.com',
    'maintainer': 'Peter Hoburg',
    'maintainer_email': 'peterHoburg@users.noreply.github.com',
    'url': 'https://peterhoburg.github.io/py_mono_tools/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
