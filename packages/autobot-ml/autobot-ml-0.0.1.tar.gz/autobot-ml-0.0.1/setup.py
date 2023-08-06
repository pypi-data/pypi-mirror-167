# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autobot', 'autobot.refactor', 'autobot.review', 'autobot.utils']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.5,<0.5.0',
 'openai>=0.23.0,<0.24.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['autobot = autobot.main:main']}

setup_kwargs = {
    'name': 'autobot-ml',
    'version': '0.0.1',
    'description': 'An automated code refactoring tool powered by GPT-3.',
    'long_description': '# autobot\n\nAn automated code refactoring tool powered by GPT-3. Like GitHub Copilot, for your existing\ncodebase.\n\n## Getting started\n\nFirst, add a `.env` file to the root directory, with a structure like this:\n\n```\nOPENAI_ORGANIZATION=${YOUR_OPENAI_ORGANIZATION}\nOPENAI_API_KEY=${YOUR_OPENAI_API_KEY}\n```\n\nThen, run `poetry install`.\n\n## Example usage\n\n### Removing useless object inheritance\n\n```shell\npython -m autobot useless_object_inheritance schematics/useless_object_inheritance/\n```\n\n### Removing print statements\n\n```shell\npython -m autobot print_statement schematics/print_statement/\n```\n\n### Rename `self.assertEquals` to `self.assertEqual`\n\n```shell\npython -m autobot assert_equals schematics/assert_equals/\n```\n\n### Remove unnecessary f-strings\n\n```shell\npython -m autobot unnecessary_f_strings schematics/unnecessary_f_strings/\n```\n\n### Migrating to standard library generics\n\n```shell\npython -m autobot standard_library_generics schematics/standard_library_generics/\n```\n\n## License\n\nMIT\n',
    'author': 'Charlie Marsh',
    'author_email': 'charlie.r.marsh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/charliermarsh/autobot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
