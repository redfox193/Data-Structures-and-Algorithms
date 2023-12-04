#include <iostream>
#include <vector>

using namespace std;

void floyd_warshall(vector< vector<long long> > &dist, long long inf) {
    for (int k = 0; k < dist.size(); k++) {
        for (int i = 0; i < dist.size(); i++) {
            for (int j = 0; j < dist.size(); j++) {
                if (dist[i][k] != inf && dist[k][j] != inf && (dist[i][k] + dist[k][j] < dist[i][j] || dist[i][j] == inf)) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

int main() {
    int n, s, f;
    cin >> n >> s >> f;

    vector<std::vector<long long>> dist(n, std::vector<long long>(n));
    vector<std::vector<long long>> ans(n, std::vector<long long>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> dist[i][j];
            ans[i][j] = dist[i][j];
        }
    }

    floyd_warshall(ans, -1);

    cout << ans[s][f];

    return 0;
}
//6 2 6
//0 -1 1 -1 -1 -1
//1 0 -1 4 2 -1
//-1 -1 0 1 -1 -1
//-1 -1 -1 0 -1 2
//-1 -1 -1 -1 0 4
//-1 -1 -1 -1 -1 0
