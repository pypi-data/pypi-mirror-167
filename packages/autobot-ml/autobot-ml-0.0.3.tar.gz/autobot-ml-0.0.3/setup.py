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
    'version': '0.0.3',
    'description': 'An automated code refactoring tool powered by GPT-3.',
    'long_description': '# autobot\n\nAn automated code refactoring tool powered by GPT-3. Like GitHub Copilot, for your existing\ncodebase.\n\nAutobot takes an example change as input and generates patches for you to review by scanning your\ncodebase for similar code blocks and "applying" that change to the existing source code.\n\n## Getting started\n\nAutobot is available as [`autobot-ml`](https://pypi.org/project/autobot-ml/) on PyPI:\n\n```shell\npip install autobot-ml\n```\n\nAutobot depends on the [OpenAI API](https://openai.com/api/) and, in particular, expects your OpenAI\norganization ID and API key to be exposed as the `OPENAI_ORGANIZATION` and `OPENAI_API_KEY`\nenvironment variables, respectively.\n\nAutobot can also read from a `.env` file:\n\n```\nOPENAI_ORGANIZATION=${YOUR_OPENAI_ORGANIZATION}\nOPENAI_API_KEY=${YOUR_OPENAI_API_KEY}\n```\n\n## Example usage\n\n_TL;DR: Autobot is a command-line tool. To generate patches, use `autobot run`; to review the\ngenerated patches, use `autobot review`._\n\nAutobot is designed around a two-step workflow.\n\nIn the first step (`autobot run {schematic} {files_to_analyze}`), we point Autobot to (1) the\n"schematic" that defines our desired change and (2) the files to which the change should be\napplied.\n\nIn the second step (`autobot review`), we review the patches that Autobot generated and,\nfor each suggested change, either apply it to the codebase or reject it.\n\nFor example: to remove any usages of NumPy\'s deprecated `np.int` and associated aliases, we\'d first\nrun `autobot run ./schematics/numpy_builtin_aliases ./path/to/main.py`, followed by\n`autobot review`.\n\n### Implementing a novel refactor\n\nEvery refactor facilitated by Autobot requires a "schematic". Autobot ships with a few example\nschematics in the `schematics` directory, but it\'s intended to be used with user-provided\nschematics.\n\nA schematic is a directory containing three files:\n\n1. `before.py`: A code snippet demonstrating the "before" state of the refactor.\n2. `after.py`: A code snippet demonstrating the "after" state of the refactor.\n3. `autobot.json`: A JSON object containing a plaintext description of the\n   before (`before_description`) and after (`after_description`) states, along with\n   the `transform_type` ("Function" or "Class").\n\nFor example: in Python 3, `class Foo(object)` is equivalent to `class Foo`. To automatically remove\nthose useless object inheritances from our codebase, we\'d create a `useless_object_inheritance`\ndirectory, and add the above files.\n\n```python\n# before.py\nclass Foo(Bar, object):\n    def __init__(self, x: int) -> None:\n        self.x = x\n```\n\n```python\n# after.py\nclass Foo(Bar):\n    def __init__(self, x: int) -> None:\n        self.x = x\n```\n\n```json\n// autobot.json\n{\n    "before_description": "with object inheritance",\n    "after_description": "without object inheritance",\n    "transform_type": "Class"\n}\n```\n\nWe\'d then run `autobot run useless_object_inheritance /path/to/file/or/directory` to generate\npatches, followed by `autobot review` to apply or reject the suggested changes.\n\n## Limitations\n\n1. To speed up execution, Autobot calls out to the OpenAI API in parallel. If you haven\'t upgraded\n   to a paid account, you may hit rate-limit errors. You can pass `--nthreads 1` to `autobot run`\n   to disable multi-threading.\n2. Depending on the transform type, Autobot will either generate a patch for every function or every\n   class. Any function or class that\'s "too long" will be GPT-3\'s maximum prompt size,\n\n## License\n\nMIT\n',
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
