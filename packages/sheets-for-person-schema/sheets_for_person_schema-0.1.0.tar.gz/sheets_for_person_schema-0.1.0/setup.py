# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sheets_for_person_schema', 'sheets_for_person_schema.datamodel']

package_data = \
{'': ['*'], 'sheets_for_person_schema': ['schema/*']}

install_requires = \
['linkml-runtime>=1.1.24,<2.0.0']

setup_kwargs = {
    'name': 'sheets-for-person-schema',
    'version': '0.1.0',
    'description': 'Files for schemasheets exercises at ICBO 2022',
    'long_description': '# sheets-for-person-schema\n\nFiles for schemasheets exercises at ICBO 2022\n\n## Website\n\n* [https://turbomam.github.io/sheets-for-person-schema](https://turbomam.github.io/sheets-for-person-schema)\n\n## Repository Structure\n\n* [examples/](examples/) - example data\n* [project/](project/) - project files (do not edit these)\n* [src/](src/) - source files (edit these)\n    * [sheets_for_person_schema](src/sheets_for_person_schema)\n        * [schema](src/sheets_for_person_schema/schema) -- LinkML schema (edit this)\n* [datamodel](src/sheets_for_person_schema/datamodel) -- Generated python datamodel\n* [tests](tests/) - python tests\n\n## Developer Documentation\n\n<details>\nUse the `make` command to generate project artefacts:\n\n- `make all`: make everything\n- `make deploy`: deploys site\n\n</details>\n\n## Credits\n\nthis project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)\n',
    'author': 'Mark Andrew Miller',
    'author_email': 'mam@lbl.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
