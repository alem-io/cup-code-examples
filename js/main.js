const getnextline = require('getnextline');

while (true) {
  let width, height, player_id, tick;
  let line = getnextline();
  [width, height, player_id, tick] = line.split(" ").map(val => parseInt(val))

  for (let i = 0; i < height; i++) {
    let map_row = getnextline();
  }

  let n = parseInt(getnextline());

  for (let i = 0; i < n; i++) {
    let line = getnextline();
    line = line.split(' ')
    let ent_type = line[0]
    let p_id = parseInt(line[1])
    let x = parseInt(line[2])
    let y = parseInt(line[3])
    let param1 = parseInt(line[4])
    let param2 = parseInt(line[5])
  }

  console.error("debug code");

  const actions = ["left", "up", "bomb", "stay", "right", "down"];
  const random_index = Math.floor(Math.random() * 6);
  console.log(actions[random_index])
}
