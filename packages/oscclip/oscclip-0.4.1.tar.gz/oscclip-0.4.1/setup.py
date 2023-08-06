# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oscclip']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['osc-copy = oscclip:osc_copy',
                     'osc-paste = oscclip:osc_paste']}

setup_kwargs = {
    'name': 'oscclip',
    'version': '0.4.1',
    'description': 'Utilities to access the clipboard via OSC52',
    'long_description': '# oscclip\n\n`oscclip` is a little, zero dependency python utility which utilizes the system clipboard via OSC52 escape sequences.\nUsing these sequences, the system clipboard is accessible via SSH as well.\nTerminal multiplexers, such as `tmux` and `screen` are supported.\n\n## Examples\n\n**Setting the clipboard**\n\n```\n$ echo "Foo" | osc-copy\n```\n\n**Setting the clipboard and bypass terminal multiplexers**\n\n```\n$ echo "Foo" | osc-copy --bypass\n```\n\n**Reading the clipboard**\n\n```\n$ osc-paste\nFoo\n```\n\n## Tested Terminals\n\n* [alacritty](https://github.com/alacritty/alacritty)\n* [foot](https://codeberg.org/dnkl/foot)\n\nFor a list of terminals that support OSC52, see [this table](https://github.com/ojroques/vim-oscyank#vim-oscyank).\n\n## Caveats\n\n### tmux\n\nThere is a [bug](https://github.com/tmux/tmux/pull/2942) in `tmux` \nDue to this `osc-paste` does not work with `tmux < 3.3` running in `foot`.\n\nIn order to make `--bypass` work, `allow-passthrough` must be enabled.\nCheck the manpage of `tmux`.\n`osc-copy` issues a warning to `stderr` when this option is not set and `--bypass` is present.\n\n## Installation\n\n**Arch Linux**\n\n```\n$ paru -S oscclip\n```\n\n**Run via poetry**\n\nCheck if your distribution provides [`poetry`](https://python-poetry.org) via its package management system!\nIt might be called `python-poetry`, `python3-poetry` or similar!\n\nOtherwise: https://python-poetry.org/docs/#installation\n\n```\n$ poetry install [--no-dev]\n$ poetry run ocs-copy\n```\n\n`--no-dev` omits the development dependencies, such as static code checkers.\n',
    'author': 'Stefan Tatschner',
    'author_email': 'stefan@rumpelsepp.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rumpelsepp/oscclip',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
