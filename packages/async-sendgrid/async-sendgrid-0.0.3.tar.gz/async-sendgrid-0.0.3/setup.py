# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_sendgrid']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.21,<0.22']

setup_kwargs = {
    'name': 'async-sendgrid',
    'version': '0.0.3',
    'description': 'SendGrid simple async client based on httpx.',
    'long_description': '# Async-Sendgrid\n\nSendGrid simple async client based on httpx.\n\n# Installation\n\n```bash\npip install async-sendgrid\n```\n\n# Usage\n\n```python\nimport async_sendgrid\nfrom sendgrid.helpers.mail import Content, Email, Mail, To\nimport os\n\nAPI_KEY = os.environ.get(\'API_KEY\')\n\nfrom_email = Email("test@example.com")\nto_email = To("test@example.com")\nsubject = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"\ncontent = Content("text/plain", "Sed varius ligula ac urna vehicula ultrices. Nunc ut dolor sem.")\nmail = Mail(from_email, to_email, subject, content)\n\ndata = {\n    "personalizations": [\n        {\n            "to": [{"email": "test@example.com"}],\n            "subject": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",\n        }\n    ],\n    "from": {"email": "test@example.com"},\n    "content": [\n        {\n            "type": "text/plain",\n            "value": "Sed varius ligula ac urna vehicula ultrices. Nunc ut dolor sem."\n        }\n    ],\n}\n\n\n# Send email with context manager\n\nasync with async_sendgrid.AsyncClient(api_key=API_KEY) as client:\n    response1 = await client.send(data)\n    response2 = await client.send(mail)\n\n# Send email without context manager\n\nclient = async_sendgrid.AsyncClient(api_key=API_KEY)\nawait client.open()\nresponse1 = await client.send(data)\nresponse2 = await client.send(mail)\nawait client.close()\n\n```\n',
    'author': 'Saltymakov Timofey',
    'author_email': 'saltytimofey@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sensodevices/async-sendgrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
