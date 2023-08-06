# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rgb_lib', 'rgb_lib._rgb_lib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rgb-lib',
    'version': '0.1.1',
    'description': 'RGB Lib Python language bindings.',
    'long_description': '# RGB Lib Python bindings\n\nThis project builds a Python library, `rgb-lib`, for the [rgb-lib]\nRust library, which is included as a git submodule. The bindings are created by\nthe [rgb-lib-ffi] project, which is located inside the rgb-lib submodule.\n\n## Install from PyPI\n\nInstall the [latest release] by running:\n```shell\npip install rgb-lib\n```\n\n## Install locally\n\n### Requirements\n- [cargo]\n- [poetry]\n\nIn order to install the project locally, run:\n```shell\n# Update the submodule\ngit submodule update --init\n\n# Generate the bindings\n./generate.sh\n\n# Build the source and wheels archives\npoetry build\n\n# Install the wheel\npip install ./dist/rgb_lib-<version>-py3-none-any.whl\n\n# or install the sdist\npip install ./dist/rgb-lib-<version>.tar.gz\n```\n\n\n[cargo]: https://github.com/rust-lang/cargo\n[rgb-lib]: https://github.com/RGB-Tools/rgb-lib\n[rgb-lib-ffi]: https://github.com/RGB-Tools/rgb-lib/tree/master/rgb-lib-ffi\n[latest release]: https://pypi.org/project/rgb-lib/\n[poetry]: https://github.com/python-poetry/poetry\n',
    'author': 'Zoe Faltibà',
    'author_email': 'zoefaltiba@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/RGB-Tools/rgb-lib-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
