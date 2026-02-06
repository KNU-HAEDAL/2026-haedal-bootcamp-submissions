#include <bits/stdc++.h>
using namespace std;

int factori(int i) {
    if (i <= 1)
        return 1;
    return i*factori(i-1);
}

int main() {
    int n; cin >> n;
    long long result = factori(n);
    cout << result;
}