#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    def treangle(x,y):
        step=y
        r=0
        while step >1:
            step-=2
            r+=1
        if x == 1:
            current_lvl=y
            for i in range(y-1):
                print(i)
                if current_lvl == 1:
                    move_right(1)
                    fill_cell()
                    move_up(r)
                    move_right(int((y-1)/2))
                    break    
                move_right(1)
                fill_cell()
                for t in range(current_lvl-1):
                    move_right(1)
                    fill_cell()
                move_left(current_lvl-1)
                move_down(1)
                current_lvl-=2
        if x == 2:
            current_lvl=y
            for i in range(y-1):
                print(i)
                if current_lvl == 1:
                    move_up(1)
                    fill_cell()
                    move_left(r)
                    move_up(int((y-1)/2))
                    break    
                move_up(1)
                fill_cell()
                for t in range(current_lvl-1):
                    move_up(1)
                    fill_cell()
                move_down(current_lvl-1)
                move_right(1)
                current_lvl-=2
        if x == 3:
            current_lvl=y
            for i in range(y-1):
                print(i)
                if current_lvl == 1:
                    move_left(1)
                    fill_cell()
                    move_down(r)
                    move_left(int((y-1)/2))
                    break    
                move_left(1)
                fill_cell()
                for t in range(current_lvl-1):
                    move_left(1)
                    fill_cell()
                move_right(current_lvl-1)
                move_up(1)
                current_lvl-=2
        if x == 4:
            current_lvl=y
            for i in range(y-1):
                print(i)
                if current_lvl == 1:
                    move_down(1)
                    fill_cell()
                    move_right(r)
                    move_down(int((y-1)/2))
                    break    
                move_down(1)
                fill_cell()
                for t in range(current_lvl-1):
                    move_down(1)
                    fill_cell()
                move_up(current_lvl-1)
                move_left(1)
                current_lvl-=2
    length = 0
    while wall_is_on_the_right() == False:
        length=length+1
        move_right(1)
    move_left(length)
    treangle(1,length-1)
    move_right(1)
    treangle(4,length-1)
    move_down(1)
    treangle(3,length-1)
    move_left(1)
    treangle(2,length-1)
    move_down(length-1)
if __name__ == '__main__':
    run_tasks()
