import time

import pyglet

window = pyglet.window.Window(fullscreen=True, vsync=True)
fpsdisplay = pyglet.window.FPSDisplay(window=window)


@window.event
def on_draw():
    if 'old_time' in globals():
        new_time = time.time()
    else:
        global old_time
        old_time = time.time() - 0.02
        new_time = time.time()
    delta_t = new_time - old_time
    old_time = time.time()
    window.clear()
    fpsdisplay.draw()


pyglet.app.run()