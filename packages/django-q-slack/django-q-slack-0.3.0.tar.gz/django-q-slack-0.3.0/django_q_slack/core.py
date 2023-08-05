import sys
import json
import requests

from traceback import format_stack


class Slack:
    def __init__(self, **kwargs):
        self.__slack_web_hook = kwargs.get('web_hook')

    def report(self):
        exception_details = sys.exc_info()
        trace_stack = format_stack()
        slack_formatted = ''.join(trace_stack).strip()
        self.__send_message(exception_details[0], exception_details[1], slack_formatted)

    def __send_message(self, exception_type, message, traceback):
        payload = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Exception type: `{exception_type.__name__}`\nException message: `{message}`\n```{traceback}```"
                    }
                }
            ]
        }
        requests.post(self.__slack_web_hook, json.dumps(payload))
