# -*- coding: UTF-8 -*- #
"""
@filename:task_utils.py
@author:cxt
@time:2025-01-07
"""
from task import Task

class TaskUtils:
    @staticmethod
    def count_completed_tasks(tasks):
        """ 统计已完成的任务数量 """
        return sum([1 for task in tasks if task.completed])

    @staticmethod
    def count_incomplete_tasks(tasks):
        """ 统计未完成的任务数量 """
        return sum([1 for task in tasks if not task.completed])

    @classmethod
    def create_sample_tasks(cls):
        """ 类方法：创建一些示例任务 """
        return [Task("任务1"), Task("任务2", True), Task("任务3")]