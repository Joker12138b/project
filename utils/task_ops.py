# -*- coding: UTF-8 -*- #
"""
@filename:task_ops.py
@author:cxt
@time:2025-01-11
@function: 任务操作
"""
from task import Task, SubTask
from utils.file_ops import save_tasks

def add_task(tasks):
    """添加任务"""
    # tasks.append({"name": name, "completed": False})
    # save_tasks(tasks)
    #     print("任务名称不能为空")
    # task_name = input("请输入任务名称: ")
    # new_task = {"name": task_name, "completed": False}
    # tasks.append(new_task)
    # save_tasks(tasks)
    # while True:
    task_name = input("请输入任务名称: ")
    tags = input("请输入任务标签（以逗号分隔）：").split(",")
    tags = [tag.strip() for tag in tags if tag.strip()]
    task = Task(task_name, tags=tags)
    tasks.append(task)
    print(f"任务'{task_name}'已添加, 标签: {', '.join(tags) if tags else []}")
    save_tasks(tasks)

        # if task_name.strip():
        #     new_task = Task(task_name)
        #     tasks.append(new_task)
        #     save_tasks(tasks)
        #     print(f"任务'{task_name}'已添加")
        #     break
        # else:
        #     print("任务名称不能为空")


def search_by_tag(tasks):
    """按标签搜索任务"""
    tag = input("请输入要搜索的标签: ").strip()
    matching_tasks = [task for task in tasks if tag in task.tags]

    if matching_tasks:
        print(f"包含标签'{tag}'的任务:")
        for task in matching_tasks:
            status = input("任务是否完成? (y/n): ").strip().lower()
            if status == 'y':
                task.mark_completed()
            elif status == 'n':
                task.mark_incomplete()
            save_tasks(tasks)
            print(task)
    else:
        """进行添加标签"""
        print(f"没有找到标签 '{tag}' 的任务。")
        try:
            num = int(input("请输入任务编号: "))
            if 1 <= num <= len(tasks):
                task = tasks[int(num) - 1]
                status = input("任务是否完成? (y/n): ").strip().lower()
                if status == 'y':
                    task.mark_completed()
                elif status == 'n':
                    task.mark_incomplete()
                save_tasks(tasks)
                print(task)
                print(f"当前任务: {task}")

                # 输入任务的标签并更新
                tags = input("请输入任务标签（以逗号分隔）：").split(",")
                tags = [tag.strip() for tag in tags if tag.strip()]
                task.tags.update(tags)
                save_tasks(tasks)
            else:
                print("无效的任务编号")
        except ValueError:
            print("请输入有效的任务编号！")


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


def add_subtask(tasks):
    """添加子任务"""
    if not tasks:
        print("任务列表为空  无法添加")
        return

    print("\n选择一个父任务：")
    for index, task in enumerate(tasks, 1):
        print(f"{index}.{task}")

    try:
        parent_id = int(input("请输入父任务编号: ")) - 1
        if 0 <= parent_id < len(tasks):
            parent_task = tasks[parent_id]
            subtask_name = input("请输入子任务名称: ")
            new_subtask = SubTask(subtask_name, parent_task)
            tasks.append(new_subtask)
            save_tasks(tasks)
            print(f"子任务'{subtask_name}'已添加")
        else:
            print("无效的任务编号")
    except ValueError:
        print("请输入有效的任务编号！")
