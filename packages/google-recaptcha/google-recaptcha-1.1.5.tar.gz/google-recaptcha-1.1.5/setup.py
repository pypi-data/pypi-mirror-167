# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['google_recaptcha']

package_data = \
{'': ['*'], 'google_recaptcha': ['templates/*']}

install_requires = \
['Flask>=2.2.2,<3.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'google-recaptcha',
    'version': '1.1.5',
    'description': "Google recaptcha helps you protect your web form by using google's latest recaptcha (Completely Automated Public Turing test to tell Computers and Humans Apart) technology.",
    'long_description': '# Standalone Google Recaptcha for Python\nGoogle recaptcha helps you protect your web form by using google\'s latest recaptcha \n(Completely Automated Public Turing test to tell Computers and Humans Apart) technology.\n\n[![PyPi](https://github.com/jpraychev/google-recaptcha/actions/workflows/python-publish.yml/badge.svg)](https://github.com/jpraychev/google-recaptcha/actions/workflows/python-publish.yml)\n[![PyPI Downloads](https://img.shields.io/pypi/dm/google-recaptcha.svg)](https://pypistats.org/packages/google-recaptcha)\n\n# Documentation\n\n# Installation\n```\npip install google-recaptcha\n```\n\n# Introduction\nCurrent version of the library works by placing the {{ recaptcha }} object in the form you want to protect. It searches automatically for the form that the object is placed in.\n\nIn your views file with RECAPTCHA_SITE_KEY and RECAPTCHA_SECRET_KEY exported as environment variables.\n\n```\n# With environment variables\n\nfrom google_recaptcha import ReCaptcha\napp = Flask(__name__)\nrecaptcha = ReCaptcha(app=app)\n\n@app.route("/contact/", methods=["GET", "POST"])\ndef home():\n\n    if recaptcha.verify():\n        print(\'Recaptcha has successded.\')\n    else:\n        print(\'Recaptcha has failed.\')\n```\n\n```\n# Without environment variables\nfrom google_recaptcha import ReCaptcha\napp = Flask(__name__)\nrecaptcha = ReCaptcha(\n    app=app,\n    site_key="your-site-key",\n    secret_key="your-secret-key"\n)\n\n@app.route("/contact/", methods=["GET", "POST"])\ndef home():\n\n    if recaptcha.verify():\n        print(\'Recaptcha has successded.\')\n    else:\n        print(\'Recaptcha has failed.\')\n```\nIn your HTML template file:\n```\n<form id="contact-form" method="post" class="control-form">\n    <div class="row">\n        <div class="col-xl-6">\n            <input type="text" name="name" placeholder="Name" required="" id="id_name">\n        </div>\n        <div class="col-xl-6">\n            <input type="text" name="email" placeholder="Email" required="" id="id_email">\n        </div>\n        <div class="col-xl-12">\n            <input type="text" name="subject" placeholder="Subject" required="" id="id_subject">\n        </div>\n        <div class="col-xl-12">\n            <textarea name="message" cols="40" rows="10" placeholder="Message" required="" id="id_message"></textarea>\n        </div>\n        <div class="col-xl-12">\n            <button id="form-btn" type="submit" class="btn btn-block btn-primary">Send now</button>\n        </div>\n    </div>\n    {{ recaptcha }}\n</form>\n```',
    'author': 'Jordan Raychev',
    'author_email': 'jpraychev@gmail.com',
    'maintainer': 'Jordan Raychev',
    'maintainer_email': 'jpraychev@gmail.com',
    'url': 'https://github.com/jpraychev/google-recaptcha',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
