while true do
    line = gets.chomp.split(" ")

    width = line[0].to_i
    height = line[1].to_i
    player_id = line[2].to_i
    tick = line[3].to_i

    (0..height - 1).each do |i|
        temp = gets.chomp
    end

    num_of_entities = gets.chomp.to_i

    (0..num_of_entities - 1).each do |i|
        line = gets.chomp.split(" ")
        ent_type = line[0]
        pID = line[1].to_i
        x = line[2].to_i
        y = line[3].to_i
        param1 = line[4].to_i
        param2 = line[5].to_i
    end

    STDERR.puts "Debug code"
    actions = ["left", "right", "up", "down", "stay"]
    
    STDOUT.puts actions[rand 6]
    STDOUT.flush
end