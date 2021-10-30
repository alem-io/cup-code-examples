# cup-code-examples

This repository contains base code examples in different languages for reading game engine data.

The process is straightforward, input data is read into variables. Based on input values, program
should output one of allowed commands, e.g. `UP`, `DOWN`, etc.

## Input format

Given, four number `W`, `H`, `P`, `T`.

- `W` width
- `H` height
- `P` player id
- `T` tick number

Then, `H` lines of strings each of width `W` are given to identify the map.
Each tile of map contains one of chars:

- `!` is wall
- `.` is empty
- `b` is bonus
- `d` is dagger

Then, `N` lines of entities are listed. Each line contains the following format:
`p or m` - `p` is for player and `m` is for monster. Then the id of the entity `i` is given.
For the monsters the id is not important and can be ignored.

Next two numbers indicate `x` and `y`, i.e. coordinates on the map. Last numbers define
presence of the features for the given entity: first number is for `bonus`, second for the `dagger`.

Example

```
13 11 1 1
.............
.!.!.!.!.!.!.
.............
.!.!.!.!.!.!.
.............
.!.!.!.!.!.!.
.............
.!.!.!.!.!.!.
.............
.!.!.!.!.!.!.
.............
4
p 1 0 0 0 0
m 0 3 6 0 0
m 0 8 4 0 0
p 2 12 10 0 0
```

Explanation

Map of width `13` and of height `11`. Your player id is `1` and current tick is number `1`.
Then, `11` lines of map with walls and empty fields only.
`4` entities are being listed:

1. `p`, i.e. player, with id `#1` is on `x:0, y:0` coordinates and has `no bonus`, `no dagger`.
2. `m`, i.e. monster is on `x:3, y:6`.
3. `m`, i.e. monster is on `x:8, y:4`.
4. `p`, i.e. player, with id `#2` is on `x:12, y:10` coordinates and has `no bonus`, `no dagger`.

## Languages

Following languages are available:

- [c](./c)
- [cpp](./cpp)
- [csharp](./csharp)
- [go](./go)
- [java](./java)
- [js](./js)
- [kotlin](./kotlin)
- [pascal](./pascal)
- [php](./php)
- [python](./python)
- [ruby](./ruby)
