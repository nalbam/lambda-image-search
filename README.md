# lambda-image-search

## Install

```bash
$ brew install python@3.9

$ npm install -g serverless

$ sls plugin install -n serverless-python-requirements
$ sls plugin install -n serverless-dotenv-plugin

$ pip3 install --upgrade -r requirements.txt
```

## Credentials

```bash
$ cp .env.example .env
```

### Slack Bot

* <https://console.developers.google.com/>
* <https://console.cloud.google.com/apis/credentials>

```bash
GOOGLE_API_KEY="xxxx"
GOOGLE_API_SECRET="xxxx"
```

## Deployment

In order to deploy the example, you need to run the following command:

```bash
$ sls deploy
```
