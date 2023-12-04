#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

///for odd palindromes
vector<int> m1_func(string &s) {
    int l = 0, r = -1;
    vector<int> m(s.size(), 0);
    for (int i = 0; i < s.size(); ++i) {
        int k = (i > r) ? 0 : min(m[l + r - i], r - i + 1);
        while (i + k < s.size() && i - k >= 0 && s[i + k] == s[i - k]) {
            ++k;
        }
        m[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }

    return m;
}

///for even palindromes
vector<int> m2_func(string &s) {
    int l = 0, r = -1;
    vector<int> m(s.size(), 0);
    for (int i = 0; i < s.size(); ++i) {
        int k = (i > r) ? 0 : min(m[l + r - i + 1], r - i + 1);
        while (i + k < s.size() && i - k - 1 >= 0 && s[i + k] == s[i - k - 1]) {
            ++k;
        }
        m[i] = k;
        if (i + k - 1 > r) {
            l = i - k;
            r = i + k - 1;
        }
    }
    return m;
}

///Example of usage
int main() {
    string s;
    cin >> s;
    vector<int> m1 = m1_func(s);
    vector<int> m2 = m2_func(s);
    int sum = 0;
    for(int i = 0; i < s.size(); i++)
        sum += m1[i] + m2[i];
    cout << sum;
    return 0;
}