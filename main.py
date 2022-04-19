def on_received_number(receivedNumber):
    global VITESSE
    if receivedNumber == 0:
        servos.P0.set_stop_on_neutral(True)
        servos.P0.run(VITESSE)
        basic.pause(10)
        servos.P0.set_stop_on_neutral(False)
    if receivedNumber == 1:
        servos.P1.set_stop_on_neutral(True)
        servos.P1.run(VITESSE)
        basic.pause(10)
        servos.P1.set_stop_on_neutral(False)
    if receivedNumber == 4:
        servos.P0.set_stop_on_neutral(True)
        servos.P1.set_stop_on_neutral(True)
        servos.P0.run(-40)
        servos.P1.run(-40)
        basic.pause(10)
        servos.P0.set_stop_on_neutral(False)
        servos.P1.set_stop_on_neutral(False)
    if receivedNumber == 2:
        if VITESSE > 100:
            VITESSE = VITESSE + 5
    if receivedNumber == 3:
        if True:
            VITESSE = VITESSE - 10
radio.on_received_number(on_received_number)

def on_gesture_logo_up():
    while input.is_gesture(Gesture.LOGO_UP):
        radio.send_number(4)
        basic.pause(10)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_right():
    while input.is_gesture(Gesture.TILT_RIGHT):
        radio.send_number(1)
        basic.pause(10)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    while input.is_gesture(Gesture.TILT_LEFT):
        radio.send_number(0)
        basic.pause(10)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_down():
    while input.is_gesture(Gesture.LOGO_DOWN):
        radio.send_number(0)
        radio.send_number(1)
        basic.pause(10)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

VITESSE = 0
radio.set_group(1)
VITESSE = 30