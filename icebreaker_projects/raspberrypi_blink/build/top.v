/* Machine-generated using Migen */
module top(
	input gpio_in,
	output user_led,
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

assign user_led = gpio_in;
assign sys_clk = clk12;
assign por_clk = clk12;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

endmodule
