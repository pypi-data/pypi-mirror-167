# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cryptmoji']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cryptmoji',
    'version': '2.0.0',
    'description': 'Encrypt Text using emojis!',
    'long_description': '# 🐱\u200d👤 Cryptmoji\n\nA simple emoji-based encryption-decryption library.\n_______________________\n\n## 📥 Installation\n\npip install the library:\n\n```sh\npip install cryptmoji\n```\n\n## 📝 Usage\n\n```python\nfrom cryptmoji import Cryptmoji\n\ntext = "Hello World!"\nkey = "random_key" # makes the encryption stronger (optional)\n\na = Cryptmoji(text, key=key)\n# The encrypt and decrypt functions return the value\nencrypted = a.encrypt()\nprint(encrypted)\n# 🎚️🎨🎼🎲🏀🍯🎓🎼🎹🏂🎸🍤\n\n# The encrypt and decrypt functions change the value in-place too\na.decrypt() \nprint(decrypted)\n# Hello World!\n```\n',
    'author': 'Siddhesh Agarwal',
    'author_email': 'siddhesh.agarwal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Siddhesh-Agarwal/cryptmoji',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
