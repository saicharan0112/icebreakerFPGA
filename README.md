# icebreakerFPGA

### FPGA device

I am using iCEBreaker FPGA [https://1bitsquared.com/collections/fpga/products/icebreaker](https://1bitsquared.com/collections/fpga/products/icebreaker) and a usb 2.0 cable to program it from my machine.


### Installation and Testing

`make install` intends to install system packages, yosys, nextpnr and icestorm binaries.

The `icebreaker/` folder contains the files required to test the "hello world" version of FPGA. Before flashing the binary to FPGA, add the below content to this file.

**File** - `/etc/udev/rules.d/53-lattice-ftdi.rules`

**Content** - `ACTION=="add", ATTR{idVendor}=="0403", ATTR{idProduct}=="6010", MODE:="666"`

Now go inside the icebreaker directory `make prog` to create binary and to flash on to the FPGA respectively.

You can run `make clean` to remove all generated files in the process, and run `make all` to create them again or if you want to start over with the updated verilog file.



