/* Machine-generated using Migen */
module top(
	output reg LED0,
	output reg LED1,
	output reg LED2,
	output reg LED3,
	input BTN0,
	input BTN1,
	input BTN2,
	input BTN3,
	input clk12
);

wire sys_clk;
wire sys_rst;
wire por_clk;
reg int_rst = 1'd1;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign sys_clk = clk12;
assign por_clk = clk12;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	if (BTN0) begin
		LED0 <= 1'd0;
	end
	if ((~BTN0)) begin
		LED0 <= 1'd1;
	end
	if (BTN1) begin
		LED1 <= 1'd0;
	end
	if ((~BTN1)) begin
		LED1 <= 1'd1;
	end
	if (BTN2) begin
		LED2 <= 1'd0;
	end
	if ((~BTN2)) begin
		LED2 <= 1'd1;
	end
	if (BTN3) begin
		LED3 <= 1'd0;
	end
	if ((~BTN3)) begin
		LED3 <= 1'd1;
	end
	if (sys_rst) begin
		LED0 <= 1'd0;
		LED1 <= 1'd0;
		LED2 <= 1'd0;
		LED3 <= 1'd0;
	end
end

endmodule
