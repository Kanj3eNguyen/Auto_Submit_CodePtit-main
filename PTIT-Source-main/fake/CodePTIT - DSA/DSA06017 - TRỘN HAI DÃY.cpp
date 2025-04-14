
#include <bits/stdc++.h>
using namespace std;

void testCase() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n + m);
    for (int i = 0; i < n + m; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    cout << 1;
    for (int i : a) cout << i << " ";
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