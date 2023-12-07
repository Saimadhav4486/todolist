from django.test import TestCase
from home.models import Task, Tag
from datetime import datetime

class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='TestTag')
        self.task = Task.objects.create(
            tasktitle='Test Task',
            taskdesc='Task description',
            status='OPEN',
            duedate=datetime.now(),
        )
        self.task.tags.add(self.tag)

    def test_task_has_tags(self):
        self.assertIn(self.tag, self.task.tags.all())

    def test_task_fields(self):
        self.assertEqual(self.task.tasktitle, 'Test Task')
        self.assertEqual(self.task.taskdesc, 'Task description')
        self.assertEqual(self.task.status, 'OPEN')
