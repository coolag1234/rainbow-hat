from .i2c_bus import bus
from . import apa102
from .bmp280 import bmp280
from .alphanum4 import AlphaNum4
from .touch import Buttons
from .lights import Lights
from . import buzzer

display = AlphaNum4(i2c=bus)
display.begin()

touch = Buttons
lights = Lights
weather = bmp280(bus)
rainbow = apa102
