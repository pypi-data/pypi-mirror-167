# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gtkspellcheck', 'gtkspellcheck._pylocales']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.1,<4.0.0', 'pyenchant>=3.0,<4.0']

extras_require = \
{'docs': ['sphinx>=4.5.0,<5.0.0', 'myst-parser>=0.18.0,<0.19.0']}

setup_kwargs = {
    'name': 'pygtkspellcheck',
    'version': '5.0.1',
    'description': 'A simple but quite powerful spellchecking library for GTK written in pure Python.',
    'long_description': '# Python GTK Spellcheck\n\n[![PyPi Project Page](https://img.shields.io/pypi/v/pygtkspellcheck.svg?&label=latest%20version)](https://pypi.python.org/pypi/pygtkspellcheck)\n[![Documentation](https://readthedocs.org/projects/pygtkspellcheck/badge/?version=latest)](https://pygtkspellcheck.readthedocs.org/en/latest/)\n\nPython GTK Spellcheck is a simple but quite powerful spellchecking library for GTK written in pure Python. It\'s spellchecking component is based on [Enchant](http://www.abisource.com/projects/enchant/) and it supports both GTK 3 and 4 via [PyGObject](https://live.gnome.org/PyGObject/).\n\n**⚡️ News:** Thanks to [@cheywood](https://github.com/cheywood), Python GTK Spellcheck now supports GTK 4! 🎉\n\n**🟢 Status:** This project is mature, actively maintained, and open to contributions and co-maintainership.\n\n\n## ✨ Features\n\n- **spellchecking** based on [Enchant](http://www.abisource.com/projects/enchant/) for `GtkTextView`\n- support for word, line, and multiline **ignore regular expressions**\n- support for both **GTK 3 and 4** via [PyGObject](https://live.gnome.org/PyGObject/) for Python 3\n- configurable extra word characters such as `\'`\n- localized names of the available languages based on [ISO-Codes](http://pkg-isocodes.alioth.debian.org/)\n- support for custom ignore tags and hot swap of `GtkTextBuffer`\n- support for Hunspell (LibreOffice) and Aspell (GNU) dictionaries\n\n<p align="center">\n  <img src="https://raw.githubusercontent.com/koehlma/pygtkspellcheck/master/docs/screenshots/screenshot.png" alt="Screenshot" />\n</p>\n\n\n## 🚀 Getting Started\n\nPython GTK Spellcheck is available from the [Python Package Index](https://pypi.python.org/pypi/pygtkspellcheck):\n```sh\npip install pygtkspellcheck\n```\nDepending on your distribution, you may also find Python GTK Spellcheck in your package manager.\nFor instance, on Debian you may want to install the [`python3-gtkspellcheck`](https://packages.debian.org/bullseye/python3-gtkspellcheck) package.\n\n\n## 🥳 Showcase\n\nOver time, several projects have used Python GTK Spellcheck or are still using it. Among those are:\n\n- [Nested Editor](http://nestededitor.sourceforge.net/about.html): “Specialized editor for structured documents.”\n- [Cherry Tree](http://www.giuspen.com/cherrytree/): “A hierarchical note taking application, […].”\n- [Zim](http://zim-wiki.org/): “Zim is a graphical text editor used to maintain a collection of wiki pages.”\n- [REMARKABLE](http://remarkableapp.github.io/): “The best markdown editor for Linux and Windows.”\n- [RedNotebook](http://rednotebook.sourceforge.net/): “RedNotebook is a modern journal.”\n- [Reportbug](https://packages.debian.org/stretch/reportbug): “Reports bugs in the Debian distribution.”\n- [UberWriter](http://uberwriter.wolfvollprecht.de/): “UberWriter is a writing application for markdown.”\n- [Gourmet](https://github.com/thinkle/gourmet): “Gourmet Recipe Manager is a manager, editor, and organizer for recipes.“\n\n\n## 🔖 Versions\n\nVersion numbers follow [Semantic Versioning](http://semver.org/). However, the update from 3 to 4 pertains only API incompatible changes in `oxt_extract` and not the spellchecking component. The update from 4 to 5 removed support for Python 2, GTK 2, `pylocales`, and the `oxt_extract` API. Otherwise, the API is still compatible with version 3.\n\n\n## 📚 Documentation\n\nThe documentation is available at [Read the Docs](http://pygtkspellcheck.readthedocs.org/).\n\n\n## 🏗 Contributing\n\nWe welcome all kinds of contributions! ❤️\n\nFor minor changes and bug fixes feel free to simply open a pull request. For major changes impacting the overall design of Python GTK Spellcheck, please first [start a discussion](https://github.com/koehlma/pygtkspellcheck/discussions/new?category=ideas) outlining your idea.\n\nBy submitting a PR, you agree to license your contributions under “GPLv3 or later”.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mail@koehlma.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/koehlma/pygtkspellcheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
