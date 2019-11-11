
from init import  *
from gun_class import *
from targe_tclass import *
def new_game(event=''):
    #управляет пушкой, целью, снарядами
    global balls
    g1 = gun()
    t = target()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    t.live = 1
    while t.live or balls:
        t.move()
        for b in ballss:
            b.move()
            if b.hittest(t) and t.live:
                t.live = 0
                t.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(canv.create_text(400, 300, text='', font='28'), text='Вы уничтожили цель за ' + str(g1.bullets_num) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
new_game()
mainloop()
