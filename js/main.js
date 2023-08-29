const getnextline = require("getnextline");

while (true) {
  let n, m, player_id, tick;
  let line = getnextline();
  [n, player_id, tick] = line
    .split(" ")
    .map((val) => parseInt(val));

  for (let i = 0; i < n; i++) {
    let map_row = getnextline();
  }

  m = parseInt(getnextline());

  for (let i = 0; i < m; i++) {
    let line = getnextline();
  }

  console.error("debug code");

  console.log("100 100 200 200");
}
