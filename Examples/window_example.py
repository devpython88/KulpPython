# import the game window class and color class and Key class
from Kulp.kulp import GameWindow, Color, Key

# initialize window (background and fps are optional) (background is black by default
# and fps is 60 by default)
window = GameWindow("Window Title", (800, 400), background_color=Color.WHITE, fps=24)


# These functions are essential but optional
@window.on_update
def update():
    # This func is called every frame
    ...


@window.on_key
def key(k: str):
    # this func is called when a key is pressed (the arg is the key)
    # examples
    if k == Key.char("w"):  # for character keys
        ...

    elif k == Key.TAB:  # for special keys (there are others in the class)
        ...


# show the window
window.start()
