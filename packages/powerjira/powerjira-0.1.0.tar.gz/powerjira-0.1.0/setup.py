# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['powerjira', 'powerjira.toolchain']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'jira>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'powerjira',
    'version': '0.1.0',
    'description': 'A succinct local jira control plane that can live in your text editor. Run jql, author issues and more!',
    'long_description': '# **PowerJira**\n*A succinct local jira control plane*\n\n<br />\n\n## **Welcome to PowerJira!**\nHello world.\n\n<br />\n\n### **Table of Contents** 📖\n<hr>\n\n  - [Welcome](#welcome-to-powerjira)\n  - [**Get Started**](#get-started-)\n  - [Usage](#usage-)\n  - [Technologies](#technologies-)\n  - [Contribute](#Contribute-)\n  - [Acknowledgements](#acknowledgements-)\n  - [License/Stats/Author](#license-stats-author-)\n\n<br />\n\n## **Get Started 🚀**\n<hr>\n\nHello world.\n\n<br />\n\n## **Usage ⚙**\n<hr>\n\nHello world.\n\n<br />\n\n## **Technologies 🧰**\n<hr>\n\n  - [flip.js](https://google.com)\n  - [flop.js](https://google.com)\n  - [flap.js](https://google.com)\n\n<br />\n\n## **Contribute 🤝**\n<hr>\n\nHello world.\n\n<br />\n\n## **Acknowledgements 💙**\n<hr>\n\nHello world.\n\n<br />\n\n## **License, Stats, Author 📜**\n<hr>\n\n<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />\n\n<!-- badge cluster -->\n\n[SHIELD](https://shields.io/)\n\n<!-- / -->\nSee [License](https://google.com) for the full license text.\n\nThis repository was authored by *Isaac Yep*.\n\n[Back to Table of Contents](#table-of-contents-)',
    'author': 'sleepyboy',
    'author_email': 'anthonybenchyep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
