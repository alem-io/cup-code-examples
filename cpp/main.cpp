#include <iostream>

using namespace std;

int main() {
    while (true) {
        int n, m, player_id, tick;
        string str;
        cin >> n >> player_id >> tick;

        cerr << n << player_id << tick << endl;

        // read cities
        for (int i = 0; i < n; i++) {
            getline(cin, str);
        }

        // number of entities
        cin >> m;

        cerr << "m:" << m << endl;

        // read entities
        for (int i = 0; i < m; i++) {
            string type;
            getline(cin, str);
        }

        // use `cerr` to print for debugging
        cerr << "debug code" << endl;

        // this will choose one of random actions
        cout << "100 100 200 200\n";
        fflush(stdout);
    }

    return 0;
}
