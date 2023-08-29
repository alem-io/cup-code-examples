<?php
    while (1) {
        fscanf(STDIN, "%d %d %d\n", $n, $player_id, $tick);
        for ($x = 0; $x < $n; $x++) {
            $line = trim(fgets(STDIN));
        }
        fscanf(STDIN, "%d\n", $m);
        for ($x = 0; $x < $m; $x++) {
            $line = trim(fgets(STDIN));
        }
        fwrite(STDERR, "debug code" . PHP_EOL);
        
        echo "100 100 200 200" . PHP_EOL;
    }
?>
