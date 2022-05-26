# MetaSoul Twitch Bot
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy coverage](https://img.shields.io/badge/mypy-100%25-green.svg)](https://github.com/python/mypy)

Developed by [Adam Birds](https://github.com/adambirds) at [ADB Web Designs](https://adbwebdesigns.co.uk).

## Source
The source code can be found [here](https://github.com/emoshape/MetaSoul-Twitch).

## Requirements
Python 3 (Version 3.6 or later).

Get one [MetaSoul™](https://metasoul.store).

## Installation

This has only been tested on Linux, so preferably use Linux or WSL 2 if on Windows.

Navigate to where you will store the bot files, then run:

```
git clone git@github.com:emoshape/MetaSoul-Twitch.git
```

Then run:

```
tools/setup/prep-prod-environment
```

Then run:

```
cp example-config.yaml config.yaml
```

You will then need to edit config.yaml to your needs. You shouldn't delete any of the keys.

The `ACCESS_TOKEN` key can be generated using this [generator](https://twitchtokengenerator.com).

The `name` key under `ACCOUNTS` should tbe the channel name you want the bot to listen to.

The `metasoul_api_key` key under `ACCOUNTS` should be your secret from your [MetaSoul account](https://emoshape.org/cloud_service/backend/web/index.php?r=site%2Flogin).
The `metasoul_epuid` key under `ACCOUNTS` should be your EPUID from your MetaSoul account.

Once you have this running the only thing then left is to setup your bot to run as a service if you wish, which you can do by amending the `./metasoul-twitch-bot.service` file with your working directory and copying it using the following command:

```
cp ./metasoul-twitch-bot.service /lib/systemd/system/
```

Then run:

```
systemctl daemon-reload
```

Then run:

```
systemctl start metasoul-twitch-bot
```

And then to ensure it starts when your server does run:

```
systemctl enable metasoul-twitch-bot
```

## License

This project is released under the [MIT License](https://github.com/emoshape/MetaSoul-Twitch/blob/main/LICENSE).
