
program cup;
	uses 
		Classes,
		StrUtils,
		SysUtils;

	var 
		line: string;
		n, m, playerID, tick: integer;
		i: integer;
begin

	while true do
		begin
			ReadLn(n, playerID, tick);
			for i := 1 to n do
				begin
					ReadLn(line);
				end;
			ReadLn(m);
			for i := 1 to m do
				begin
					ReadLn(line);
				end;

			WriteLn(StdErr, 'Debug Code');
			
			WriteLn("100 100 200 200");
			Flush(Output);
		end;
end.
