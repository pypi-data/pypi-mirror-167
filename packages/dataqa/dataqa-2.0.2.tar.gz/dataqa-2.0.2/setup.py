# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataqa', 'dataqa.tests']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.4,<2.0.0', 'pytest>=7.1.3,<8.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'dataqa',
    'version': '2.0.2',
    'description': 'Python Client library for DataQA',
    'long_description': '# DataQA\n\nTODO: Add logo here\n\nDataQA is a tool to perform AI model quality assessment (QA) using an interactive app that can be shared with technical and non-technical members of your team.\n\nTODO: Add a gif.\n\nThe official documentation page is at: [docs.dataqa.ai]().\n\n# Installation\n\n`pip install dataqa`\n\n# Quick start\n\n## Step 1: create an account\n\nGo to (https://app.dataqa.ai/)[https://app.dataqa.ai/login] and follow the steps to create your first project. Once your account and your first project have been created, you will see a screen such as this one:\n\nTODO: Add screenshot of the screen with the publish string\n\nYou will need this key later in order to be able to create your first QA app. You can always come back to this page to find it.\n\n## Step 2: Publish your data\n\nCreating your first shareable QA app is as simple as this:\n\n```python\nimport pandas as pd\nfrom lib.publish import DataQA \ndataqa = DataQA()\ndataqa.login()\n# Prompt username and password\ndf = pd.DataFrame([[1, "Laptop", 1600], [2, "Mouse", 10]], columns=["id", "product", "price"])\ndataqa.publish(PROJECT_ID, df)\n```\n\nThe `PROJECT_ID` is the hash string on the dataqa project page.\n\n## Step 3: Use the UI to explore your data\n\nTODO: add screenshot or GIF\n\n',
    'author': 'Maria Mestre',
    'author_email': 'maria@dataqa.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dataqa.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
