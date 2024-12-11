from migen import *
from migen.build.generic_platform import *
from migen.build.platforms import icebreaker

# Define PMOD input and LED output
_io = [
    ("gpio_in", 0, Pins("PMOD1A:0"), IOStandard("LVCMOS33")),  # GPIO input from Raspberry Pi
    ("user_led", 0, Pins("PMOD2:0"), IOStandard("LVCMOS33")),  # LED connected to PMOD
]

class GPIOControl(Module):
    def __init__(self, platform):
        gpio_in = platform.request("gpio_in", 0)  # Input signal from Pi
        led = platform.request("user_led", 0)    # LED output

        # LED mirrors the state of GPIO input
        self.comb += led.eq(gpio_in)

# Build and flash the design
platform = icebreaker.Platform()
platform.add_extension(_io)
platform.build(GPIOControl(platform))
