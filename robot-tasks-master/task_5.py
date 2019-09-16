#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    for i in range(9):
        if wall_is_beneath():
            move_right(1);
        
if __name__ == '__main__':
    run_tasks()
