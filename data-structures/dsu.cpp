#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

void make_dsu(int x, vector <int> &v)
{
    v[x] = x;
}

int find_dsu(int x, vector <int> &v)
{
    if(v[x] == x)
        return x;
    vector <int> t;
    while(v[x] != x)
    {
        t.push_back(x);
        x = v[x];
    }
    for(int i : t)
        v[i] = x;
    return x;
}

/// use random!!!
void union_dsu(int x, int y, vector <int> &v)
{
    int px = find_dsu(x, v);
    int py = find_dsu(y, v);
    if(rand() % 2 == 0)
        swap(px, py);
    v[px] = py;
}