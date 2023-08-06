# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['picsellia_elasticsearch_client']

package_data = \
{'': ['*']}

install_requires = \
['ElasticMock>=1.8.1,<2.0.0', 'elasticsearch==7.16.2']

setup_kwargs = {
    'name': 'picsellia-elasticsearch-client',
    'version': '1.1.0',
    'description': 'Package wrapping elasticsearch client for Picsellia',
    'long_description': '# Picsellia Elasticsearch Client\n\nPicsellia Elasticsearch Client is a Python library that wraps Elasticsearch Python Client in order to push Picsellia metrics.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.\n\n```bash\npip install picsellia-elasticsearch-client\n```\n\n## Usage\n\n```python\nfrom picsellia_elasticsearch_client.client import PicselliaELKClient\n\nclient = PicselliaELKClient(host="localhost", port=443)\n\nmetric = PicselliaMetric(service="service", data={ "hello" : "world" })\n\nclient.push(metric)\n\nerror = PicselliaError(service="service", exception=KeyError(\'key\'))\n\nclient.push(error)\n\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)',
    'author': 'Thomas Darget',
    'author_email': 'thomas.darget@picsellia.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
