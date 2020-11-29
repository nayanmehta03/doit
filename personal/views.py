from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Board, Task
import json
from django.http import HttpResponse


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        boards = Board.objects.filter(owner=request.user)
        task_stat = {}
        for board in boards:
            tasks = Task.objects.filter(board=board)
            ongoing, complete, total = 0, 0, 0
            for task in tasks:
                if task.ongoing:
                    ongoing += 1
                elif task.completed:
                    complete += 1
                total += 1
            task_stat[board] = [total, ongoing, complete]
        print(task_stat)
        return render(request, 'personal/index.html', {'data': boards, 'stat': task_stat})
    else:
        return redirect('login')


def add_board(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            new_board = Board(name=name, description=desc, owner=request.user)
            new_board.save()
            response = {'status': 0, 'message': 'Board Created.', 'url': '/login'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')


def add_task(request, board_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            board = Board.objects.filter(id=board_id)[0]
            new_task = Task(name=name, description=desc, board=board, completed=False, ongoing=False)
            new_task.save()
            response = {'status': 0, 'message': 'Task Created.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')


def tasks(request, board_id):
    if request.user.is_authenticated:
        board = Board.objects.filter(id=board_id)[0];
        tasks = Task.objects.filter(board=board)
        return render(request, 'tasks/index.html', {'tasks': tasks, 'board': board})
    else:
        return redirect('login')


@csrf_exempt
def delete_task(request, task_id):
    if request.user.is_authenticated:
        if request.method == 'DELETE':
            Task.objects.filter(id=task_id).delete()
            response = {'status': 0, 'message': f'Task Deleted.'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        return redirect('login')


@csrf_exempt
def start_task(request, task_id):
    if request.user.is_authenticated:
        if request.method == 'UPDATE':
            Task.objects.filter(id=task_id).update(ongoing=True)
            response = {'status': 0, 'message': f'Task Started.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')


@csrf_exempt
def complete_task(request, task_id):
    if request.user.is_authenticated:
        if request.method == 'UPDATE':
            Task.objects.filter(id=task_id).update(completed=True, ongoing=False)
            response = {'status': 0, 'message': f'Task Completed.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')

@csrf_exempt
def delete_board(request, board_id):
    if request.user.is_authenticated:
        if request.method == 'DELETE':
            Board.objects.filter(id=board_id).delete()
            response = {'status': 0, 'message': f'Board Deleted.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')

