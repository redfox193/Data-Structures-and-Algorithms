#include <iostream>
#include <vector>
#include <set>
#include <queue>

using namespace std;

void dijkstra(vector< vector < pair<int, long long> > > &list, vector<long long> &dist, vector<int> &p, int start) {
    set<pair<long long, int>> heap;
    dist[start] = 0;
    heap.insert({dist[start], start});

    int u, v, w;
    while (!heap.empty()) {
        pair<long long, int> para = *heap.begin();
        heap.erase(heap.begin());
        u = para.second;

        for (int i = 0; i < list[u].size(); i++) {
            v = list[u][i].first;
            w = list[u][i].second;

            if (dist[v] > dist[u] + w) {
                heap.erase({dist[v], v});
                dist[v] = dist[u] + w;
                p[v] = u;
                heap.insert({dist[v], v});
            }
        }
    }
}

///when w is either a or b, O(n + m)
void ab_dijkstra(vector< vector < pair<int, long long> > > &list, vector<long long> &dist, vector<int> &p, int start, int a) {
    queue<int> qa;
    queue<int> qb;
    vector<int> vis(list.size());
    dist[start] = 0;
    vis[start] = 1;
    for (auto& e: list[start]){
        dist[e.first] = e.second;
        if(e.second == a)
            qa.push(e.second);
        else
            qb.push(e.second);
    }

    int u, v, w;
    while (!qa.empty() || !qb.empty() ) {
        if(qa.empty()) {
            u = qb.front();
            qb.pop();
        }
        else if(qb.empty()) {
            u = qa.front();
            qa.pop();
        }
        else {
            u = min(qa.front(), qb.front());
            if(qa.front() < qb.front())
                qa.pop();
            else
                qb.pop();
        }
        if(vis[u])
            continue;
        vis[u] = 1;
        for (int i = 0; i < list[u].size(); i++) {
            v = list[u][i].first;
            w = list[u][i].second;
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                p[v] = u;
                if(w == a)
                    qa.push(v);
                else
                    qb.push(v);
            }
        }
    }
}

///Example of usage
int main() {
    int n, s, f;
    cin >> n >> s >> f;
    s--;
    f--;
    vector<vector<pair<int, long long>>> v(n, vector<pair<int, long long>>());
    vector<int> p(n, -1);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            long long w;
            cin >> w;
            if (w >= 0)
                v[i].emplace_back(j, w);
        }
    vector<long long> dist(n, 1e10);
    dijkstra(v, dist, p, s);

    vector<int> way;
    if (dist[f] == 1e10) {
        cout << -1;
        return 0;
    }
    way.push_back(f + 1);
    while (p[f] != -1) {
        way.push_back(p[f] + 1);
        f = p[f];
    }
    for (int i = way.size() - 1; i >= 0; i--)
        cout << way[i] << " ";

    return 0;
}
//3 2 1
//0 1 1
//4 0 1
//2 1 0
//ans:
//2 3 1
