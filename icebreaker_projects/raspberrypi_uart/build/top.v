/* Machine-generated using Migen */
module top(
	output reg uart_tx,
	input uart_rx,
	output user_led0,
	output user_led1,
	input clk12
);

reg [23:0] __main___counter = 24'd0;
wire sys_clk;
wire sys_rst;
wire por_clk;
reg platform_int_rst = 1'd1;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign user_led0 = uart_tx;
assign user_led1 = uart_rx;
assign sys_clk = clk12;
assign por_clk = clk12;
assign sys_rst = platform_int_rst;

always @(posedge por_clk) begin
	platform_int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	__main___counter <= (__main___counter + 1'd1);
	uart_tx <= __main___counter[23];
	if (sys_rst) begin
		uart_tx <= 1'd0;
		__main___counter <= 24'd0;
	end
end

endmodule
