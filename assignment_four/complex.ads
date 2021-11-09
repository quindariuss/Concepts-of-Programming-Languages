package complex is 
	type number is record
		real:		Integer;
		imaginary:	Integer;
	end record;

	procedure show (number_one: number; number_two: number);
	procedure add (number_one: number; number_two: number);
	procedure subtract (number_one: number; number_two: number);
	procedure multiply (number_one: number; number_two: number);
	procedure divide (number_one: number; number_two: number);
end complex;
