/* Machine-generated using Migen */
module top(
	output LED1,
	output LED2,
	output LED3,
	output LED4,
	output LED5,
	input clk12
);

reg [25:0] counter = 26'd0;
wire sys_clk;
wire sys_rst;
wire por_clk;
reg int_rst = 1'd1;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign LED1 = counter[25];
assign LED2 = (~counter[25]);
assign LED3 = (~counter[25]);
assign LED4 = counter[25];
assign LED5 = counter[25];
assign sys_clk = clk12;
assign por_clk = clk12;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	counter <= (counter + 1'd1);
	if (sys_rst) begin
		counter <= 26'd0;
	end
end

endmodule
