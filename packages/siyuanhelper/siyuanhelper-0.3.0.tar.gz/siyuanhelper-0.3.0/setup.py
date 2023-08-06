# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['siyuanhelper']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'asyncstdlib>=3.10.4,<4.0.0',
 'cchardet>=2.1.7,<3.0.0']

setup_kwargs = {
    'name': 'siyuanhelper',
    'version': '0.3.0',
    'description': 'Helper lib for Siyuan Note',
    'long_description': '<div id="top"></div>\n\n<h3 align="center">siyuanhelper</h3>\n  <p align="center">\n    The Helper Lib for Siyuan Note.\n    <br />\n    <a href="https://clouder0.github.io/siyuanhelper/"><strong>Explore the docs »</strong></a>\n    <br />\n    <a href="https://github.com/Clouder0/siyuanhelper/blob/main/README.zh-Hans.md"><strong>中文 »</strong></a>\n  </p>\n</div>\n\n## 📜 TOC\n\n<details><summary>Table of Contents</summary>\n\n- [🌟 Badges](#🌟-badges)\n- [💡 Introduction](#💡-introduction)\n- [✨ Features](#✨-features)\n- [🎏 Getting Started](#🎏-getting-started)\n- [🗺️ Roadmap](#🗺️-roadmap)\n- [❓ Faq](#❓-faq)\n- [💌 Contributing](#💌-contributing)\n- [🙏 Acknowledgment](#🙏-acknowledgment)\n- [📖 License](#📖-license)\n- [📧 Contact](#📧-contact)\n\n</details>\n\n## 🌟 Badges\n\n[![Test][github-action-test-shield]][github-action-test-url]\n[![Codecov][codecov-shield]][codecov-url]\n[![pre-commit-ci][pre-commit-ci-shield]][pre-commit-ci-url]\n[![pepy-shield]][pepy-url]\n\n[![release-shield]][release-url]\n[![pyversions-shield]][pyversions-url]\n[![Contributors][contributors-shield]][contributors-url]\n[![Forks][forks-shield]][forks-url]\n[![Stargazers][stars-shield]][stars-url]\n[![Issues][issues-shield]][issues-url]\n[![MIT License][license-shield]][license-url]\n[![CodeFactor-shield]][CodeFactor-url]\n[![code-style-black-shield]][code-style-black-url]\n\n<!-- INTRODUCTION -->\n## 💡 Introduction\n\nSiyuan Helper is a python API wrapper for [Siyuan Note](https://github.com/siyuan-note/siyuan).\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## ✨ Features\n\n- Aysnc\n- Object Oriented\n- Type Annotated\n- Fully Documented\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## 🎏 Getting Started\n\nSee our [Quickstart](https://clouder0.github.io/siyuanhelper/quickstart/) to get hands on experience.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## 🗺️ Roadmap\n\nPlease check out our [Github Project](https://github.com/Clouder0/siyuanhelper/projects/1).\n\nSee the [open issues](https://github.com/Clouder0/siyuanhelper/issues) for a full list of proposed features (and known issues).\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## ❓ FAQ\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- CONTRIBUTING -->\n## 💌 Contributing\n\nContributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.\n\nIf you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".\nDon\'t forget to give the project a star! Thanks again!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\nDon\'t forget to see our [Contributing Guidelines](https://github.com/Clouder0/siyuanhelper/blob/main/CONTRIBUTING.md) for details.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## 🙏 Acknowledgment\n\nThere are various open source projects that siyuanhelper depends on, without which this tool wouldn\'t exist. Credits to them!\n\n- [aiohttp](https://github.com/aio-libs/aiohttp), Apache License 2.0\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## 📖 License\n\nDistributed under the MIT License. See `LICENSE` for more information.\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n## 📧 Contact\n\nClouder0\'s email: clouder0@outlook.com\n\nProject Link: [https://github.com/Clouder0/siyuanhelper](https://github.com/Clouder0/siyuanhelper)\n\n<p align="right">(<a href="#top">back to top</a>)</p>\n\n<!-- MARKDOWN LINKS & IMAGES -->\n<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->\n[contributors-shield]: https://img.shields.io/github/contributors/Clouder0/siyuanhelper.svg?style=for-the-badge\n[contributors-url]: https://github.com/Clouder0/siyuanhelper/graphs/contributors\n[forks-shield]: https://img.shields.io/github/forks/Clouder0/siyuanhelper.svg?style=for-the-badge\n[forks-url]: https://github.com/Clouder0/siyuanhelper/network/members\n[stars-shield]: https://img.shields.io/github/stars/Clouder0/siyuanhelper.svg?style=for-the-badge\n[stars-url]: https://github.com/Clouder0/siyuanhelper/stargazers\n[issues-shield]: https://img.shields.io/github/issues/Clouder0/siyuanhelper.svg?style=for-the-badge\n[issues-url]: https://github.com/Clouder0/siyuanhelper/issues\n[license-shield]: https://img.shields.io/github/license/Clouder0/siyuanhelper.svg?style=for-the-badge\n[license-url]: https://github.com/Clouder0/siyuanhelper/blob/main/LICENSE\n[github-action-test-shield]: https://github.com/Clouder0/siyuanhelper/actions/workflows/test.yml/badge.svg?branch=main\n[github-action-test-url]: https://github.com/Clouder0/siyuanhelper/actions/workflows/test.yml\n[codecov-shield]:https://codecov.io/gh/Clouder0/siyuanhelper/branch/main/graph/badge.svg?token=D2XT099AFB\n[codecov-url]: https://codecov.io/gh/Clouder0/siyuanhelper\n[pre-commit-ci-shield]: https://results.pre-commit.ci/badge/github/Clouder0/siyuanhelper/main.svg\n[pre-commit-ci-url]: https://results.pre-commit.ci/latest/github/Clouder0/siyuanhelper/main\n[code-style-black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge\n[code-style-black-url]: https://github.com/psf/black\n[pyversions-shield]: https://img.shields.io/pypi/pyversions/siyuanhelper.svg?style=for-the-badge\n[pyversions-url]: https://pypi.org/project/siyuanhelper/\n[release-shield]: https://img.shields.io/github/release/Clouder0/siyuanhelper.svg?style=for-the-badge\n[release-url]: https://github.com/Clouder0/siyuanhelper/releases\n[CodeFactor-shield]: https://www.codefactor.io/repository/github/clouder0/siyuanhelper/badge/main?style=for-the-badge\n[CodeFactor-url]: https://www.codefactor.io/repository/github/clouder0/siyuanhelper/overview/main\n[pepy-shield]: https://static.pepy.tech/personalized-badge/siyuanhelper?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads\n[pepy-url]: https://pepy.tech/project/siyuanhelper\n',
    'author': 'clouder',
    'author_email': 'clouder0@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.github.com/Clouder0/siyuanhelper',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
