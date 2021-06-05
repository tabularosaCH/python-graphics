from graphics import *
from time import sleep

from graphics import *
from time import sleep


def face():
    # GraphWin(title, width, height)
    win = GraphWin("Human Face", 500, 500, autoflush=False)
    # color max 255
    win.setBackground(color_rgb(210, 112, 180))

    # Oval(top left point1, bottom right point2)
    # face outline
    o = Oval(Point(190, 150), Point(340, 380))
    o.setOutline('black')
    o.setWidth(3)
    o.draw(win)

    # left eye, x is width(30) and y is height(26)
    eye1 = Oval(Point(225, 240), Point(255, 212))
    eye1.setOutline('black')
    eye1.setWidth(1)
    eye1.setFill('black')
    eye1.draw(win)
    # left eye, pupil
    c1 = Circle(Point(245, 225), 8)
    c1.setFill('blue')
    c1.setWidth(3)
    c1.draw(win)
    # left eyebrow x_left boarder(5), x_width(30)
    line1 = Line(Point(220, 205), Point(255, 205))
    line1.draw(win)
    line1.setWidth(5)
    line1.setOutline('black')

    # right eye, x boarder(-35) and y (keep same height for leveling)
    eye2 = Oval(Point(275, 240), Point(305, 212))
    eye2.setOutline('black')
    eye2.setWidth(1)
    eye2.setFill('black')
    eye2.draw(win)
    # right eye, pupil
    c2 = Circle(Point(290, 225), 8)
    c2.setFill('blue')
    c2.setWidth(3)
    c2.draw(win)
    # right eyebrow x_right boarder(-30), x_width(-30)
    line2 = Line(Point(275, 205), Point(310, 205))
    line2.draw(win)
    line2.setWidth(5)
    line2.setOutline('black')

    # nose length
    line3 = Line(Point(265, 230), Point(290, 275))
    line3.draw(win)
    line3.setWidth(1)
    line3.setOutline('black')
    # nose tip
    line3 = Line(Point(265, 275), Point(290, 275))
    line3.draw(win)
    line3.setWidth(1)
    line3.setOutline('black')

    # mouth
    o2 = Oval(Point(225, 300), Point(310, 315))
    o2.setOutline('red3')
    o2.setWidth(2)
    o2.draw(win)
    o2.setFill('black')

    # tear drops left_eye 1
    c3 = Circle(Point(245, 245), 4)
    c3.setFill('blue')
    c3.setOutline('white')
    c3.setWidth(2)
    c3.draw(win)
    # tear drops left_eye 2
    c4 = Circle(Point(245, 250), 4)
    c4.setFill('blue')
    c4.setOutline('white')
    c4.setWidth(2)
    c4.draw(win)
    # tear drops left_eye 3
    c5 = Circle(Point(245, 263), 4)
    c5.setFill('blue')
    c5.setOutline('white')
    c5.setWidth(2)
    c5.draw(win)
    # tear drops left_eye 4
    c6 = Circle(Point(245, 267), 4)
    c6.setFill('blue')
    c6.setOutline('white')
    c6.setWidth(2)
    c6.draw(win)

    # teardrops move down by 20
    for i in range(80):
        c4.move(0, 20)
        time.sleep(.03)
        win.update()
    for i in range(80):
        c5.move(0, 20)
        time.sleep(.03)
        win.update()
    for i in range(80):
        c6.move(0, 20)
        time.sleep(.03)
        win.update()

    win.close()


face()
