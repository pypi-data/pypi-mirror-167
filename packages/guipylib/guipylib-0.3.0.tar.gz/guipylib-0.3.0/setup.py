# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guipy', 'guipy.components']

package_data = \
{'': ['*']}

install_requires = \
['pygame>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'guipylib',
    'version': '0.3.0',
    'description': 'UI library for pygame',
    'long_description': '# Guipy\n\n![Python](https://img.shields.io/badge/python-3-blue.svg?v=1)\n![Version](https://img.shields.io/pypi/v/guipylib.svg?v=1)\n![License](https://img.shields.io/pypi/l/guipylib.svg?v=1)\n\nPygame UI Library built by Casey (@caseyhackerman) and Jason\n\n## Installation\n\n```\npip install guipylib\n```\n\nor with poetry\n\n```\npoetry add guipylib\n```\n\n## Components\n\n### Button\n\n<p align="center">\n<img alt="Button" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/button.gif" width="200" />\n</p>\n\n### Dropdown\n\n<p align="center">\n<img alt="Dropdown" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/dropdown.gif" width="500" />\n</p>\n\n### Live Plot\n\n<p align="center">\n<img alt="Live Plot" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/live_plot.gif" width="600" />\n</p>\n\n### Plot\n\n<p align="center">\n<img alt="Plot" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/plot.gif" width="600" />\n</p>\n\n### Slider\n\n<p align="center">\n<img alt="Slider" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/slider.gif" width="600" />\n</p>\n\n### Switch\n\n<p align="center">\n<img alt="Switch" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/switch.gif" width="500" />\n</p>\n\n### Textbox\n\n<p align="center">\n<img alt="Textbox" src="https://github.com/Zjjc123/guipy/blob/main/docs/imgs/textbox.gif" width="600" />\n</p>\n\n## Example\n\n```python\nimport pygame\n\nimport colorsys\n\nfrom guipy.components.slider import Slider\nfrom guipy.manager import GUIManager\nfrom guipy.utils import *\n\nwinW = 1280\nwinH = 720\n\nroot = pygame.display.set_mode((winW, winH))\n\nman = GUIManager()\n\nmySlider = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.4)\nmySlider2 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0)\nmySlider3 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.5)\nmySlider4 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.5)\n\nman.add(mySlider, (0, 25))\nman.add(mySlider2, (0, 75))\nman.add(mySlider3, (0, 125))\nman.add(mySlider4, (0, 175))\n\nrunning = True\nwhile running:\n    events = pygame.event.get()\n    for event in events:\n        if event.type == pygame.QUIT:\n            running = False\n\n    root.fill(DARK_GREY)\n\n    color = tuple(\n        i * 255\n        for i in colorsys.hls_to_rgb(mySlider2.val, mySlider3.val, mySlider4.val)\n    )\n    center = (winW // 2, winH // 2)\n    r = 10 + mySlider.val * 100\n    pygame.draw.circle(root, color, center, r)\n    pygame.draw.circle(root, BLACK, center, r, 3)\n\n    man.update(pygame.mouse.get_pos(), events, root)\n    pygame.display.update()\n```\n\n## Documentation\n\nCheck out some helpful guides and API references [here](https://zjjc123.github.io/guipy/)\n',
    'author': 'Casey Culbertson, Jason Zhang',
    'author_email': 'me@jasonzhang.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Zjjc123/guipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
