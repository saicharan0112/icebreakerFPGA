from migen import *
from migen.build.generic_platform import *
from migen.build.platforms import icebreaker

# Define LED pins
_io = [
    ("LED0", 0, Pins("PMOD2:0"), IOStandard("LVCMOS33")),
    ("LED1", 0, Pins("PMOD2:1"), IOStandard("LVCMOS33")),
    ("LED2", 0, Pins("PMOD2:2"), IOStandard("LVCMOS33")),
    ("LED3", 0, Pins("PMOD2:4"), IOStandard("LVCMOS33")),
    # ("LED5", 0, Pins("PMOD2:5"), IOStandard("LVCMOS33")),
    # ("BTN1", 0, Pins("PMOD2:7"), IOStandard("LVCMOS33")),
    # ("BTN2", 0, Pins("PMOD2:6"), IOStandard("LVCMOS33")),
    # ("BTN3", 0, Pins("PMOD2:3"), IOStandard("LVCMOS33"))
    ("BTN0", 0, Pins("PMOD1A:0"), IOStandard("LVCMOS33")),
    ("BTN1", 0, Pins("PMOD1A:1"), IOStandard("LVCMOS33")),
    ("BTN2", 0, Pins("PMOD1A:2"), IOStandard("LVCMOS33")),
    ("BTN3", 0, Pins("PMOD1A:3"), IOStandard("LVCMOS33")),
    # ("BTN4", 0, Pins("PMOD1A:4"), IOStandard("LVCMOS33")),
    # ("BTN5", 0, Pins("PMOD1A:5"), IOStandard("LVCMOS33")),
    # ("BTN6", 0, Pins("PMOD1A:6"), IOStandard("LVCMOS33")),
    # ("BTN7", 0, Pins("PMOD1A:7"), IOStandard("LVCMOS33"))
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


class BTNTest(Module):
    def __init__(self, platform):
        
        led0 = platform.request("LED0", 0)
        pmod1 = platform.request("BTN1", 0)
        pmod2 = platform.request("BTN2", 0)
        pmod3 = platform.request("BTN3", 0)
        self.sync += [
            If(pmod1[0] & pmod2[0] & pmod3[0], led0.eq(1)),
            If(~pmod1[0] & ~pmod2[0] & ~pmod3[0], led0.eq(0))
        ]


class BTNLED(Module):
    def __init__(self, platform):
        
        led0 = platform.request("LED0", 0)
        led1 = platform.request("LED1", 0)
        led2 = platform.request("LED2", 0)
        led3 = platform.request("LED3", 0)
        pmod0 = platform.request("BTN0", 0)
        pmod1 = platform.request("BTN1", 0)
        pmod2 = platform.request("BTN2", 0)
        pmod3 = platform.request("BTN3", 0)
        # pmod4 = platform.request("BTN4", 0)
        # pmod5 = platform.request("BTN5", 0)
        # pmod6 = platform.request("BTN6", 0)
        # pmod7 = platform.request("BTN7", 0)

        self.sync += [
            If(pmod0[0] , led0.eq(0)),
            If(~pmod0[0] , led0.eq(1)),
            
            If(pmod1[0] , led1.eq(0)),
            If(~pmod1[0] , led1.eq(1)),
            
            If(pmod2[0] , led2.eq(0)),
            If(~pmod2[0] , led2.eq(1)),
            
            If(pmod3[0] , led3.eq(0)),
            If(~pmod3[0] , led3.eq(1)),
            # If(pmod1[0] & pmod2[0] & pmod3[0], led0.eq(1)),
            # If(pmod1[0] & pmod2[0] & pmod3[0], led0.eq(1)),
            # If(~pmod1[0] & ~pmod2[0] & ~pmod3[0], led0.eq(0))
        ]



# Use iCEBreaker platform
platform = icebreaker.Platform()
platform.add_extension(_io)
platform.build(BTNLED(platform))
