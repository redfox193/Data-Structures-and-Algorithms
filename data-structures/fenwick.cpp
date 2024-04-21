#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

//Notes
//time complexity to proccess request - O(log n)
//time complexity to change element - O(log n)
//space complexity - O(n)

//fenwick tree for sum
//let v[0..n-1] - our array
//let t[0..n-1] - array of sums, where t_i = sum of v_j for all v_j : F(i) <= j <= i



int F(int x) {
    return x & (x + 1);
}

int H(int x) {
    return x | (x + 1);
}

//get sum [0..r]
int sum (int r, vector<int> &t)
{
    int result = 0;
    for (; r >= 0; r = F(r) - 1)
        result += t[r];
    return result;
}

//update t[i] after incrementing v[i] by x
void inc (int i, int x, vector<int> &t)
{
    for (; i < t.size(); i = H(i))
        t[i] += x;
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    vector<int> t(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
        inc(i, v[i], t);
    }
    for(int i = 0; i < n; i++)
        cout << t[i] << " ";
    cout << endl;
    for(int i = 0; i < n; i++)
        cout << sum(i, t) << " ";
    return 0;
}