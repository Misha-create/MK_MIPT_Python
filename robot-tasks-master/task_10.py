#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
        while wall_is_on_the_right()==False:
            if wall_is_above() or wall_is_beneath():
                fill_cell()
            move_right(1)
        if wall_is_above() or wall_is_beneath():
            fill_cell() 


if __name__ == '__main__':
    run_tasks()
