import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Task, Category
from .forms import FormTask, FormCategory


def index(request):
    return render(request, 'index.html')


def Category_View(request):
    return render(request, 'category_list.html', {
        'category': Category.objects.all,
        'title': "Category"
    })


def Todolist_View(request):
    return render(request, 'task_list.html', {
        'todo_tasks': Task.objects.filter(status_id=1).order_by('due_date'),
        'ongoing_tasks': Task.objects.filter(status_id=2).order_by('due_date'),
        'done_tasks': Task.objects.filter(status_id=3).order_by('due_date'),
        'abandoned_tasks': Task.objects.order_by('due_date').filter(status_id=4).order_by('due_date'),

        'todo_count': Task.objects.filter(status_id=1).count(),
        'ongoing_count': Task.objects.filter(status_id=2).count(),
        'done_count': Task.objects.filter(status_id=3).count(),
        'abandoned_count': Task.objects.filter(status_id=4).count(),
        'title': "Todolist"
    })


def add_task(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TaskListChanged": None,
                        "showMessage": f"{task.title} added."
                    })
                })

    else:
        form = FormTask()
    return render(request, 'task_form.html', {
        'form': form,
    })


def add_category(request):
    if request.method == "POST":
        form = FormCategory(request.POST)
        if form.is_valid():
            category = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TaskListChanged": None,
                        "showMessage": f"{category.name} added."
                    })
                })

    else:
        form = FormCategory()
    return render(request, 'category_form.html', {
        'form': form,
    })


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = FormTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "categoryListChanged": None,
                        "showMessage": f"{task.title} updated."
                    })
                }
            )
    else:
        form = FormTask(instance=task)
    return render(request, 'task_form.html', {
        'form': form,
        'task': task,
    })


def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = FormCategory(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "categoryListChanged": None,
                        "showMessage": f"{category.name} updated."
                    })
                }
            )
    else:
        form = FormCategory(instance=category)
    return render(request, 'category_form.html', {
        'form': form,
        'category': category,
    })


def change_status(request, id_task, id_status):
    Task.objects.filter(id=id_task).update(status_id=id_status)
    return redirect('/task_list')


def remove_task(request, id):
    task = Task.objects.filter(id=id)
    task.delete()
    # messages.success(request, "Data Terhapus")
    return redirect('/task_list')


def remove_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    # messages.success(request, "Data Terhapus")
    return redirect('/category')
