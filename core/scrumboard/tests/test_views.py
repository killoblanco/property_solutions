from django.db.models import QuerySet
from django.test import TestCase, RequestFactory

from core.scrumboard.views import *
from core.scrumboard.models import Requirements


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class ReadRequestViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = '/admin/scrumboard/list'
        self.template = 'scrumboard/pages/list.html'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_no_items(self):
        request = self.factory.get(self.url)
        response = ReadRequestView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context_data['solo'].artist, 'Rich')
        with self.assertTemplateUsed(self.template):
            response.render()

    def test_items(self):
        Requirements.objects.create(detail="Test Detail", type="Feature", priority="5", deadline="2017-01-01")
        request = self.factory.get(self.url)
        response = ReadRequestView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed(self.template):
            response.render()


class UpdateRequestViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory
        self.url = 'admin/scrumboard/update/1/'
        self.template = 'scrumboard/pages/form.html'

    def test_update(self):
        Requirements.objects.create(detail="Test Detail", type="Feature", priority="5", deadline="2017-01-01")
        request = self.factory.get(self.url)
        response = UpdateRequestView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed(self.template):
            response.render()
