# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['generator']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0', 'python-hcl2>=3.0.5,<4.0.0']

entry_points = \
{'console_scripts': ['terragrunt-generator = generator.main:main']}

setup_kwargs = {
    'name': 'terragrunt-generator',
    'version': '0.6.0',
    'description': '',
    'long_description': '# terragrunt-generator\n\n**terragrunt-generator** provide a way to generate a ```terragrunt.hcl``` file with documented inputs who\'s coming from variables exposed by terraform module.\n\nThe result is easily configurable with a **yaml** file.\n## Requirements\n\n- python3.6+\n\n## Instalation\n\n```\n$ pip install terragrunt-generator\n```\n\n## Usages\n\n### Exec\n\n```\nterragrunt-generator -u https://github.com/goabonga/terragrunt-generator.git -v main -p /examples/modules\n\n```\n\n### Results\n\n```\n# modules main\n#\n# yaml config\n# ```\n# modules:\n#   enabled: true\n#   required:\n#   optional: "optional"\n#   # nullable:\n# ```\n#\ninclude {\n    path = "${find_in_parent_folders()}"\n}\n\nlocals {\n    all = merge(\n        yamldecode(file("find_in_parent_folders("config.yaml")")),\n    )\n}\n\nterraform {\n    source = lookup(local.all["modules"], "enabled", true) == true ? "https://github.com/goabonga/terragrunt-generator.git////examples/modules?ref=main" : null\n}\n\ninputs = merge({\n    # required - required value - required\n    required = lookup(local.all["modules"], "required", "None")\n    # optional - optional value\n    optional = lookup(local.all["modules"], "optional", "optional")\n\n},\n  # nullable - nullable value\n  (lookup(local.all["modules"], "nullable", null) == null ? {} : { nullable =  lookup(local.all["modules"], "nullable") })\n)\n\n```\n',
    'author': 'Chris',
    'author_email': 'goabonga@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
