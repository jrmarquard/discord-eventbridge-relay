# discord-eventbridge-relay

Simple client to relay discord messages to EventBridge.

## Requirements

- python 3.9
- virtualenv (optional)

## Setup

Install python dependencies

```
virtualenv venv
pip install -r requirements.txt
python relay.py
```

Setup env vars

```
cp .env.template .env
```

And populate values with your secrets.

## Start the relay script

```
source venv/bin/activate
python relay.py
```