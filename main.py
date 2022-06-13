radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        if (auto == 0) {
            if (obstacl == 0) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, VITESSE)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 30)
                basic.pause(10)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            }
        }
    }
    if (receivedNumber == 1) {
        if (auto == 0) {
            if (obstacl == 0) {
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, VITESSE)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
                basic.pause(10)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            }
        }
    }
    if (receivedNumber == 4) {
        if (auto == 0) {
            if (obstacl == 0) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 70)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 70)
                basic.pause(10)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 0)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 0)
            }
        }
    }
    if (receivedNumber == 2) {
        if (VITESSE > 100) {
            VITESSE = VITESSE + 20
        }
    }
    if (receivedNumber == 3) {
        if (true) {
            VITESSE = VITESSE - 20
        }
    }
    if (receivedNumber == 4) {
        if (auto == 0) {
            auto = 1
        } else {
            auto = 0
        }
    }
})
input.onGesture(Gesture.LogoUp, function () {
    while (input.isGesture(Gesture.LogoUp)) {
        radio.sendNumber(4)
        basic.pause(10)
    }
})
input.onButtonPressed(Button.A, function () {
    while (input.buttonIsPressed(Button.A)) {
        radio.sendNumber(3)
        basic.pause(10)
    }
})
input.onGesture(Gesture.TiltRight, function () {
    while (input.isGesture(Gesture.TiltRight)) {
        radio.sendNumber(1)
        basic.pause(10)
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    while (input.isGesture(Gesture.TiltLeft)) {
        radio.sendNumber(0)
        basic.pause(10)
    }
})
input.onButtonPressed(Button.AB, function () {
    while (input.buttonIsPressed(Button.AB)) {
        radio.sendNumber(4)
        basic.pause(10)
    }
})
input.onButtonPressed(Button.B, function () {
    while (input.buttonIsPressed(Button.B)) {
        radio.sendNumber(2)
        basic.pause(10)
    }
})
input.onGesture(Gesture.LogoDown, function () {
    while (input.isGesture(Gesture.LogoDown)) {
        radio.sendNumber(0)
        radio.sendNumber(1)
        basic.pause(10)
    }
})
let obstacl = 0
let auto = 0
let VITESSE = 0
radio.setGroup(1)
VITESSE = 150
basic.forever(function () {
    if (auto == 1) {
        while (auto == 1) {
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
                maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)
            }
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 150)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 30)
            }
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 30)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 150)
            }
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)
            }
        }
    }
    while (auto == 0) {
        if (IR.IR_read() == 1) {
            obstacl = 1
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 150)
            basic.pause(1000)
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 0)
            obstacl = 0
        }
    }
})
