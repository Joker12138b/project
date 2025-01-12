# -*- coding: UTF-8 -*- #
"""
@filename:file_ops.py
@author:cxt
@time:2025-01-11
@function: 文件操作
"""
import json
import os
from task import Task, SubTask

dataFile = './data/data.json'


def load_tasks():
    """加载任务数据"""
    if not os.path.exists(dataFile):
        return []

    with open(dataFile, "r", encoding="utf-8") as file:
        task_data = json.load(file)
        # return [Task.from_dict(task) for task in task_data]
        tasks = []
        for task in task_data:
            if "parent_task" in task:
                parent_task = next(t for t in tasks if t.name == task["parent_task"])
                tasks.append(SubTask(task["name"], parent_task, task["completed"]))
            else:
                if isinstance(task["tags"], str):
                    tasks["tags"] = [task["tags"]]
                tasks.append(Task(task["name"], task["completed"], task["tags"]))
        return tasks


def save_tasks(tasks):
    """保存任务数据"""
    task_data = [Task.to_edit(task) for task in tasks]
    with open(dataFile, 'w', encoding="utf-8") as file:
        json.dump(task_data, file, ensure_ascii=False, indent=4)

