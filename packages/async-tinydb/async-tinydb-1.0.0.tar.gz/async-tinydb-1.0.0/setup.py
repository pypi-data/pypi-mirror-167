# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asynctinydb']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'nest-asyncio>=1.5.5,<2.0.0',
 'ujson>=5.4.0,<6.0.0']

extras_require = \
{':python_version <= "3.10"': ['typing-extensions>=3.10.0,<5.0.0']}

setup_kwargs = {
    'name': 'async-tinydb',
    'version': '1.0.0',
    'description': 'Yet Another Async TinyDB',
    'long_description': '![logo](https://raw.githubusercontent.com/msiemens/tinydb/master/artwork/logo.png)\n\n## What\'s This?\n\n"An asynchronous IO version of `TinyDB` based on `aiofiles`."\n\nAlmost every method is asynchronous. And it\'s based on `TinyDB 4.7.0+`.  \nI will try to keep up with the latest version of `TinyDB`.\n\nSince I modified it in just a few hours, I\'m not sure if it\'s stable enough for production.  \nBut hey! It passed all the tests anyways.\n\n## A few extra minor differences from the original `TinyDB`:\n\n* **lazy-load:** When access-mode is set to `\'r\'`, `FileNotExistsError` is not raised until the first read operation.\n* **ujson:** Using `ujson` instead of `json`. Some arguments aren\'t compatible with `json`\n\n## How to use IT?\n\n#### Installation\n\n```Bash\npip install async-tinydb\n```\n\n#### Importing\n```Python\nfrom asynctinydb import TinyDB, where\n```\n\n\nBasically, all you need to do is insert an `await` before every method that needs IO.\n\nNotice that some parts of the code are blocking, for example when calling `len()` on `TinyDB` or `Table` Objects.\n\n## Example Codes:\n\n```Python\nimport asyncio\nfrom asynctinydb import TinyDB, Query\n\nasync def main():\n    db = TinyDB(\'test.json\')\n    await db.insert({"answer": 42})\n    print(await db.search(Query().answer == 42))  # >>> [{\'answer\': 42}] \n\nasyncio.run(main())\n```\n',
    'author': 'Markus Siemens',
    'author_email': 'markus@m-siemens.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/VermiIIi0n/async-tinydb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
