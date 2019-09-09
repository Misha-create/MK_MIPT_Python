#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    i = True
    while i:
        fill_cell()
        while wall_is_on_the_right() == False:
            move_right(1)
            fill_cell()
        if wall_is_beneath() == False:
            move_down(1)
            fill_cell()
            while wall_is_on_the_left() == False:
                move_left(1)
                fill_cell()
        else:
            i = False
    while wall_is_on_the_left() == False:
         move_left(1)            
    
if __name__ == '__main__':
    run_tasks()
