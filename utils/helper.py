# -*- coding: UTF-8 -*- #
"""
@filename:helper.py
@author:cxt
@time:2025-01-04
"""
import json
import os
from task import Task
from utils.task_utils import TaskUtils

dataFile = './data/data.json'


def print_welcome():
    print("=" * 50)  # 设置分隔符
    print("欢迎使用任务管理系统".center(50, "-"))
    print("=" * 50)  # 设置分隔符


# def display_tasks(tasks):
#     """ 显示任务列表 """
#     if not tasks:
#         print("没有任务")
#         return
#     for index, task in enumerate(tasks, 1):
#         print(f"{index}. {task}")


def load_tasks():
    """加载任务数据"""
    if not os.path.exists(dataFile):
        return []

    with open(dataFile, "r", encoding="utf-8") as file:
        task_data = json.load(file)
        return [Task.from_dict(task) for task in task_data]
    # tasks = []
    # if os.path.exists(dataFile):
    #     with open(dataFile, 'r', encoding="utf-8") as file:
    #         tasks = json.load(file)
    #         tasks = [Task(task['name'], task['completed']) for task in tasks]
    # return tasks


def save_tasks(tasks):
    """保存任务数据"""
    task_data = [Task.to_edit() for task in tasks]
    # task_data = [{"name": task.name, "completed": task.completed} for task in tasks]
    with open(dataFile, 'w', encoding="utf-8") as file:
        json.dump(task_data, file, ensure_ascii=False, indent=4)


def add_task(tasks):
    """添加任务"""
    # tasks.append({"name": name, "completed": False})
    # save_tasks(tasks)
    #     print("任务名称不能为空")
    # task_name = input("请输入任务名称: ")
    # new_task = {"name": task_name, "completed": False}
    # tasks.append(new_task)
    # save_tasks(tasks)
    while True:
        task_name = input("请输入任务名称: ")
        if task_name.strip():
            new_task = Task(task_name)
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"任务'{task_name}'已添加")
            break
        else:
            print("任务名称不能为空")


def edit_task(tasks):
    """编辑任务"""
    if not tasks:
        print("没有任务可供编辑")
        return

    try:
        task_id = int(input("请输入要编辑的任务编号: ")) - 1
        if 0 <= task_id < len(tasks):
            task = tasks[task_id]
            print(f"当前任务: {task}")
            new_name = input("请输入新的任务名称(按回车跳过): ")
            if new_name.strip():
                task.name = new_name
            status = input("任务是否完成? (y/n): ").strip().lower()
            if status == 'y':
                task.mark_completed()
            elif status == 'n':
                task.mark_incomplete()
            save_tasks(tasks)
            print("任务已更新")
        else:
            print("无效的任务编号")
    except ValueError:
        print("请输入有效的任务编号！")


def remove_task(tasks):
    """删除任务"""
    if not tasks:
        print("没有任务可供删除")
        return

    try:
        task_id = int(input("请输入要删除的任务编号: ")) - 1
        if 0 <= task_id < len(tasks):
            task = tasks[task_id]
            print(f"删除任务: {task}")
            del tasks[task_id]
            save_tasks(tasks)
            print("任务已删除")
        else:
            print("无效的任务编号")
    except ValueError:
        print("请输入有效的任务编号！")


def display_tasks(tasks):
    """显示任务统计信息"""

    # print(f"总任务数：{len(tasks)}")
    # print(f"已完成任务数：{TaskUtils.count_completed_tasks(tasks)}")
    # print(f"未完成任务数：{TaskUtils.count_incomplete_tasks(tasks)}\n")
    """美化任务列表的显示"""
    if not tasks:
        print("没有任务")
        return

    print("\n任务信息统计：")
    print("=" * 50)
    for index, task in enumerate(tasks, 1):
        status = "\033[92m完成\033[0m" if task.completed else "\033[91m未完成\033[0m"
        print(f"{str(index).ljust(3)} | {task.name.ljust(30)} | {status}")
    print("=" * 50)

def display_task_stats(tasks):
    """显示任务统计信息"""
    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)
    incomplete = total - completed
    print("\n任务统计")
    print("=" * 50)
    print(f"总任务数: {total}")
    print(f"已完成任务数: {completed}")
    print(f"未完成任务数: {incomplete}")
    print("=" * 50)
    # print(f"总任务数：{len(tasks)}")
    # print(f"已完成任务数：{TaskUtils.count_completed_tasks(tasks)}")
    # print(f"未完成任务数：{TaskUtils.count_incomplete_tasks(tasks)}\n")
    # """美化任务列表的显示"""
    # if not tasks:
    #     print("没有任务")
    #     return
    #
    # print("\n任务信息统计：")
    # print("=" * 50)
    # for index, task in enumerate(tasks, 1):
    #     status = "\033[92m完成\033[0m" if task.completed else "\033[91m未完成\033[0m"
    #     print(f"{str(index).ljust(3)} | {task.name.ljust(30)} | {status}")
    # print("=" * 50)

# def ds(tasks):
#     print("-"*30)
#     print(f"任务名称：{tasks[0].name}")
#     print("-" * 30)
