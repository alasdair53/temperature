input.onButtonPressed(Button.A, function () {
    basic.showString("" + (input.temperature()))
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (input.lightLevel()))
    basic.showArrow(ArrowNames.South)
})
basic.showString("Temperature")
