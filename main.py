def on_button_pressed_a():
    basic.show_string("" + str((input.temperature())))
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("" + str((input.light_level())))
    basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Temperature")
