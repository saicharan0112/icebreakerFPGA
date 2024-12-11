from migen import *
from migen.build.platforms import icebreaker
from migen.build.generic_platform import Pins, Subsignal,IOStandard  # Correct imports


_io = [
    ("uart", 0,
     Subsignal("tx", Pins("PMOD1A:1")),  # TX pin
     Subsignal("rx", Pins("PMOD1A:2")),  # RX pin
     IOStandard("LVCMOS33")),
    ("user_led0", 0 , Pins("PMOD2:0"), IOStandard("LVCMOS33")),
    ("user_led1", 0 , Pins("PMOD2:1"), IOStandard("LVCMOS33")),
]


class UART(Module):
    def __init__(self, platform, sys_clk_freq, baud_rate):
        # UART Pins
        uart_pins = platform.request("uart")

        # Baud rate generator
        baud_gen = BaudRateGenerator(sys_clk_freq, baud_rate)
        self.submodules += baud_gen

        # RX Signal
        uart_rx = Signal()

        # Synchronize RX pin with baud clock
        self.sync += [
            If(baud_gen.tick,
                uart_rx.eq(uart_pins.rx)
            )
        ]

        # Monitor RX activity with LED
        self.comb += platform.request("user_led0").eq(uart_rx)


class BaudRateGenerator(Module):
    def __init__(self, sys_clk_freq, baud_rate):
        self.tick = Signal()  # Pulses once per baud period

        # Calculate clock divider
        divider = int(sys_clk_freq // baud_rate)
        counter = Signal(max=divider)

        # Clock divider logic
        self.sync += [
            If(counter == 0,
                counter.eq(divider - 1),
                self.tick.eq(1)  # Generate a pulse
            ).Else(
                counter.eq(counter - 1),
                self.tick.eq(0)
            )
        ]


class SimpleUARTTx(Module):
    def __init__(self, platform):
        uart_pins = platform.request("uart")
        counter = Signal(104)
        self.sync += [
            If(counter == 0,
                uart_pins.tx.eq(1),  # Send idle state
                counter.eq(120)      # Adjust for baud rate timing
            ).Else(
                counter.eq(counter - 1)
            )
        ]
        
        self.comb += platform.request("user_led0").eq(uart_pins.rx)
        self.comb += platform.request("user_led1").eq(uart_pins.tx)


class TXTest(Module):
    def __init__(self, platform):
        uart_pins = platform.request("uart")
        counter = Signal(24)  # Slow down toggling for visibility
        self.sync += [
            counter.eq(counter + 1),
            uart_pins.tx.eq(counter[-1])  # Toggle TX with MSB of counter
        ]
        self.comb += platform.request("user_led0").eq(uart_pins.tx)
        self.comb += platform.request("user_led1").eq(uart_pins.rx)


class UARTLoopback(Module):
    def __init__(self, platform):
        uart_pins = platform.request("uart")
        self.comb += uart_pins.tx.eq(uart_pins.rx)  # Simple loopback

        # Debug LEDs
        self.comb += [
            platform.request("user_led0").eq(uart_pins.rx),  # Monitor RX
            platform.request("user_led1").eq(uart_pins.tx),  # Monitor TX
        ]


# Build Platform
platform = icebreaker.Platform()
platform.add_extension(_io)

dut = TXTest(platform)
platform.build(dut)
