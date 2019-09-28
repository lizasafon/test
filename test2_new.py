from graphics import *


def draw_tree(posx, posy, height=130, width=20, crown_rad=50, crown_color='green', branch_color='brown'):
    branch = Polygon(Point(posx - width / 2, posy), Point(posx + width / 2, posy),
                     Point(posx + width / 2, posy - height), Point(posx - width / 2, posy - height))
    branch.setFill(branch_color)
    branch.setOutline(branch_color)

    crown = Circle(Point(posx, posy - height), crown_rad)
    crown.setFill(crown_color)
    crown.setOutline(crown_color)

    branch.draw(win)
    crown.draw(win)


def draw_sun(pos=(0, 0)):
    sun = Circle(Point(*pos), 50)
    sun.setFill('yellow')
    sun.setOutline('yellow')
    sun.draw(win)

def draw_cloud(p1, p2, color='white'):
    cloud = Oval(Point(*p1), Point(*p2))
    cloud.setFill(color)
    cloud.setOutline(color)
    cloud.draw(win)


def prepare():
    sky = Polygon(Point(0, 0), Point(0, 648), Point(1152, 648), Point(1152, 0))
    sky.setFill("#c0c0c0")
    sky.setOutline("#c0c0c0")
    grass = Polygon(Point(0, 648), Point(1152, 648), Point(1152, 448), Point(0, 448))
    grass.setFill("#008000")
    grass.setOutline("#008000")

    sky.draw(win)
    grass.draw(win)

    draw_cloud((30, 300), (350, 180), 'white')
    draw_cloud((300, 50), (520, 10), 'white')
    draw_cloud((800, 80), (1130, 200), 'white')

    draw_sun()



def draw_house(left_down_corner, length, height, roof_color='#C6865C', frame_color='#8B1212',
               window_color='#99D9EA', door_color='#C6865C', door_hand_color='black', door_window_orientation=1, door_hand_orientation=1):
    ldk = left_down_corner
    l = length
    h = height

    frame = Rectangle(Point(ldk[0], ldk[1] - h), Point(ldk[0] + l, ldk[1]))
    frame.setFill(frame_color)
    frame.setOutline('black')

    roof = Polygon(Point(ldk[0], ldk[1] - h), Point(ldk[0] + l, ldk[1] - h), Point(ldk[0] + 0.5 * l, ldk[1] - 3 * h / 2))
    roof.setFill(roof_color)
    roof.setOutline(roof_color)

    posx = ldk[0] + 2.5 / 5 * l + door_window_orientation * 1.5 / 5 * l
    window = Circle(Point(posx, ldk[1] - 11 / 18 * h), l / 6)
    window.setFill(window_color)
    window.setOutline(window_color)

    posx = ldk[0] + 2.5 / 7 * l - door_window_orientation * 1.5 / 7 * l
    door = Rectangle(Point(posx, ldk[1] - 22 * h / 29), Point(posx + 2 / 7 * l, ldk[1]))
    door.setFill(door_color)
    door.setOutline(door_color)

    deltax = 0.25 / 7 * l
    if door_hand_orientation == -1:
        deltax = (2 - 0.25) / 7 * l
    door_hand = Circle(Point(posx + deltax, ldk[1] - h /3), l / 60)
    door_hand.setOutline('black')
    door_hand.setFill(door_hand_color)

    frame.draw(win)
    roof.draw(win)
    window.draw(win)
    door.draw(win)
    door_hand.draw(win)

win = GraphWin("risunok", 1152, 648)
prepare()
draw_house((500, 570), 250, 190, door_hand_color='#87f0f8')
draw_house((200, 520), 200, 160, window_color='#148d02', roof_color='#ee9f34', door_color='#8d5202')
draw_house((800, 520), 150, 100, window_color='#8d0285', roof_color='#8d5202')


draw_house((950, 140), 70, 50, window_color='#148d02', roof_color='#ee9f34')
draw_house((850, 120), 70, 50, roof_color='#8d5202')
draw_house((900, 170), 70, 50, window_color='#8d0285', door_color='#8d5202', door_hand_color='#87f0f8')


draw_tree(100, 500)







win.getMouse()

win.close()