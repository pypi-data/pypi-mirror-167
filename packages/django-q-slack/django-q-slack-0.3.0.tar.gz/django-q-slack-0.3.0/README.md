# django-q-slack

A Django Q Error Reporter plugin adding Slack support.

---

## Installation


## Usage
Configure Sentry via the Django Q Q_CLUSTER dictionary in your Django project's settings.py. It is important that the sentry key be set in the error_reporter dictionary, as this name aligns with the project's entry point for this plugin. The only required configuration entry is your Sentry DSN.

```bash
Q_CLUSTER = {
    'error_reporter': {
        'slack': {
            'web_hook': 'https://hooks.slack.com/services/...../..../....'
        }
    }
```