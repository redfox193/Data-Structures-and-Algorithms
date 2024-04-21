#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

long long def = 0;

//segtree for operation sum on l..r and adding value by index i
struct segtree
{
    int sz = 1;
    vector <long long> operations;
    vector <long long> sums;

    void init(int n)
    {
        while(sz < n)
            sz *= 2;
        operations.assign(2 * sz, 0);
        sums.assign(2 * sz, 0);
    }

    long long build(vector <long long> &v, int x, int lx, int rx)
    {
        if(rx - lx == 1)
            if(lx < v.size())
                return operations[x] = v[lx];
            else
                return operations[x];
        int m = (lx + rx) / 2;
        long long s1 = build(v, 2 * x + 1, lx, m);
        long long s2 = build(v, 2 * x + 2, m, rx);
        return operations[x] = s1 + s2;
    }

    void build(vector <long long> &v)
    {
        init(v.size());
        build(v, 0, 0, sz);
    }

    void addv(int l, int r, long long &v, int x, int lx, int rx)
    {
        if(rx <= l || lx >= r)
            return;
        if(lx >= l && rx <= r)
        {
            operations[x] += v;
            sums[x] += v * (rx - lx);
            return;
        }
        int m = (lx + rx) / 2;
        addv(l, r, v, x * 2 + 1, lx, m);
        addv(l, r, v, x * 2 + 2, m, rx);
        sums[x] = sums[2 * x + 1] + sums[2 * x + 2] + operations[x] * (rx - lx);
        return;
    }

    void addv(int l, int r, long long  v)
    {
        addv(l, r, v, 0, 0, sz);
    }

    long long getsum(int l, int r, int x, int lx, int rx)
    {
        if(rx <= l || lx >= r)
            return 0;
        if(lx >= l && rx <= r)
            return sums[x];
        int m = (lx + rx) / 2;
        long long m1 = getsum(l, r, 2 * x + 1, lx, m);
        long long m2 = getsum(l, r, 2 * x + 2, m, rx);
        return m1 + m2 + operations[x] * (min(rx, r) - max(lx, l));
    }

    long long getsum(int l, int r)
    {
        long long sum = getsum(l, r, 0, 0, sz);
        return sum;
    }
};

int main()
{
    int n, m;
    cin >> n >> m;
    segtree st;
    st.init(n);
    while(m--)
    {
        int t, a, b, c;
        cin >> t >> a >> b;
        if(t == 1)
        {
            cin >> c;
            st.addv(a, b, c);
        }
        else
        {
            cout << st.getsum(a, b) << endl;
        }
    }
    return 0;
}
