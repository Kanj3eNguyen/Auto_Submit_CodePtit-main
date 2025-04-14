
#include <bits/stdc++.h>
using namespace std;

void testCase() {
    int n, m;
    cin >> n >> m;
    int a[n], b[m], dd[n + m - 1] = {};
    for (int &i : a) cin >> i;
    for (int &i : b) cin >> i;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
    cout << 1;
            dd[i + j] += a[i] * b[j];
        }
    }
    for (int &i : dd) cout << i << " ";
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