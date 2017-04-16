from django.test import TestCase
from django.core.urlresolvers import resolve


class ScrumBoardURLsTestCase(TestCase):
    def test_root_url(self):
        root = resolve('/admin/scrumboard/')
        self.assertEqual(root.func.__name__, 'IndexView')

    def test_list_url(self):
        list_url = resolve('/admin/scrumboard/list')
        self.assertEqual(list_url.func.__name__, 'RequestsListView')
