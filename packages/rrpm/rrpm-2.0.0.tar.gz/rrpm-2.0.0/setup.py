# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rrpm', 'rrpm.ext', 'rrpm.presets', 'rrpm.presets.base']

package_data = \
{'': ['*']}

install_requires = \
['questionary>=1.10.0,<2.0.0',
 'rich>=12.4.4,<13.0.0',
 'rrpmpkg>=1.0.2,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['rrpm = rrpm.rrpm:cli']}

setup_kwargs = {
    'name': 'rrpm',
    'version': '2.0.0',
    'description': 'A tool to manage all your projects easily!',
    'long_description': '<br/>\n<p align="center">\n    <a href="https://github.com/pybash1/rrpm" target="_blank">\n        <img width="50%" src="https://raw.githubusercontent.com/pybash1/rrpm/master/extra/banner.png" alt="RRPM logo">\n    </a>\n</p>\n<br/>\n<p align="center">\n    <a href="LICENSE" target="_blank">\n        <img src="https://img.shields.io/github/license/pybash1/rrpm.svg" alt="GitHub license">\n    </a>\n    <a href="https://github.com/pybash1/rrpm/releases" target="_blank">\n        <img src="https://img.shields.io/github/tag/pybash1/rrpm.svg" alt="GitHub tag (latest SemVer)">\n    </a>\n    <a href="https://github.com/pybash1/rrpm/commits/" target="_blank">\n        <img src="https://img.shields.io/github/commit-activity/y/pybash1/rrpm.svg" alt="GitHub commit activity">\n    </a>\n    <a href="https://github.com/pybash1/rrpm/graphs/contributors" target="_blank">\n        <img src="https://img.shields.io/github/contributors-anon/pybash1/rrpm.svg" alt="GitHub contributors">\n    </a>\n    <a href="https://deepsource.io/gh/rrpm-org/rrpm/?ref=repository-badge}" target="_blank">\n        <img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/rrpm-org/rrpm.svg/?label=active+issues&show_trend=true&token=8_Tl9hB9xFIiP7QrgjuSZSid"/>\n    </a>\n</p>\n<br/>\n\n[**RRPM**](https://github.com/pybash1/rrpm) is the **all-in-one project and remote repository management tool**. A\nsimple CLI tool that supports project generation for multiple languages, along with support for generating projects\nusing different package managers and/or environments. This repository contains the **core CLI source code**.\n\n## 🚀 Installation and Documentation\n\n`rrpm` can be installed from PyPI\n\n```bash\npip install rrpm\n```\n\nComplete documentation can be found on [GitBook](https://pybash.gitbook.io/rrpm)\n\n## Usage\n\n```bash\n\n Usage: python -m rrpm [OPTIONS] COMMAND [ARGS]...\n\n┌─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐\n│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]        │\n│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the installation. [default: None]                                                                                                     │\n│ --help                                                       Show this message and exit.                                        │\n└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘\n┌─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────┐\n│ config               View current config file or regenerate config file                                 │\n│ create               Generate a project from any of the presets and/or its variations                   │\n│ get                  Clone a remote repository to directory specified in config                         │\n│ list                                                                                                    │\n│ migrate              Migrate and import all repositories from another directory                         │\n│ remove               Remove a cloned repository                                                         │\n│ tree                 List all cloned repositories and generated projects                                │\n└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘\n\n```\n\n## ❤️ Community and Contributions\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\n## 📫 Have a question? Want to chat? Ran into a problem?\n\nWe are happy to welcome you in our official [Discord server](https://discord.gg/FwsGkZAqcZ) or answer your questions via [GitHub Discussions](https://github.com/pybash1/rrpm/discussions)!\n\n## 🤝 Found a bug? Missing a specific feature?\n\nFeel free to **file a new issue** with a respective title and description on the the [pybash1/rrpm](https://github.com/pybash1/rrpm/issues) repository. If you already found a solution to your problem, **we would love to review your pull request**!\n\n## ✅ Requirements\n\nRRPM requires Python >=3.7\n\n## Presets\n\n- [x] Python\n  - [x] Pip\n    - [x] Python Package\n    - [x] FastAPI\n    - [x] Flask\n  - [x] Poetry\n    - [x] Python Package\n    - [x] FastAPI\n    - [x] Flask\n  - [x] Virtual Environments\n    - [x] Python Package\n    - [x] FastAPI\n    - [x] Flask\n- [x] JavaScript\n  - [x] NPM\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n    - [x] Astro\n    - [x] Svelte\n    - [x] SvelteKit\n    - [x] Vue\n  - [x] Yarn\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n    - [x] Astro\n    - [x] Svelte\n    - [x] SvelteKit\n    - [x] Vue\n  - [x] Pnpm\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n- [x] TypeScript\n  - [x] NPM\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n  - [x] Svelte\n  - [x] Vue\n  - [x] Yarn\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n  - [x] Svelte\n  - [x] Vue\n  - [x] Pnpm\n    - [x] NodeJS\n    - [x] ReactJS\n      - [x] create-react-app\n      - [x] Vite\n    - [x] NextJS\n    - [x] Svelte\n    - [x] Vue\n\n## 📘 License\n\nThe RRPM tool is released under the under terms of the [MIT License](https://choosealicense.com/licenses/mit/).\n',
    'author': 'pybash1',
    'author_email': 'pybash@authdeck.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://rrpm.vercel.app',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
