
#include <bits/stdc++.h>
using namespace std;

void tower(int n, char a, char b, char c) {
    if (n == 1) {
        cout << a << " -> " << c << endl;
        return;
    }
    tower(n - 1, a, c, b);
    tower(1, a, b, c);
    tower(n - 1, b, a, c);
    cout << 1;
}

void testCase() {
    int n; cin >> n;
    tower(n, 'A', 'B', 'C');
    // Số lượng | Nguồn | Trung gian | Đích
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T = 1;
    while (T--) {
        testCase();
        cout << "\n";
    }
    return 0;
}