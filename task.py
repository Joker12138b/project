# -*- coding: UTF-8 -*- #
"""
@filename:task.py
@author:cxt
@time:2025-01-07
"""
class Task:
    def __init__(self, name, completed=False, tags=None):
        """初始化任务的名称和完成状态"""
        self.name = name
        self.completed = completed
        self.tags = set(tags) if tags else set()

    def __str__(self):
        """ 定义任务的字符串表示 """
        tags_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"任务名称: {self.name}, 状态: {'完成' if self.completed else '未完成'}, 标签: {tags_str}"

    @classmethod
    def to_edit(cls, task):
        """将任务转化为字典"""
        return {
            "name": task.name,
            "completed": task.completed,
            "tags": list(task.tags) if task.tags else []
        }

    @classmethod
    def from_dict(cls, task_dict):
        """从字典中创建任务"""
        return cls(task_dict["name"], task_dict["completed"], task_dict.get("tags", []))

    def add_tag(self, tag):
        """添加标签"""
        self.tags.add(tag)

    def remove_tag(self, tag):
        """删除标签"""
        self.tags.discard(tag)


    def to_dict(self):
        """将任务转化为字典"""
        return {
            "name": self.name,
            "completed": self.completed,
            "tags": list(self.tags)
        }

    @classmethod
    def from_dict(cls, task_dict):
        """从字典中创建任务"""
        return cls(task_dict["name"], task_dict["completed"], task_dict.get("tags", []))

    def mark_completed(self):
        """ 标记任务为完成"""
        self.completed = True

    def mark_incomplete(self):
        """ 标记任务为完成"""
        self.completed = False


"""主要是进行继承、重写、多态的学习"""
class SubTask(Task):
    """ 子任务类  继承自Task """
    def __init__(self, name, parent_task, completed=False):
        super().__init__(name, completed)  # 调用父类的初始化方法
        self.parent_task = parent_task  # 关联的父任务

    def __str__(self):
        """ 定义子任务的字符串表示 """
        return f"子任务: {self.name}, 属于: {self.parent_task.name}, 状态: {'完成' if self.completed else '未完成'}"

    @classmethod
    def to_edit(cls, task):
        """将子任务转化为字典格式"""
        task_dict = super().to_edit()
        task_dict["parent_task"] = cls.parent_task.name
        return task_dict
