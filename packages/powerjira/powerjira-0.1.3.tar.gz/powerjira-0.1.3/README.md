# **PowerJira**
*A succinct local jira control plane*

<br />

## **Welcome to PowerJira!**
Hate how visually noise and clunky the Jira web-app is? Ever wish you could just type the small subset of issue fields you actually care about into an editor and create/find tickets quickly?

Welcome to the party! 🥳

<br />

### **Table of Contents** 📖
<hr>

  - [Welcome](#welcome-to-powerjira)
  - [**Get Started**](#get-started-)
  - [Usage](#usage-)
  - [Technologies](#technologies-)
  - [Contribute](#Contribute-)
  - [Acknowledgements](#acknowledgements-)
  - [License/Stats/Author](#license-stats-author-)

<br />

## **Get Started 🚀**
<hr>

To get started, clone the [interface repository](https://github.com/anthonybench/powerjira) and populate the config files per the readme.

Specifically, you need 4 files. These can be named whatever you wish by editing `main.py:59`. \
Below are the requirements of the file with the default (suggested) file names:
- `summary` - Text file for the issue summary
- `description` - Text file for the issue description
- `agent.yml` - Yaml file for user credentials
- `config.yml` - Yaml file to configure issue creation

Set up your editor space the way you like it, and bam! You've dramatically reduced your time spent in the jira web-app, and even possibly absolve the need for it completely!

<br />

## **Usage ⚙**
<hr>

With your shell's working directory positioned where the 4 files are present (or if paths have been set accordingly):

**Create ticket with config values**
```sh
./main.py [-r|--raw]
```
**Fetch info from existing ticket**
```sh
./main.py --fetch=<issue-key> [-r|--raw]
```
**Info**
```sh
./main.py [-h|--help]
```

The "*raw*" option flag (`-r`, `--raw`) outputs a formatted dump of the raw api response.

<br />

## **Technologies 🧰**
<hr>

  - [flip.js](https://google.com)
  - [flop.js](https://google.com)
  - [flap.js](https://google.com)

<br />

## **Contribute 🤝**
<hr>

Feel free to push PR's to help make this tool more extensible/flexible over at the [GitHub repo](https://github.com/anthonybench/powerjira).

<br />

## **Acknowledgements 💙**
<hr>

Thanks to Atlassian for making market-leading tools that kinda frustrate me.

<br />

## **License, Stats, Author 📜**
<hr>

<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />

<!-- badge cluster -->

[SHIELD](https://shields.io/)

<!-- / -->
See [License](https://www.gnu.org/licenses/gpl-3.0.txt) for the full license text.

This repository was authored by *Isaac Yep*.

[Back to Table of Contents](#table-of-contents-📖)