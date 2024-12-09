from migen import *
from migen.build.generic_platform import *
from migen.build.platforms import icebreaker

# Define LED pins
_io = [
    ("LED1", 0, Pins("PMOD2:1"), IOStandard("LVCMOS33")),
    ("LED2", 0, Pins("PMOD2:2"), IOStandard("LVCMOS33")),
    ("LED3", 0, Pins("PMOD2:4"), IOStandard("LVCMOS33")),
    ("LED4", 0, Pins("PMOD2:5"), IOStandard("LVCMOS33")),
    ("LED5", 0, Pins("PMOD2:0"), IOStandard("LVCMOS33"))
]

class LEDTest(Module):
    def __init__(self, platform):

        counter = Signal(26)
        self.sync += counter.eq(counter + 1)

        led0 = platform.request("LED1", 0)
        led1 = platform.request("LED2", 0)
        led2 = platform.request("LED3", 0)
        led3 = platform.request("LED4", 0)
        led4 = platform.request("LED5", 0)

        # Sequentially light up LEDs
        self.comb += [
            led0.eq(counter[25]),
            led1.eq(~counter[25]),
            led2.eq(~counter[25]),
            led3.eq(counter[25]),
            led4.eq(counter[25])
        ]

# Use iCEBreaker platform
platform = icebreaker.Platform()
platform.add_extension(_io)
platform.build(LEDTest(platform))
