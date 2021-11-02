
program cup;
	uses 
		Classes,
		StrUtils,
		SysUtils;

	var 
		line: string;
		w, h, playerID, tick: integer;
		n: integer;
		actions: array[0..5] of string;
		random_index: integer;
		i: integer;
begin

	while true do
		begin
			ReadLn(w, h, playerID, tick);
			for i := 1 to h do
				begin
					ReadLn(line);
				end;
			ReadLn(n);
			for i := 1 to n do
				begin
					ReadLn(line);
				end;

			WriteLn(StdErr, 'Debug Code');
			
			actions[0] := 'left';
			actions[1] := 'right';
			actions[2] := 'up';
			actions[3] := 'down';
			actions[4] := 'stay';

			random_index := Random(5);

			WriteLn(actions[random_index]);
			Flush(Output);
		end;
end.
