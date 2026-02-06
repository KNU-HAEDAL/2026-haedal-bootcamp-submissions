#include <bits/stdc++.h>
using namespace std;

bool cmp(const pair<int, string>& a, const pair<int, string>& b) {
	return a.first < b.first;
}

int main() {
    string name;
    int n, age; cin >> n;
    vector<pair<int, string>> person(n);

    for (int i = 0; i < n; i++) {
        cin >> person[i].first >> person[i].second;
    }

    stable_sort(person.begin(), person.end(), cmp);

    for (auto iter : person) {
        cout << iter.first << " " << iter.second << "\n";
    }
}