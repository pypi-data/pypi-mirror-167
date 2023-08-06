# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cerebrate_sdk']

package_data = \
{'': ['*']}

install_requires = \
['requests']

setup_kwargs = {
    'name': 'cerebrate-sdk',
    'version': '0.1.5',
    'description': 'Cerebrate SDK',
    'long_description': '# Cerebrate SDK\n\n## Install\n### with poetry\n```shell\npoetry add cerebrate-sdk\n```\n\n### or with pip\n```shell\npip install cerebrate-sdk\n```\n\n## Examples\n### Fake email detector\n```python\nfrom cerebrate_sdk import Cerebrate\n\nc = Cerebrate(\'YOUR_API_KEY\')\n\ntask = "Detect if email is fake or real"\nexamples = [\n    "qwertyuiooiu@ihdj.com: fake"\n    "support@cerebrate.ai: real",\n]\n\nresult = c.predict(task, examples, "lajotig138@5k2u.com: ")\n\nprint(result[0])\n# fake\n\n```\n\n### With options\n```python\nfrom cerebrate_sdk import Cerebrate, Options\n\nc = Cerebrate(\'YOUR_API_KEY\')\n\noptions = Options(\n    stop=[\'Q:\'],\n    temperature=0.7,\n    max_tokens=100,\n    top_p=1,\n    presence_penalty=0,\n    frequency_penalty=0,\n    best_of=1\n)\n\ntask = "Detect if email is fake or real"\nexamples = [\n    "qwertyuiooiu@ihdj.com: fake"\n    "support@cerebrate.ai: real",\n]\n\nresult = c.predict(task, examples, "lajotig138@5k2u.com: ", options=options)\n\nprint(result[0])\n# fake\n\n```\n\n### Raw usage\n```python\nfrom cerebrate_sdk import Cerebrate\n\nc = Cerebrate("YOUR_API_KEY")\n\nresult = c.raw("Suggest the next item for user\'s cart."\n               "Cart: bacon, eggs, tomatoes"\n               "Suggested item: ")\nprint(result[0])\n# sausage\n\n```',
    'author': 'Cerebrate AI',
    'author_email': 'admin@cerebrate.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
