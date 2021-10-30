#include <stdio.h>
#include <stdlib.h>

int main(void) {
  while (1) {
    int h, w, player_id, tick;
    scanf("%d%d%d%d", &w, &h, &player_id, &tick);

    // read map
    for (int i = 0; i < h; i++) {
      char line[w + 1];
      scanf("%s", line);
    }

    // number of entities
    int n;
    scanf("%d", &n);
    getchar();

    // read entities
    for (int i = 0; i < n; i++) {
      char ent_type;
      int p_id, x, y, param_1, param_2;

      scanf("%c%d%d%d%d%d", &ent_type, &p_id, &x, &y, &param_1, &param_2);
      getchar();
    }

    // use fprintf(stderr, ...) to print for debugging
    fprintf(stderr, "debug code\n");

    // this will choose one of random actions
    const char actions[][10] = {"left", "right", "up", "down", "bomb"};
    int random_index = rand() % 5;

    // bot action
    printf("%s\n", actions[random_index]);
    fflush(stdout);
  }

  return 0;
}
