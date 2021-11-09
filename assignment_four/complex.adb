with Ada.Text_IO; use Ada.Text_IO;

package body complex is 
	procedure show (number_one: number; number_two: number) is
	begin 
		Put_Line("Number One: ");
		Put_Line("Real: " & Integer'Image(number_one.real));
		Put_Line("Imaginary: " & Integer'Image(number_one.imaginary));
		Put_Line("Number Two: ");
		Put_Line("Real: " & Integer'Image(number_two.real));
		Put_Line("Imaginary: " & Integer'Image(number_two.imaginary));
	end show;
	procedure add (number_one: number; number_two: number) is
	begin
		Put_Line("Real: " & Integer'Image(number_one.real + number_two.real) & " Imaginary: " & Integer'Image(number_one.imaginary + number_two.imaginary));
	end add;

	procedure subtract (number_one: number; number_two: number) is
	begin
		Put_Line("Real: " &Integer'Image(number_one.real - number_two.real)& " Imaginary: " & Integer'Image(number_one.imaginary - number_two.imaginary));
	end subtract;
	
	procedure multiply (number_one: number; number_two: number) is
	begin
		Put_Line("Real: " &Integer'Image(number_one.real * number_two.real)& " Imaginary: " & Integer'Image(number_one.imaginary * number_two.imaginary));
	end multiply;

	procedure divide (number_one: number; number_two: number) is
	begin
		Put_Line("Real: " &Float'Image(Float(number_one.real) / Float(number_two.real))& " Imaginary: " & Float'Image(Float(number_one.imaginary) / Float(number_two.imaginary)));
	end divide;
end complex;
