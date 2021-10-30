#include <iostream>

using namespace std;

int main() {
    while (true) {
        int h, w, player_id, tick;
        cin >> w >> h >> player_id >> tick;

        cerr << w << h << player_id << tick << endl;

        // read map
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                char c;
                cin >> c;
            }
        }

        // number of entities
        int n;
        cin >> n;

        cerr << "n:" << n << endl;

        // read entities
        for (int i = 0; i < n; i++) {
            string type;
            int p_id, x, y, param_1, param_2;

            cin >> type >> p_id >> x >> y >> param_1 >> param_2;
            cerr << type << p_id << x << y << param_1 << param_2 << endl;
        }

        // use `cerr` to print for debugging
        cerr << "debug code" << endl;

        // this will choose one of random actions
        const string actions[] = {"left", "right", "up", "down", "bomb"};
        int random_index = rand() % 5;

        // bot action
        cout << actions[random_index] << endl;
    }

    return 0;
}
