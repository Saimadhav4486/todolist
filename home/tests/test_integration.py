from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from home.models import Task, Tag
from datetime import datetime

class TestIntegration(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name='TestTag')

    def test_create_task_api(self):
        url = reverse('task-list-create')
        data = {
            'tasktitle': 'New Task',
            'taskdesc': 'Description',
            'status': 'OPEN',
            'duedate': datetime.now().isoformat(),
            'tags': [self.tag.id],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
