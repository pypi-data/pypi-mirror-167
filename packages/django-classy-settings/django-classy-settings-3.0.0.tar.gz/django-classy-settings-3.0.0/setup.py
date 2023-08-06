# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cbs']

package_data = \
{'': ['*']}

install_requires = \
['Django']

setup_kwargs = {
    'name': 'django-classy-settings',
    'version': '3.0.0',
    'description': 'Simple class-based settings for Django',
    'long_description': 'django-classy-settings\n======================\n\nMinimalist approach to class-based settings for Django\n\nhttps://django-classy-settings.readthedocs.io/en/latest/\n\n\nQuick Start\n-----------\n\nIn your `settings.py`\n\n    from cbs import BaseSettings, env\n\n\n    ...\n    # For env settings with a DJANGO_ prefix\n    denv = env(prefix=\'DJANGO_\')\n\n    class Settings(BaseSettings):\n\n        DEBUG = denv.bool(True)  # Controlled by DJANGO_DEBUG\n\n        DEFAULT_DATABASE = denv.dburl(\'sqlite://db.sqlite\')\n\n        def DATABASES(self):\n            return {\n                \'default\': self.DEFAULT_DATABASE,\n            }\n\n\n    class ProdSettings(Settings):\n        DEBUG = False\n\n        @env\n        def STATIC_ROOT(self):\n            raise ValueError("Must set STATIC_ROOT!")\n\n    __getattr__ = BaseSettings.use()\n\n\nSwitch between ``Settings`` and ``ProdSettings`` using the ``DJANGO_MODE`` env var:\n\n    # Run default Settings\n    $ ./manage.py test\n\n    # Run ProdSettings\n    $ DJANGO_MODE=prod ./manage.py test\n',
    'author': 'Curtis Maloney',
    'author_email': 'curtis@tinbrain.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://django-classy-settings.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
