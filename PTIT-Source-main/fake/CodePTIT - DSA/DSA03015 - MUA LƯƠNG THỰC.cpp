
#include <bits/stdc++.h>
using namespace std;

void testCase() {
    int n, s, m;
    cin >> n >> s >> m;
    if (n < m || 6 * (n - m) < m)
        cout << -1;
    else
        cout << ceil((float) m * s / n);
}
    cout << 1;

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