from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False) #get one
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# {"id":1,"title":"hello there", "completed":false}

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')

# def index(request):

#     if request.method == "POST":
#         if "addTask" in request.POST:
#             text = request.POST["text"]
#             category = Category(category=text)
#             category.save()

#         if "deleteTask" in request.POST:
#             selected_list = request.POST.getlist('checkedbox')

#             for category_id in selected_list:
#                 category = Category.objects.get(id=int(category_id))
#                 category.delete()

#         return redirect("/")

#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'MiniMemo/index.html', context)

# def lists(request, category_id):

#     if request.method == "POST":
#         if "addTask" in request.POST:
#             text = request.POST["text"]
#             todo = TodoList(text=text, category_id=int(category_id))
#             todo.save()

#         if "deleteTask" in request.POST:
#             selected_list = request.POST.getlist('checkedbox')

#             for todo_id in selected_list:
#                 todo = TodoList.objects.get(id=int(todo_id))
#                 todo.delete()
#         return HttpResponseRedirect(request.path_info)
#     try:
#         todos = TodoList.objects.filter(category_id=int(category_id))
#     except TodoList.DoesNotExist:
#         todos = None
#     context = {'todos': todos}
#     return render(request, 'MiniMemo/lists.html', context)

