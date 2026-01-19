from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TaskForm
import openpyxl
from django.http import HttpResponse
from .models import Task


def task_create(request):
    if request.method == "POST":
        Task.objects.create(
            use_case_name=request.POST.get("use_case_name"),
            uce_name=request.POST.get("uce_name"),
            tower=request.POST.get("tower"),
            task_type=request.POST.get("task_type"),
            task_description=request.POST.get("task_description"),
            time_to_complete=request.POST.get("time_to_complete"),
        )
        return redirect("success")

    return render(request, "task_form.html")


def success(request):
    return render(request, "success.html")

def export_tasks_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tasks"

    # ✅ Updated headers
    ws.append([
        "Use Case Name",
        "UCE Name",
        "Tower",
        "Task Type",
        "Task Description",
        "Time to Complete (Minutes)",
        "Created At"
    ])

    # Fetch data from DB
    tasks = Task.objects.all().order_by('-created_at')

    for task in tasks:
        ws.append([
            task.use_case_name,
            task.uce_name,
            task.tower,
            task.task_type,           # shows label value in Excel
            task.task_description,
            task.time_to_complete,    # ✅ Minutes (NO float conversion)
            task.created_at.strftime("%Y-%m-%d %H:%M")
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=task_data.xlsx"

    wb.save(response)
    return response
