from django.test import LiveServerTestCase
from selenium import webdriver

from core.scrumboard.models import Requirements


class ListViewUserTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(2)
        self.url = self.live_server_url + '/admin/scrumboard/list'

    def no_item(self):
        page = self.browser.get(self.url)

    def item(self):
        Requirements.objects.create(detail="Test Detail", type="Feature", priority="5", deadline="2017-01-01")
        page = self.browser.get(self.url)

