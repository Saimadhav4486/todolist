from rest_framework import generics
from home.models import Task
from rest_framework.response import Response
from rest_framework import status
from home.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from home.models import Task

class TaskListAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def home(request):
    context = {'success':False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        due_date = request.POST.get('due_date', '')
        if not due_date:
            due_date = None
        status = request.POST['status']
        tags = request.POST['tags']
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        ins = Task(tasktitle = title, taskDesc=desc, due_date=due_date, status = status)
        ins.save()
        print(tag_list)
        existing_tags = []

        for tag_name in tag_list:
            tag, created = ins.tags.get_or_create(name=tag_name)

            if not created:
                existing_tags.append(tag_name)
        context = {'success':True, 'existing_tags': existing_tags}
    return render(request, 'index.html', context)

def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    print(Task.tags)
    return render(request, 'tasks.html', context)