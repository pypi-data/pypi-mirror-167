# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toasted']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20.0,<0.21.0', 'winsdk>=1.0.0b6,<1.1.0']

setup_kwargs = {
    'name': 'toasted',
    'version': '0.1.0',
    'description': 'Toast notifications library for Windows, built on top of WinRT.',
    'long_description': '# toasted\n\nToast notifications library for Windows. Unlike other Windows toast libraries, Toasted is the one of the most comprehensive toast libraries. Because it supports all elements (images, progresses, texts, inputs, buttons...) that you probably never seen on a toast. Not only that, it also includes useful features found in the Notifications API.\n\n> Struggling with making a GUI for your script? Say no more.\n\n![](.github/assets/preview.png)\n\n## Install\n\n```\npython -m pip install toasted\n```\n\n## Example\n\n```py\nimport asyncio\nfrom typing import Dict\nfrom toasted import Toast, Text\n\n# Create Toast with Toast(),\n# see docstring for all available parameters.\nmytoast = Toast()\n\n# Add elements.\nmytoast += Text("Hello world!")           # Using += operator.\nmytoast.data.append(Text("Hello world!")) # Or access the inner list with Toast.data.\n\n# Set up a handler.\n# This handler will be executed when toasted has clicked or dismissed.\n@mytoast.handler\ndef myhandler(arguments : str, user_input : Dict[str, str], dismiss_reason : int):\n    # dismiss_reason will set to a value higher than or equals to 0 when dismissed,\n    # -1 means a toast or button click.\n    if dismiss_reason == -1:\n        print("Got arguments:", arguments)\n    else:\n        print("Toast has dismissed:", dismiss_reason)\n\n# Run show() async function.\nasyncio.run(mytoast.show())\n```\n\n## Highlights\n\n* **Remote (HTTP) images support**\n    <br>Normally, Windows restricts the use of HTTP images and only allows local file paths on non-UWP applications. But to overcome the limitation, Toasted downloads HTTP images to %TEMP%, so you can now use images from web without any configuration! Downloaded images are deleted once toast has dismissed / clicked. Also, to comply with Windows API, you can enable sending system information (such as `ms-lang`, `ms-theme`, `ms-contrast`) to remote sources as query parameters by setting `add_query_params` property.\n\n* **Update toast content (Data binding)**\n    <br>Properties in toast elements can have a binding/dynamic/reference value, which is done by simply putting a key surrounded with curly braces like, `{myProgress}`. Then, you can set a new value for `myProgress` key before showing toast with `show()`, and with `update()` to update toast in-place without showing a new toast.\n\n* **Import from JSON**\n    <br>Notification elements and their properties can be imported with dictionaries (JSON-accepted types) with `Toast.from_json()`, so you can add more than one element by calling a single method. See example JSON configurations [here.](examples)\n    \n## Notes\n\n* As you can see from screenshot, it is not possible to change "Python" title in normal ways, since Windows requires a "source application" to show notifications from. However, [Toast collections](https://docs.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/toast-collections) allows to override app icon, but I\'m not sure how I can implement this (or even, is it possible for a non-UWP app?), so still working on it.\n',
    'author': 'ysfchn',
    'author_email': '54748183+ysfchn@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ysfchn/toasted',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
