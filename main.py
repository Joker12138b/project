# -*- coding: UTF-8 -*- #
"""
@filename:main.py
@author:cxt
@time:2025-01-04
"""
from utils.helper import *

def main():
    # 书写一个函数进行输出   无返回值
    print_welcome()

    # 加载任务数据
    task = load_tasks()

    while True:
        display_tasks(task)
        display_task_stats(task)
        # ds(task)
        print("\n菜单")
        print("1. 添加任务")
        print("2. 编辑任务")
        print("3. 删除任务")
        print("4. 添加子任务")
        print("5. 退出")
        choice = input("请选择操作: ")
        if choice == '1':
            add_task(task)
        elif choice == '2':
            edit_task(task)
        elif choice == '3':
            remove_task(task)
        elif choice == '4':
            add_subtask(task)
        elif choice == '4':
            print_separator("再见!")
            save_tasks(task)
            break
        else:
            print("无效的选择，请重新输入")


if __name__ == '__main__':
    main()
