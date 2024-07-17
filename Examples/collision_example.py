# import the game window class and color class and Key class
from Kulp.kulp import GameWindow, Color, Key
# import kulp GFX
from Kulp.kulp_gfx import Rectangle

# initialize window (background and fps are optional) (background is black by default
# and fps is 60 by default)
window = GameWindow("Window Title", (800, 400), background_color=Color.WHITE, fps=24)

# the rectangle to draw
rect = Rectangle(10, 20, 50, 50, Color.RED)  # (x, y, width, height, color)

# the rect for collision
rect2 = Rectangle(10, 200, 50, 50, Color.BLACK)  # use the w key to move and collide with this rect


# These functions are essential but optional
@window.on_update
def update():
    # This func is called every frame
    # draw the rectangle
    # if an error occurs, Try adding `global rect` at this function's start
    window.draw_rect(rect)
    window.draw_rect(rect2)

    # collision
    if rect.collides(rect2):
        ...  # do something on collision


@window.on_key
def key(k: str):
    # this func is called when a key is pressed (the arg is the key)
    # examples
    if k == Key.char("w"):  # for character keys
        # example movement
        # if an error occurs, Try adding `global rect` at this function's start
        rect.y += 10

    elif k == Key.TAB:  # for special keys (there are others in the class)
        ...


# show the window
window.start()
