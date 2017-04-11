import requests
from property_solutions.settings import MAILG_DOMAIN_NAME, MAILG_API_KEY, MAILG_DEFAULT_SENDER


class Mailg:
    url = "https://api.mailgun.net/v3/%s/messages" % MAILG_DOMAIN_NAME
    data = {
        'from': MAILG_DEFAULT_SENDER,
        'to': [],
        'subject': '',
        'text': ''
    }

    def send_mail(self):
        return requests.post(
            self.url,
            auth=("api", MAILG_API_KEY),
            data=self.data
        )
