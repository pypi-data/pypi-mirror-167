# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['p3orm', 'p3orm.drivers']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.8,<0.49.0', 'pydantic>=1.8.2,<2.0.0']

extras_require = \
{'postgres': ['asyncpg>=0.26.0,<0.27.0'],
 'sqlite': ['aiosqlite>=0.17.0,<0.18.0']}

setup_kwargs = {
    'name': 'p3orm',
    'version': '0.6.1',
    'description': 'Utilitarian Python ORM for Postgres/SQLite, backed by asyncpg/aiosqlite, Pydantic, and PyPika',
    'long_description': '# p3orm\n\n<a href="https://rafalstapinski.github.io/p3orm">\n  <img src="https://rafalstapinski.github.io/p3orm/img/logo.svg" alt="p3orm logo" />\n</a>\n\n<p align="center">\n  <strong>\n    <em>\n      Utilitarian Python ORM for Postgres/SQLite powered by <a href="https://github.com/MagicStack/asyncpg">asyncpg</a>/<a href="https://github.com/omnilib/aiosqlite">aiosqlite</a>, <a href="https://github.com/samuelcolvin/pydantic">Pydantic</a>, and <a href="https://github.com/kayak/pypika">PyPika</a>\n    </em>\n  </strong>\n</p>\n\n---\n\n**Documentation**: <a href="https://rafalstapinski.github.io/p3orm">https://rafalstapinski.github.io/p3orm</a>\n\n**Source Code**: <a href="https://github.com/rafalstapinski/p3orm">https://github.com/rafalstapinski/p3orm</a>\n\n---\n\n<p align="center">\n  <a href="https://github.com/rafalstapinski/p3orm/actions/workflows/test.yml" target="_blank">\n    <img src="https://github.com/rafalstapinski/p3orm/actions/workflows/test.yml/badge.svg" alt="Test Status" />\n  </a>\n  <a href="https://pypi.org/project/p3orm" target="_blank">\n    <img src="https://img.shields.io/pypi/v/p3orm?color=%2334D058" alt="pypi" />\n  </a>\n  <a href="https://pypi.org/project/p3orm" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/p3orm?color=%23334D058" alt="Supported Python Versions: 3.8, 3.9, 3.10" />\n  </a>\n  <a href="https://github.com/rafalstapinski/p3orm/blob/master/LICENSE" target="_blank">\n    <img src="https://img.shields.io/pypi/l/p3orm?color=%23334D058" alt="MIT License" />\n  </a>\n</p>\n\n---\n<h2>Philosophy</h2>\n\n90% of the time we talk to a database is with a CRUD operation. p3orm provides convenience helpers for fetching (one, first, many), inserting (one, many), updating (one), and deleting (one, many).\n\nThe remaining 10% is a bit more complicated. p3orm doesn\'t attempt to hide SQL queries or database interactions behind any magic. Instead, it empowers you to write direct and legible SQL queries with [PyPika](https://github.com/kayak/pypika) and execute them explicitly against the database.\n\nNotably, objects created or fetched by p3orm are dead, they\'re just [Pydantic](https://github.com/samuelcolvin/pydantic) models. If you want to interact with the database, you do so explicitly.\n\n### tl;dr - p3orm makes easy things easy, and hard things possible\n\n---\n<h2>Features</h2>\n\n- Comprehensive type annotations (full intellisense support)\n- String type validation an parsing powered by `Pydantic`\n- Support for `PyPika` queries\n- Support for all `postgres` [datatypes](https://magicstack.github.io/asyncpg/current/usage.html#type-conversion)\n- Support for all `sqlite` [datatypes](https://www.sqlite.org/datatype3.html)\n\n---\n<h2>Installation</h2>\n\nInstall with `poetry`\n```sh\npoetry add p3orm[sqlite]\n# or\npoetry add p3orm[postgres]\n```\n\nor with `pip`\n\n```sh\npip install p3orm[sqlite]\n# or\npip install p3orm[postgres]\n```\n\nThe `[sqlite]` extra installs `aiosqlite` as p3orm\'s database driver, whereas `[postgres]` installs `asyncpg`.\n\n---\n<h2>Basic Usage</h2>\n\n```python\nfrom datetime import datetime\nfrom p3orm import Column, Table\n\nfrom p3orm import sqlite as db\n# or: from p3orm import postgres as db\n\nclass Thing(Table):\n    id = Column(int, pk=True, autogen=True)\n    name = Column(str)\n    created_at = Column(datetime, autogen=True)\n\nawait db().connect(":memory:")\n\nthing = Thing(name="Name")\n\ninserted = await Thing.insert_one(thing)\n\nfetched = await Thing.fetch_first(Thing.id == 1)\n\nfetched.name = "Changed"\n\nupdated = await Thing.update_one(fetched)\n\ndeleted = await Thing.delete_where(Thing.id == updated.id)\n\nawait db().disconnect()\n```\n',
    'author': 'Rafal Stapinski',
    'author_email': 'stapinskirafal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rafalstapinski.github.io/p3orm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
