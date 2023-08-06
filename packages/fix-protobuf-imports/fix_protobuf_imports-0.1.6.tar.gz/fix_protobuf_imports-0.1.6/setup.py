# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fix_protobuf_imports']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['fix-protobuf-imports = '
                     'fix_protobuf_imports.fix_protobuf_imports:main']}

setup_kwargs = {
    'name': 'fix-protobuf-imports',
    'version': '0.1.6',
    'description': 'A script to fix relative imports (from and to nested sub-directories) within compiled `*_pb2.py` Protobuf files.',
    'long_description': '# fix-protobuf-imports\n\nThis script will fix relative imports (from and to nested sub-directories) within compiled `*pb2.py` and `*pb2.pyi` Protobuf files/modules generated from `protoc --python_out --mypy_out`:\n\n```bash\nfix-protobuf-imports /path/to/python_out/dir\n```\n\n## When do I need to fix my imports?\n\nE.g. you might have the following file/module structure:\n\n- `./`\n  - `a_pb2.py`\n  - `b_pb2.py`\n  - `./sub/`\n    - `c_pb2.py`\n    - `./nested/`\n      - `d_pb2.py`\n      - `__init__.py`\n    - `__init__.py`\n  - `__init__.py`\n\nNow assume, `c.proto` is importing `a.proto`, `b.proto` and `d.proto`.\n\n`protoc` will generate the following import statements for `c_pb2.py`:\n\n```python\n# c_pb2.py\n\nfrom google.protobuf import descriptor as _descriptor\n\nimport a_pb2 as a__pb2\nimport b_pb2 as b__pb2\n\nfrom sub.nested import d_pb2 as sub_dot_nested__d__pb2\n\n# ...\n```\n\nUsing these modules will not work under Python 3, as the imports are not relative. As it can get quite cumbersome to fix these issues, this script will convert the imports automatically:\n\n```bash\nfix-protobuf-imports /path/to/python_out/dir\n```\n\nThis will result in the following working imports:\n\n```python\n# c_pb2.py\n\nfrom google.protobuf import descriptor as _descriptor\n\nfrom .. import a_pb2 as a__pb2\nfrom .. import b_pb2 as b__pb2\n\nfrom ..sub.nested import d_pb2 as sub_dot_nested__d__pb2\n\n# ...\n```\n\n## Development\nThis project uses the Python project managment tool `poetry`.\n\n1. Install Poetry\n  ```sh\n    curl -sSL https://install.python-poetry.org | python3 - --preview\n  ```\n2. Install dependencies\n  ```sh\n    poetry install\n  ```\n3. Test script\n  ```sh\n    poetry run fix-protobuf-imports --help\n  ```\n',
    'author': 'Markus Wegmann',
    'author_email': 'mw@technokrat.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
