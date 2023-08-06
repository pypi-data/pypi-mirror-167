# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zenconfig', 'zenconfig.formats', 'zenconfig.schemas']

package_data = \
{'': ['*']}

extras_require = \
{'pydantic': ['pydantic>=1,<2'],
 'toml': ['tomli>=2,<3', 'tomli-w>=1,<2'],
 'yaml': ['PyYAML>=6,<7']}

setup_kwargs = {
    'name': 'zenconfig',
    'version': '0.1.0',
    'description': 'Simple configuration loader for python.',
    'long_description': '# simple-config\nSimple configuration loader for python.\n\nCompared to other solutions, the goal is to bring:\n- simple usage for simple use cases\n- multiple format support\n- use objects rather than plain dict to interact with the config\n- optionally use the power of pydantic for validation\n\n## Simple usage\nIf you don\'t want to configure much, you can use:\n```python\nfrom dataclasses import dataclass\nfrom zenconfig import Config\n\n@dataclass\nclass MyConfig(Config):\n    PATH = "~/myconfig.json"\n    \n    some_key: str\n    some_optional_key: bool = False\n\n\ncfg = MyConfig(some_key="hello")\ncfg.save()\n...\ncfg = MyConfig.load()\ncfg.some_optional_key = True\ncfg.save()\n...\ncfg.clear()\n```\n\n## Config file loading\nWhen creating your config, you can specify at least one of those two attributes:\n- `ENV_PATH` the environment variable name containing the path to the config file\n- `PATH` directly the config path\n\n> 💡 When supplying both, if the env var is not set, it will use `PATH`.\n\nThe only transformation on the path made is to expand user constructs.\nIf the file does not exist it will be created (not parent directories though).\nYou can specify the file mode via `Config.FILE_MODE`.\n\n## Read only\nIf you do not want to be able to modify the config from your code, you can use `ReadOnlyConfig`.\n\n## Supported formats\nCurrently, those formats are supported:\n- JSON\n- YAML - requires the `yaml` extra\n- TOML - requires the `toml` extra\n\nThe format is automatically inferred from the config file extension.\nYou can still specify it manually using `Config.FORMAT`, for custom ones or configuring dump options.\n\nTo use them:\n```python\nfrom dataclasses import dataclass\nfrom zenconfig import Config\nfrom zenconfig.formats.yaml import YAMLFormat\n\n@dataclass\nclass MyYAMLConfig(Config):\n    PATH = "~/myconfig.yaml"\n```\n\nOther formats can be added by subclassing either `Format` or `ReadOnlyFormat`\n\n## Supported schemas\nCurrently, those schemas are supported:\n- plain dict\n- dataclasses\n- pydantic models - requires the `pydantic` extra\n\n\nThe format is automatically inferred from the config class.\nYou can still specify it manually using `Config.SCHEMA`, for custom ones or configuring dump options.\n\nTo use pydantic:\n```python\nfrom typing import ClassVar\nfrom pydantic import BaseModel\nfrom zenconfig import Config\n\nclass MyPydanticConfig(Config, BaseModel):\n    PATH: ClassVar[str] = "~/myconfig.yaml"\n```\n\n> ⚠️ When using pydantic, you have to supply the `ClassVar` type annotations\n> otherwise pydantic will treat those as its own fields and complain.\n\n',
    'author': 'Gabriel Pajot',
    'author_email': 'gab@les-cactus.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gpajot/zen-config',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
