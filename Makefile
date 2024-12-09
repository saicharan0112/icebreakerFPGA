# Makefile to install icestorm binaries along with the base and side packages

install: system icestorm nextpnr yosys

system:
	sudo apt-get install << packages.txt

icestorm: 
	git clone https://github.com/YosysHQ/icestorm.git icestorm
	cd icestorm
	make -j$(nproc)
	sudo make install
	cd ../


nextpnr:
	git clone https://github.com/YosysHQ/nextpnr nextpnr
	cd nextpnr
	make -j$(nproc)
	sudo make install
	cd ../

yosys:
	git clone https://github.com/YosysHQ/yosys.git yosys
	cd yosys
	make -j$(nproc)
	sudo make install
	cd ../