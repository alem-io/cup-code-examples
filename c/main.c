#include <stdio.h>
#include <stdlib.h>

int main(void) {
  while (1) {
    int n, player_id, tick;
    scanf("%d%d%d\n", &n, &player_id, &tick);

    // read cities
    for (int i = 0; i < n; i++) {
      char *line = NULL;
      size_t len = 0;
      ssize_t lineSize = 0;
      lineSize = getline(&line, &len, stdin);
      free(line);
    }

    // number of movements
    int m;
    scanf("%d\n", &m);

    // read movements
    for (int i = 0; i < m; i++) {
      char *line =NULL;
      size_t len = 0;
      ssize_t lineSize = 0;
      lineSize = getline(&line, &len, stdin);
      free(line);
    }

    // use fprintf(stderr, ...) to print for debugging
    fprintf(stderr, "debug code\n");

    // bot action
    printf("100 100 200 200\n");
    fflush(stdout);
  }

  return 0;
}
