from migen import *
from migen.genlib.fifo import SyncFIFO

class UART(Module):
    def __init__(self):
        # UART parameters
        self.tx = Signal()
        self.rx = Signal()
        
        # TX FIFO - 8-bit data, 8 entries depth
        self.tx_fifo = SyncFIFO(8, 8)  # 8-bit data, 8 entries depth
        
        # RX FIFO - 8-bit data, 8 entries depth
        self.rx_fifo = SyncFIFO(8, 8)
        
        # TX Path
        self.sync += [
            If(self.tx_fifo.readable,
                self.tx_fifo.rd.eq(1),  # Read the FIFO
                self.tx.eq(self.tx_fifo.dout)  # Output the data
            )
        ]
        
        # RX Path
        self.sync += [
            If(self.rx.ready,
                self.rx_fifo.write(self.rx.data)  # Write data to the RX FIFO
            )
        ]

    def send_message(self, message):
        for char in message:
            self.tx_fifo.write(ord(char))  # Write each character to the TX FIFO


uart = UART()
uart.send_message("hi Pi")