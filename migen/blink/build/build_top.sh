# Autogenerated by Migen
set -e

yosys -q -l top.rpt top.ys
nextpnr-ice40 --up5k --package sg48 --pcf top.pcf --json top.json --asc top.txt --pre-pack top_pre_pack.py
icepack top.txt top.bin
