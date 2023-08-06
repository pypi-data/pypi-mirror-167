# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipl_config']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.3.0,<5.0.0'],
 'dotenv': ['python-dotenv>=0.21.0,<0.22.0'],
 'hcl2': ['python-hcl2>=3.0.5,<4.0.0'],
 'toml': ['toml>=0.10.2,<0.11.0'],
 'yaml': ['pyyaml>=5.0,<7.0']}

setup_kwargs = {
    'name': 'ipl-config',
    'version': '0.1.9',
    'description': 'InPlat config adapters',
    'long_description': '[![tests](https://github.com/koi8-r/ipl-config/actions/workflows/ci.yml/badge.svg)](https://github.com/koi8-r/ipl-config/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/koi8-r/ipl-config/branch/master/graph/badge.svg?token=OKURU75Y7A)](https://codecov.io/gh/koi8-r/ipl-config)\n[![pypi](https://img.shields.io/pypi/v/ipl-config.svg)](https://pypi.python.org/pypi/ipl-config)\n[![versions](https://img.shields.io/pypi/pyversions/ipl-config.svg)](https://github.com/koi8-r/ipl-config)\n\n\n# Config adapters with pydantic behavior\n- json\n- yaml\n- toml\n- hcl2\n- environ\n- .env\n- TODO: multiline PEM keys load with cryptography\n\n## Examples\n### .env\n```dotenv\nAPP_VERSION=v0.0.1a1\nAPP_HTTP_HOST=myname.lan\nHTTP_2=true\nAPP_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQg8M4vd2AmKTW0/nqc\nYQBi/bRZjkVezdGHi+zH5kYvm/2hRANCAATxEs1e8hqwpYCTk3amfq/UnGyvViPZ\nMidz4nFzQvcq7A9Ju/wvEfLDjA131kh2Sk+x3dgLxhTf7yKJXZC0jg3d\n-----END PRIVATE KEY-----"\n```\n### config.yaml\n```yaml\nhttp:\n  port: 10001\n  transport:\n    timeout: 60.0\n    buffer_size: 65535\n  interfaces:\n    - 127.0.0.1\n    - 192.168.0.1\nversion: 1\n```\n### yaml with env, dotenv and args overrides\n```python\nfrom datetime import datetime\nfrom ipaddress import IPv4Address\nfrom os import environ\nfrom pathlib import Path\nfrom typing import Dict, Union\n\nfrom pydantic import BaseModel, Field\n\nfrom ipl_config import BaseSettings\n\n\nclass TcpTransport(BaseModel):\n    timeout: float  # from config file\n    buffer_size: int = Field(0.01, env=\'BUFF_SIZE\')  # from env\n\n\nclass Http(BaseModel):\n    host: str  # from dotenv\n    bind: str  # from env\n    port: int  # from config file\n    interfaces: list[IPv4Address]  # from config file\n    transport: TcpTransport\n    http2: bool = Field(env=\'HTTP_2\')  # from dotenv\n\n\nclass IplConfig(BaseSettings):\n    version: str  # from kwargs\n    created: datetime  # from env\n    http: Http  # env also works for complex objects\n    private_key: str  # from dotenv\n    group_by_id: Union[Dict[int, str], None]\n\n\nif __name__ == "__main__":\n    environ[\'app_http_bind\'] = \'1.1.1.1\'\n    environ[\'buff_size\'] = \'-1\'\n    environ[\'app_created\'] = \'2000-01-01T00:00:00Z\'\n    environ[\'app_group_by_id_0\'] = \'root\'\n\n\n    root = Path(\'.\')\n\n    cfg = IplConfig(\n        version=\'v0.0.1a1\',\n        env_file=root / \'.env\',\n        config_file=root / \'config.yaml\',\n    )\n    cfg.write_json(indent=4)\n    print()\n```\n',
    'author': 'InPlat',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/koi8-r/ipl-config',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
