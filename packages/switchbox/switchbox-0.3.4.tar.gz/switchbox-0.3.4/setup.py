# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['switchbox', 'switchbox.ext', 'switchbox.tests']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'PyGithub>=1.55,<2.0',
 'click>=8.1.3,<9.0.0',
 'giturl>=0.1.3,<0.2.0',
 'inflect>=6.0.0,<7.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['git-switchbox = switchbox.cli:main',
                     'switchbox = switchbox.cli:main']}

setup_kwargs = {
    'name': 'switchbox',
    'version': '0.3.4',
    'description': 'Tools for working with Git repositories.',
    'long_description': "switchbox\n=========\n\nA collection of small tools for git workflows.\n\nInstallation\n------------\n\nClone the repository and install the package with `pip`.\n\n```zsh\npip install --user .\n```\n\nUsage\n-----\n\nInvoke `switchbox` directly or run it via `git switchbox`.\n\nSwitchbox commands assume your git repository has a default branch and a\ndefault remote. When Switchbox is used for the first time (or you run\n`switchbox setup`) it will find and remember names for these.\n\n* The default branch will use a branch named `main` or `master`.\n* The default remote will use a remote named `upstream` or `origin`.\n\nSwitchbox options are set in a repository's `.git/config` file under a\n`switchbox` section.\n\n### `switchbox config`\n\nShow config options that Switchbox has set.\n\n### `switchbox config init`\n\nDetect a default branch and default remote, and save them to the repository's\ngit configuration. This will be done automatically when you first use a command\nthat works on a default branch or default remote.\n\n### `switchbox config default-branch $branch`\n\nChange the default branch.\n\n### `switchbox config default-remote $remote`\n\nChange the default remote.\n\n### `switchbox finish [--update/--no-update]`\n\n* Update all git remotes.\n* Update the local default branch to match the remote default branch.\n* Switch to the default branch.\n* Remove branches **merged** into the default branch.\n* Remove branches **squashed** into the default branch.\n\n### `switchbox tidy [--update/--no-update]`\n\n* Update all git remotes.\n* Remove branches **merged** into the default branch.\n* Remove branches **squashed** into the default branch.\n\n### `switchbox update`\n\n* Update all git remotes.\n",
    'author': 'Sam Clements',
    'author_email': 'sam@borntyping.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/switchbox/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
