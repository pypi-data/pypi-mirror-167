# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysurreal', 'pysurreal.connector', 'pysurreal.orm']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'pysurreal',
    'version': '1.0.0a0',
    'description': 'Community-created Python connector and ORM for SurrealDB.',
    'long_description': '# pysurreal\n\nCommunity-created Python connector and ORM for SurrealDB.\n\n## Installation\n\nRaw Python:\n\n```bash\npython3 -m pip install pysurreal\n```\n\nPoetry:\n\n```bash\npoetry add pysurreal\n```\n\n## Basic Usage\n\n```py\nfrom asyncio import run\n\nfrom pysurreal import Client\n\n\nasync def main() -> None:\n    async with Client("http://localhost:8000", "namespace", "database", "root", "root") as client:\n        result = await client.raw_query("""\n            CREATE example:123 SET\n                name = \'example\',\n                list = [\'a\', \'b\', \'c\']\n            ;\n        """)\n\n        if result.error is not None:\n            print(result.error.information)\n            return\n\n        print(result.response)\n\n\nrun(main())\n```\n\n## License\n\nThis project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.\n\n## Contributing\n\nThank you for your interest in contributing to pysurreal! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more information about contributing.\n',
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vcokltfre/pysurreal',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
