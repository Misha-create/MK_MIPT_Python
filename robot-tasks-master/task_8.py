#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while(wall_is_beneath()!=wall_is_above()) and(wall_is_above()==False or wall_is_beneath()==False):
        move_right()

if __name__ == '__main__':
    run_tasks()
