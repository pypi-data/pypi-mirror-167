# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['libvcs', 'libvcs._internal', 'libvcs.cmd', 'libvcs.sync', 'libvcs.url']

package_data = \
{'': ['*']}

extras_require = \
{':python_version == "3.10"': ['typing-extensions>=4.1.1,<5.0.0']}

setup_kwargs = {
    'name': 'libvcs',
    'version': '0.15.0',
    'description': 'Lite, typed, python utilities for Git, SVN, Mercurial, etc.',
    'long_description': '# `libvcs` &middot; [![Python Package](https://img.shields.io/pypi/v/libvcs.svg)](https://pypi.org/project/libvcs/) [![License](https://img.shields.io/github/license/vcs-python/libvcs.svg)](https://github.com/vcs-python/libvcs/blob/master/LICENSE) [![Code Coverage](https://codecov.io/gh/vcs-python/libvcs/branch/master/graph/badge.svg)](https://codecov.io/gh/vcs-python/libvcs)\n\nlibvcs is a lite, [typed](https://docs.python.org/3/library/typing.html), pythonic tool box for\ndetection and parsing of URLs, commanding, and syncing with `git`, `hg`, and `svn`. Powers\n[vcspull](https://www.github.com/vcs-python/vcspull/).\n\n## Overview\n\nFeatures for Git, Subversion, and Mercurial:\n\n- **Detect and parse** VCS URLs\n- **Command** VCS via python API\n- **Sync** repos locally\n\nTo **get started**, see the [quickstart](https://libvcs.git-pull.com/quickstart.html) for more.\n\n```console\n$ pip install --user libvcs\n```\n\n## URL Parser\n\nYou can validate and parse Git, Mercurial, and Subversion URLs through\n[`libvcs.url`](https://libvcs.git-pull.com/url/index.html):\n\nValidate:\n\n```python\n>>> from libvcs.url.git import GitURL\n\n>>> GitURL.is_valid(url=\'https://github.com/vcs-python/libvcs.git\')\nTrue\n```\n\nParse and adjust a Git URL:\n\n```python\n>>> from libvcs.url.git import GitURL\n\n>>> git_location = GitURL(url=\'git@github.com:vcs-python/libvcs.git\')\n\n>>> git_location\nGitURL(url=git@github.com:vcs-python/libvcs.git,\n        user=git,\n        hostname=github.com,\n        path=vcs-python/libvcs,\n        suffix=.git,\n        matcher=core-git-scp)\n```\n\nSwitch repo libvcs -> vcspull:\n\n```python\n>>> from libvcs.url.git import GitURL\n\n>>> git_location = GitURL(url=\'git@github.com:vcs-python/libvcs.git\')\n\n>>> git_location.path = \'vcs-python/vcspull\'\n\n>>> git_location.to_url()\n\'git@github.com:vcs-python/vcspull.git\'\n\n# Switch them to gitlab:\n>>> git_location.hostname = \'gitlab.com\'\n\n# Export to a `git clone` compatible URL.\n>>> git_location.to_url()\n\'git@gitlab.com:vcs-python/vcspull.git\'\n```\n\nSee more in the [parser document](https://libvcs.git-pull.com/parse/index.html).\n\n## Commands\n\nSimple [`subprocess`](https://docs.python.org/3/library/subprocess.html) wrappers around `git(1)`,\n`hg(1)`, `svn(1)`. Here is [`Git`](https://libvcs.git-pull.com/cmd/git.html#libvcs.cmd.git.Git) w/\n[`Git.clone`](http://libvcs.git-pull.com/cmd/git.html#libvcs.cmd.git.Git.clone):\n\n```python\nimport pathlib\nfrom libvcs.cmd.git import Git\n\ngit = Git(dir=pathlib.Path.cwd() / \'my_git_repo\')\ngit.clone(url=\'https://github.com/vcs-python/libvcs.git\')\n```\n\n## Sync\n\nCreate a [`GitSync`](https://libvcs.git-pull.com/projects/git.html#libvcs.sync.git.GitProject)\nobject of the project to inspect / checkout / update:\n\n```python\nimport pathlib\nfrom libvcs.sync.git import GitSync\n\nrepo = GitSync(\n   url="https://github.com/vcs-python/libvcs",\n   dir=pathlib.Path().cwd() / "my_repo",\n   remotes={\n       \'gitlab\': \'https://gitlab.com/vcs-python/libvcs\'\n   }\n)\n\n# Update / clone repo:\n>>> repo.update_repo()\n\n# Get revision:\n>>> repo.get_revision()\nu\'5c227e6ab4aab44bf097da2e088b0ff947370ab8\'\n```\n\n## Donations\n\nYour donations fund development of new features, testing and support. Your money will go directly to\nmaintenance and development of the project. If you are an individual, feel free to give whatever\nfeels right for the value you get out of the project.\n\nSee donation options at <https://www.git-pull.com/support.html>.\n\n## More information\n\n- Python support: 3.9+, pypy\n- VCS supported: git(1), svn(1), hg(1)\n- Source: <https://github.com/vcs-python/libvcs>\n- Docs: <https://libvcs.git-pull.com>\n- Changelog: <https://libvcs.git-pull.com/history.html>\n- APIs for git, hg, and svn:\n  - [`libvcs.url`](https://libvcs.git-pull.com/url/): URL Parser\n  - [`libvcs.cmd`](https://libvcs.git-pull.com/cmd/): Commands\n  - [`libvcs.sync`](https://libvcs.git-pull.com/sync/): Clone and update\n- Issues: <https://github.com/vcs-python/libvcs/issues>\n- Test Coverage: <https://codecov.io/gh/vcs-python/libvcs>\n- pypi: <https://pypi.python.org/pypi/libvcs>\n- Open Hub: <https://www.openhub.net/p/libvcs>\n- License: [MIT](https://opensource.org/licenses/MIT).\n\n[![Docs](https://github.com/vcs-python/libvcs/workflows/docs/badge.svg)](https://libvcs.git-pull.com/)\n[![Build Status](https://github.com/vcs-python/libvcs/workflows/tests/badge.svg)](https://github.com/vcs-python/libvcs/actions?query=workflow%3A%22tests%22)\n',
    'author': 'Tony Narlock',
    'author_email': 'tony@git-pull.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/vcs-python/libvcs/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
