# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mcping']

package_data = \
{'': ['*']}

install_requires = \
['mcstatus>=9.3,<10.0', 'orjson>=3.7,<4.0']

entry_points = \
{'console_scripts': ['mcping = mcping.cli:main']}

setup_kwargs = {
    'name': 'mcping',
    'version': '0.2.0',
    'description': 'Get statuses from Minecraft servers',
    'long_description': "# mcping [![Build Badge]](https://gitlab.com/MysteryBlokHed/mcping/-/pipelines) [![Docs Badge]](https://mcping.readthedocs.io/en/latest/) [![License Badge]](#license)\n\nGet statuses from Minecraft servers.\n\n## Difference between this and mcstatus\n\nThis package uses some classes and functions from [mcstatus].\n\nUnlike mcstatus, this package will only attempt to handshake and get the status.\nIt doesn't do any DNS lookups or pings that aren't strictly required to get the status.\n\nThis package also doesn't convert the status response into a series of nested classes,\nwhich should make the results much easier to work with, especially when dealing with\nnon-standard status responses (eg. Forge mod lists).\n\nA side effect of this is that there isn't any guarantee that the status response\nwill have all of the keys that it should, meaning you'll need to do some validation\nbefore assuming that keys are present, or that they're the types you think.\n\n## Docs\n\nDocumentation is available at <https://mcping.readthedocs.io>.\n\n## Installation\n\nIf you want to use the library, install with `pip`:\n\n```sh\npip install mcping\n```\n\nIf you only want the CLI, `pipx` is recommended:\n\n```sh\npipx install mcping\n```\n\n## Use\n\n### Library\n\n```python\nimport mcping\n\n# Synchronous\nmcping.status('127.0.0.1')\n\n# Asynchronous\nasync def main():\n    await mcping.async_status('127.0.0.1')\n```\n\n### CLI\n\nThe package also includes a CLI to get server statuses.\nIt can be run from a cloned repo using the `cli.py` file:\n\n```sh\npython3 cli.py example.com\npython3 cli.py example.com:25565\n```\n\nIf the library is installed, the `mcping` script should also be installed and available globally:\n\n```sh\nmcping example.com\nmcping example.com:25565\n```\n\n## License\n\nThis project is licensed under either of\n\n- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or\n  <http://www.apache.org/licenses/LICENSE-2.0>)\n- MIT license ([LICENSE-MIT](LICENSE-MIT) or\n  <http://opensource.org/licenses/MIT>)\n\nat your option.\n\nSome code in `mcping/__init__.py` is modified from the [mcstatus] project's code,\nlicensed under the Apache License, Version 2.0.\n\n[build badge]: https://img.shields.io/gitlab/pipeline-status/MysteryBlokHed/mcping\n[docs badge]: https://img.shields.io/readthedocs/mcping\n[license badge]: https://img.shields.io/badge/license-MIT%20or%20Apache--2.0-green\n[mcstatus]: https://github.com/py-mine/mcstatus\n",
    'author': 'Adam Thompson-Sharpe',
    'author_email': 'adamthompsonsharpe@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/MysteryBlokHed/mcping',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
