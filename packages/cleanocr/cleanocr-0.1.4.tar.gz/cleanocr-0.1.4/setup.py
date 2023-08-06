# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleanocr', 'cleanocr.models']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python==4.5.3.56',
 'poetry>=1.0.0,<2.0.0',
 'torch==1.11.0',
 'torchvision==0.12.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['vspoetry = cleanocr:main']}

setup_kwargs = {
    'name': 'cleanocr',
    'version': '0.1.4',
    'description': 'Automatically denoise degraded document images to improve ocr engine',
    'long_description': '<img alt="face-recognition-plugin" src="https://user-images.githubusercontent.com/82228271/189012182-7cd4d760-90d1-4f78-8003-1e01538c3321.png">\n\n## Installation\n```\npip install cleanocr\n```\n\n## Documentation\n```\nimport cv2\nfrom cleanocr import denoise_ocr\n\nimage = cv2.imread(\'test.png\')\nresult = denoise_ocr(image)\ncv2.imwrite(\'result.png\', result)\n```\n\n## How it works\n![example](example/cleanocr.png)\n\n',
    'author': 'prenes',
    'author_email': 'prenes.contact@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.prenes.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
