from Clock import Clock
import time

clock = Clock()

clock.lap("a")

time.sleep(0.2)

clock.lap("b")

time.sleep(0.1)

clock.lap("c")

clock.summary()