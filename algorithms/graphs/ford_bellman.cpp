#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct edge
{
    int u, v, w;
};

void ford_bellman(vector<edge> &edges, int start, vector<int> &dist, vector<int> &pred) {
    dist[start] = 0;

    for(int i = 0; i < dist.size() - 1; i++)
        for(auto& e: edges)
            if(dist[e.v] > dist[e.u] + e.w) {
                dist[e.v] = dist[e.u] + e.w;
                pred[e.v] = e.u;
            }
}

///return in reverse order
void find_negative_contour(vector<edge> &edges, vector<int>& dist, vector<int>& pred, queue<int>& contour) {
    int ind = -1;

    for(auto& e: edges)
        if(dist[e.v] > dist[e.u] + e.w) {
            ind = e.v;
            break;
        }

    if(ind == -1)
        return;

    vector<int> vis(dist.size());
    while (pred[ind] != -1 && !vis[ind]) {
        vis[ind] = 1;
        contour.push(ind);
        ind = pred[ind];
    }
    while(contour.front() != ind)
        contour.pop();
}

///Example of usage
int main() {
    int n, m;
    cin >> n >> m;
    vector<edge> edges(m);
    for(int i = 0; i < m; i++)
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    vector<int> dist(n, 1000);
    vector<int> pred(n, -1);
    ford_bellman(edges, 0, dist, pred);
    for(auto& d: dist)
        cout << d << " ";
    cout << "\n";
    for(auto& pr: pred)
        cout << pr << " ";
    cout << "\n";
    queue<int> contuor;
    find_negative_contour(edges, dist, pred, contuor);
    if(contuor.empty())
        cout << "no negative contuor";
    else
        while(!contuor.empty()) {
            cout << contuor.front() << " ";
            contuor.pop();
        }
    return 0;
}
//5 6
//0 1 1
//2 1 0
//0 2 1
//3 4 2
//3 2 1
//1 3 -2
