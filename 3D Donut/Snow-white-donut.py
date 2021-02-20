from vpython import *

canvas(background= color.purple)
donut = ring(radius=0.5, thickness=0.25, color=vector(400, 100, 1))
flavor = ring(radius=0.55, thickness=0.25, color=vector(255, 255, 255))
rad = 0

while True:
    rate(10)
    donut.pos = vector(5*cos(rad), sin(rad), 0)
    flavor.pos = vector(5*cos(rad), sin(rad), 0)
    rad = rad + 0.05
