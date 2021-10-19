<?php
    while (1) {
        fscanf(STDIN, "%d %d %d %d\n", $width, $height, $player_id, $tick);
        for ($x = 0; $x < $height; $x++) {
            $line = trim(fgets(STDIN));
        }
        fscanf(STDIN, "%d\n", $n);
        for ($x = 0; $x < $n; $x++) {
            $line = trim(fgets(STDIN));
            $values = explode(" ", $line);
            $ent_type = $values[0];
            $pid = intval($values[1]);
            $x = intval($values[2]);
            $y = intval($values[3]);
            $param1 = intval($values[4]);
            $param2 = intval($values[5]);
        }
        fwrite(STDERR, "debug code" . PHP_EOL);
        
        $actions = ["left", "right", "up", "down", "bomb"];
        $random_index = random_int(0, 5);
        echo $actions[$random_index] . PHP_EOL;
    }
?>
