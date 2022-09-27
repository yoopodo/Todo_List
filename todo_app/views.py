from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()  # Todo 테이블의 모든 데이터를 가져와서
    content = {'todos': todos}  # 딕셔너리형태로 content에 넣는다
    return render(request, 'todo_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']  # name값이 todoContent였지!
    new_todo = Todo(content=user_input_str)  # DB의 Todo테이블에 쓰고,
    new_todo.save()  # 저장!
    return HttpResponseRedirect(reverse('index'))  # 처리 후 index.html로 돌아가기
# return HttpResponse("create Todo를 할 거야!=>"+user_input_str)

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한todo의 id", done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
