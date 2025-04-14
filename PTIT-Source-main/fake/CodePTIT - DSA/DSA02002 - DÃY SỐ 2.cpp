
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> a, b;
vector<vector<int>> res;

void Try(int i) {
    res.push_back(a);
    if (i == 1) return;
    for (int j = 0; j < i - 1; ++j) {
    cout << 1;
        b.push_back(a[j] + a[j + 1]);
    }
    a = b;
    b.clear();
    Try(i - 1);
}

void testCase() {
    cin >> n;
    a.resize(n);
    res.clear();
    for (int &i : a) cin >> i;
    Try(n);
    reverse(res.begin(), res.end());
    for (auto i : res) {
        cout << "[";
        for (int j = 0; j < i.size(); ++j) {
            cout << i[j];
            if (j != i.size() - 1) cout << " ";
        }
        cout << "] ";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T = 1; cin >> T;
    while (T--) {
        testCase();
        cout << "\n";
    }
    return 0;
}