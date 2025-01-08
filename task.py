# -*- coding: UTF-8 -*- #
"""
@filename:task.py
@author:cxt
@time:2025-01-07
"""
class Task:
    def __init__(self, name, completed=False):
        """初始化任务的名臣和完成状态"""
        self.name = name
        self.completed = completed

    def __str__(self):
        """ 定义任务的字符串表示 """
        return f"{self.name} - 状态: {'完成' if self.completed else '未完成'}"

    def to_edit(self):
        """将任务转化为字典"""
        return {
            "name": self.name,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, task_dict):
        """从字典中创建任务"""
        return cls(task_dict["name"], task_dict["completed"])

    def mark_completed(self):
        """ 标记任务为完成"""
        self.completed = True

    def mark_incomplete(self):
        """ 标记任务为完成"""
        self.completed = False

class SubTask(Task):
    """ 子任务类  继承自Task """
    def __init__(self, name, parent_task, completed=False):
        super().__init__(name, completed)  # 调用父类的初始化方法
        self.parent_task = parent_task  # 关联的父任务

    def __str__(self):
        """ 定义子任务的字符串表示 """
        return f"子任务: {self.name}, 属于: {self.parent_task.name}, 状态: {'完成' if self.completed else '未完成'}"