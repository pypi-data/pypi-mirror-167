# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['powerjira']
install_requires = \
['PyYAML>=6.0,<7.0', 'jira>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'powerjira',
    'version': '0.1.3',
    'description': 'A succinct, minimal local jira control plane that can live in your text editor. Interface with tickets fast!',
    'long_description': '# **PowerJira**\n*A succinct local jira control plane*\n\n<br />\n\n## **Welcome to PowerJira!**\nHate how visually noise and clunky the Jira web-app is? Ever wish you could just type the small subset of issue fields you actually care about into an editor and create/find tickets quickly?\n\nWelcome to the party! 🥳\n\n<br />\n\n### **Table of Contents** 📖\n<hr>\n\n  - [Welcome](#welcome-to-powerjira)\n  - [**Get Started**](#get-started-)\n  - [Usage](#usage-)\n  - [Technologies](#technologies-)\n  - [Contribute](#Contribute-)\n  - [Acknowledgements](#acknowledgements-)\n  - [License/Stats/Author](#license-stats-author-)\n\n<br />\n\n## **Get Started 🚀**\n<hr>\n\nTo get started, clone the [interface repository](https://github.com/anthonybench/powerjira) and populate the config files per the readme.\n\nSpecifically, you need 4 files. These can be named whatever you wish by editing `main.py:59`. \\\nBelow are the requirements of the file with the default (suggested) file names:\n- `summary` - Text file for the issue summary\n- `description` - Text file for the issue description\n- `agent.yml` - Yaml file for user credentials\n- `config.yml` - Yaml file to configure issue creation\n\nSet up your editor space the way you like it, and bam! You\'ve dramatically reduced your time spent in the jira web-app, and even possibly absolve the need for it completely!\n\n<br />\n\n## **Usage ⚙**\n<hr>\n\nWith your shell\'s working directory positioned where the 4 files are present (or if paths have been set accordingly):\n\n**Create ticket with config values**\n```sh\n./main.py [-r|--raw]\n```\n**Fetch info from existing ticket**\n```sh\n./main.py --fetch=<issue-key> [-r|--raw]\n```\n**Info**\n```sh\n./main.py [-h|--help]\n```\n\nThe "*raw*" option flag (`-r`, `--raw`) outputs a formatted dump of the raw api response.\n\n<br />\n\n## **Technologies 🧰**\n<hr>\n\n  - [flip.js](https://google.com)\n  - [flop.js](https://google.com)\n  - [flap.js](https://google.com)\n\n<br />\n\n## **Contribute 🤝**\n<hr>\n\nFeel free to push PR\'s to help make this tool more extensible/flexible over at the [GitHub repo](https://github.com/anthonybench/powerjira).\n\n<br />\n\n## **Acknowledgements 💙**\n<hr>\n\nThanks to Atlassian for making market-leading tools that kinda frustrate me.\n\n<br />\n\n## **License, Stats, Author 📜**\n<hr>\n\n<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />\n\n<!-- badge cluster -->\n\n[SHIELD](https://shields.io/)\n\n<!-- / -->\nSee [License](https://www.gnu.org/licenses/gpl-3.0.txt) for the full license text.\n\nThis repository was authored by *Isaac Yep*.\n\n[Back to Table of Contents](#table-of-contents-📖)',
    'author': 'sleepyboy',
    'author_email': 'anthonybenchyep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anthonybench/powerjira',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
