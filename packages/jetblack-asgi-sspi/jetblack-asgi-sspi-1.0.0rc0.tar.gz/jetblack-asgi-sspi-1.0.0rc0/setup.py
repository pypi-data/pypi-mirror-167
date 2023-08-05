# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetblack_asgi_sspi']

package_data = \
{'': ['*']}

install_requires = \
['bareutils>=4.0.1,<5.0.0',
 'jetblack-asgi-typing>=0.4.0,<0.5.0',
 'pyspnego>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'jetblack-asgi-sspi',
    'version': '1.0.0rc0',
    'description': 'ASGI middleware for SSPI',
    'long_description': '# jetblack-asgi-sspi\n\n[ASGI](https://asgi.readthedocs.io/en/latest/index.html) middleware\nfor [SSPI](https://en.wikipedia.org/wiki/Security_Support_Provider_Interface) authentication\non Windows.\n\nThis is not specific to a particular ASGI framework or server.\n\n## Installation\n\nInstall from the pie store.\n\n```\npip install jetblack-asgi-sspi\n```\n\n## Usage\n\nThe following program uses the\n[Hypercorn](https://pgjones.gitlab.io/hypercorn/)\nASGI server, and the\n[bareASGI](https://github.com/rob-blackbourn/bareASGI)\nASGI framework.\n\n```python\nimport asyncio\nimport logging\n\nfrom bareasgi import Application, HttpRequest, HttpResponse\nfrom bareutils import text_writer\nfrom hypercorn import Config\nfrom hypercorn.asyncio import serve\n\nfrom jetblack_asgi_sspi.spnego_middleware import SPNEGOMiddleware, SSPIDetails\n\n# A callback to display the results of the SSPI middleware.\nasync def http_request_callback(request: HttpRequest) -> HttpResponse:\n    # Get the details from scope[\'extensions\'][\'sspi\']. Note if\n    # authentication failed this might be absent or empty.\n    extensions = request.scope.get(\'extensions\', {})\n    sspi_details = extensions.get(\'sspi\', {})\n    client_principal = sspi_details.get(\'client_principal\', \'unknown\')\n\n    message = f"Authenticated as \'{client_principal}\'"\n\n    return HttpResponse(\n        200,\n        [(b\'content-type\', b\'text/plain\')],\n        text_writer(message)\n    )\n\nasync def main_async():\n    # Make the ASGI application.\n    app = Application()\n    app.http_router.add({\'GET\'}, \'/\', http_request_callback)\n\n    # Wrap the application with the middleware.\n    wrapped_app = SPNEGOMiddleware(\n        app,\n        protocol=b\'NTLM\',  # NTLM or Negotiate\n        forbid_unauthenticated=True\n    )\n\n    # Start the ASGI server.\n    config = Config()\n    config.bind = [\'localhost:9023\']\n    await serve(wrapped_app, config)\n\nif __name__ == \'__main__\':\n    logging.basicConfig(level=logging.DEBUG)\n    asyncio.run(main_async())\n```\n\n### Arguments\n\nThe `SPNEGOMiddleware` wraps the ASGI application. The first and only\npositional argument is the ASGI application. Optional arguments include:\n\n* `protocol` (`bytes`): Either `b"Negotiate"` or `b"NTLM"` (for systems not part of a domain).\n* `service` (`str`): The SPN service. Defaults to `"HTTP"`.\n* `hostname` (`str`, optional): The hostname. Defaults to `gethostname`.\n* `session_duration` (`timedelta`, optional): The duration of a session. Defaults to 1 hour.\n* `forbid_unauthenticated` (`bool`): If true, and authentication fails, send 403 (Forbidden). Otherwise handle the request unauthenticated.\n\n### Results\n\nIf the authentication is successful the SSPI details are added to the\n`"extensions"` property of the ASGI scope under the property `"sspi"`.\nThe following properties are set:\n\n* `"client_principal"` (`str`): The username of the client.\n* `"negotiated_protocol"` (`str`): The negotiated protocol.\n* `"protocol"` (`str`): The requested protocol.\n* `"spn"` (`str`): The SPN of the server.\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/jetblack-asgi-sspi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
