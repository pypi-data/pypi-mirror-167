# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diffusions',
 'diffusions.models',
 'diffusions.models.imagen',
 'diffusions.pipelines',
 'diffusions.schedulers',
 'diffusions.utils']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'einops>=0.4.1,<0.5.0',
 'numpy>=1.21.0',
 'torch>=1.12.0,<2.0.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'diffusions',
    'version': '0.1.11',
    'description': 'Diffusion models',
    'long_description': '# diffusions\nDiffusion models\n',
    'author': 'yuta0306',
    'author_email': 'yuta20010306@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yuta0306/diffusions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
