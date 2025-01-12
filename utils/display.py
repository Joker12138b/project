# -*- coding: UTF-8 -*- #
"""
@filename:display.py
@author:cxt
@time:2025-01-11
@function: 显示任务信息
"""
from utils.file_ops import load_tasks


def print_welcome():
    print_separator("欢迎使用任务管理系统")


def print_separator(title="", width=50):
    if title:
        print(f" {title} ".center(width, "-"))
    print("=" * width)


def format_task(index, task):
    """格式化任务信息"""
    status = "\033[92m完成\033[0m" if task.completed else "\033[91m未完成\033[0m"
    tag = task.tags or "无标签"
    return f"{str(index).ljust(3)} | {task.name.ljust(30)} | {status} | {tag}"


def display_tasks(tasks):
    if not tasks:
        print("没有任务")
        return
    print_separator("当前任务列表")
    for index, task in enumerate(tasks, 1):
        # status = "\033[92m完成\033[0m" if task.completed else "\033[91m未完成\033[0m"
        # print(f"{str(index).ljust(3)} | {task.name.ljust(30)} | {status}")
        print(format_task(index, task))
    print("=" * 50)


def display_task_stats(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)
    incomplete = total - completed
    print_separator("任务统计")
    print(f"总任务数：{total}")
    print(f"已完成任务：{completed}")
    print(f"未完成任务：{incomplete}")
    print("=" * 50)
