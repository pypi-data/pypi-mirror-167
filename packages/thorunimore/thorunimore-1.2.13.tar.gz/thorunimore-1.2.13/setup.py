# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thorunimore',
 'thorunimore.database',
 'thorunimore.database.base',
 'thorunimore.telegram',
 'thorunimore.web']

package_data = \
{'': ['*'], 'thorunimore.web': ['static/*', 'templates/*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'authlib>=0.14.3,<0.15.0',
 'coloredlogs>=14.0,<15.0',
 'flask-sqlalchemy>=2.4.4,<3.0.0',
 'flask>=1.1.2,<2.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'itsdangerous>=1.1.0,<2.0.0',
 'markupsafe>=1,<2',
 'psycopg2>=2.9.3,<3.0.0',
 'requests>=2.24.0,<3.0.0',
 'royalnet==6.0.0a4',
 'telethon>=1.16.4,<2.0.0']

entry_points = \
{'console_scripts': ['thorunimore-telegram = '
                     'thorunimore.telegram.__main__:main',
                     'thorunimore-web = thorunimore.web.__main__:main']}

setup_kwargs = {
    'name': 'thorunimore',
    'version': '1.2.13',
    'description': 'Authentication gateway bot for the Unimore Informatica Telegram group',
    'long_description': '# Thor Bot\n\nGatekeeper bot for the Unimore Informatica unofficial Telegram group network\n\n\\[ [**Website**](https://thor.steffo.eu) | [PyPI](https://pypi.org/project/thorunimore/) \\]\n\n> NOTE: This bot will be replaced soon with its rewrite, [Loki Bot](https://github.com/Steffo99/lokiunimore). Development on this version has ceased.\n\n![The OpenGraph image of this page, with the project logo in the foreground and a blurred version of the Thor website in the background.](resources/opengraph.png)\n\n## Functionality\n\nIf added as an administrator to a Telegram group, this bot will instantly kick any joining member who hasn\'t passed verification.\n\nVerification is performed by:\n\n1. visiting the bot\'s homepage\n2. pressing the "Verify" button\n3. logging in via Google with a `@studenti.unimore.it` account\n4. following the deep link to Telegram\n5. pressing the "Start" button in the bot chat\n6. answering the few questions the bot asks about the user\'s configuration\n\nAdditionally, verified users of the bot may choose to make their real name available for lookups via a bot command.\n\nVerified members joining a monitored group which made their real name available are announced by the bot in the group.\n\n## Installation via PyPI\n\nThis method is recommended only for development purposes.\n\n1. Create a new venv and enter it:\n   ```console\n   $ python -m venv venv\n   $ source venv/bin/activate\n   ```\n   \n2. Download through PyPI:\n   ```console\n   $ pip install thorunimore\n   ```\n   \n3. Install the packages required to connect to the desired SQL database:\n   \n   - For PostgreSQL:\n     ```console\n     $ pip install psycopg2-binary\n     ```\n\n4. Set the following environment variables:\n\n   - [The URI of the SQL database you want to use](https://docs.sqlalchemy.org/en/13/core/engines.html)\n     ```bash\n     export SQLALCHEMY_DATABASE_URI="postgresql://steffo@/thor_dev"\n     ```\n   \n   - [A Google OAuth 2.0 client id and client secret](https://console.developers.google.com/apis/credentials)\n     ```bash\n     export GOOGLE_CLIENT_ID="000000000000-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.apps.googleusercontent.com"\n     export GOOGLE_CLIENT_SECRET="aaaaaaaaaaaaaaaaaaaaaaaa"\n     ```\n   \n   - A random string of characters used to sign Telegram data\n     ```bash\n     export SECRET_KEY="Questo è proprio un bel test."\n     ```\n   \n   - [api_id and api_hash for a Telegram application](https://my.telegram.org/apps)\n     ```bash\n     export TELEGRAM_API_ID="1234567"\n     export TELEGRAM_API_HASH="abcdefabcdefabcdefabcdefabcdefab"\n     ```\n\n   - [The username and token of the Telegram bot](https://t.me/BotFather)\n     ```bash\n     export TELEGRAM_BOT_USERNAME="thorunimorebot"\n     export TELEGRAM_BOT_TOKEN="1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"\n     ```\n\n   - The desired logging level and format\n     ```bash\n     export LOG_LEVEL="DEBUG"\n     export LOG_FORMAT="{asctime}\\t| {name}\\t| {message}"\n     ```\n   \n   - The url at which web is hosted\n     ```bash\n     export BASE_URL="http://lo.steffo.eu:30008"\n     ```\n     \n   - The url to join the Telegram group\n     ```bash\n     export GROUP_URL="https://t.me/joinchat/AAAAAAAAAAAAAAAAAAAAAA"\n     ```\n\n5. Run both of the project\'s processes simultaneously:\n   ```console\n   $ python -m thorunimore.telegram &\n   $ python -m thorunimore.web &\n   ```\n\n### Configuring as a SystemD unit\n\nThis section assumes the project\'s files are located in `/opt/thorunimore`.\n\n6. Install `gunicorn` in the previously created venv:\n   ```console\n   $ pip install gunicorn\n   ```\n\n7. Create the `bot-thorunimore` systemd unit by creating the `/etc/systemd/system/bot-thorunimore.service` file:\n   ```ini\n   [Unit]\n   Name=bot-thorunimore\n   Description=A moderator bot for the Unimore Informatica group\n   Requires=network-online.target postgresql.service\n   After=network-online.target nss-lookup.target\n   \n   [Service]\n   Type=exec\n   User=thorunimore\n   WorkingDirectory=/opt/thorunimore\n   ExecStart=/opt/thorunimore/venv/bin/python -OO -m thorunimore.telegram\n   Environment=PYTHONUNBUFFERED=1\n   \n   [Install]\n   WantedBy=multi-user.target\n   ```\n\n8. Create the `web-thorunimore` systemd unit by creating the `/etc/systemd/system/web-thorunimore.service` file:\n   ```ini\n   [Unit]\n   Name=web-thorunimore\n   Description=Thorunimore Gunicorn Server\n   Wants=network-online.target postgresql.service\n   After=network-online.target nss-lookup.target\n   \n   [Service]\n   Type=exec\n   User=thorunimore\n   WorkingDirectory=/opt/thorunimore\n   ExecStart=/opt/thorunimore/venv/bin/gunicorn -b 127.0.0.1:30008 thorunimore.web.__main__:reverse_proxy_app\n   \n   [Install]\n   WantedBy=multi-user.target\n   ```\n   \n9. Create the `/etc/systemd/system/bot-thorunimore.d/override.conf` and \n   `/etc/systemd/system/web-thorunimore.d/override.conf` containing the previously configured variables, so that they are passed to the SystemD unit:\n   ```ini\n   [Service]\n   Environment="SQLALCHEMY_DATABASE_URI=postgresql://thorunimore@/thor_prod"\n   Environment="GOOGLE_CLIENT_ID=000000000000-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.apps.googleusercontent.com"\n   Environment="GOOGLE_CLIENT_SECRET=aaaaaaaaaaaaaaaaaaaaaaaa"\n   Environment="SECRET_KEY=Questo è proprio un bel server."\n   Environment="TELEGRAM_API_ID=1234567"\n   Environment="TELEGRAM_API_HASH=abcdefabcdefabcdefabcdefabcdefab"\n   Environment="TELEGRAM_BOT_USERNAME=thorunimorebot"\n   Environment="TELEGRAM_BOT_TOKEN=1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"\n   Environment="LOG_LEVEL=DEBUG"\n   Environment="LOG_FORMAT={asctime}\\t| {name}\\t| {message}"\n   Environment="BASE_URL=https://thor.steffo.eu"\n   Environment="GROUP_URL=https://t.me/joinchat/AAAAAAAAAAAAAAAAAAAAAA"\n   ```\n   \n10. Start (and optionally enable) both services:\n    ```console\n    # systemctl start "bot-thorunimore" "web-thorunimore"\n    # systemctl enable "bot-thorunimore" "web-thorunimore"\n    ```\n\n11. Reverse-proxy the web service with a web server such as Apache HTTPd:\n    ```apacheconf\n    <VirtualHost *:80>\n    \n    ServerName "thor.steffo.eu"\n    Redirect permanent "/" "https://thor.steffo.eu/"\n    \n    </VirtualHost>\n    \n    <VirtualHost *:443>\n    \n    ServerName "thor.steffo.eu"\n    \n    ProxyPass "/" "http://127.0.0.1:30008/"\n    ProxyPassReverse "/" "http://127.0.0.1:30008/"\n    RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}\n    \n    SSLEngine on\n    SSLCertificateFile "/root/.acme.sh/*.steffo.eu/fullchain.cer"\n    SSLCertificateKeyFile "/root/.acme.sh/*.steffo.eu/*.steffo.eu.key"\n    \n    </VirtualHost>\n    ```\n    ```console\n    # a2ensite rp-thorunimore\n    ```\n\n## Installation via Docker\n\nThis method is recommended for production deployments.\n\n- Two Docker images are provided, `thorunimore-web` and `thorunimore-telegram`, which only require configuration of the environment and setup of a reverse proxy.\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'me@steffo.eu',
    'maintainer': 'Stefano Pigozzi',
    'maintainer_email': 'me@steffo.eu',
    'url': 'https://thor.steffo.eu/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
