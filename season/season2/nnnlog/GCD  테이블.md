# GCD  테이블
https://www.acmicpc.net/problem/12972

## 풀이
첫번째, g_{ij}에서 i = j라면, g_{ij} = A_i이므로 원래 수열의 값은 항상 GCD 테이블에 있다.

두번째, 임의의 두 수, a와 b에 대해서, min(a, b) >= gcd(a, b)이다.

따라서, gcd 테이블에서 가장 큰 값 중 하나는 원래 수열의 값이 된다.

원래 수열에서 가장 큰 값을 A라고 하고, 두번째로 큰 수를 B라고 하자.

gcd(A, B)를 하더라도 여전히, B보다 작거나 같으므로 gcd 테이블에서 두번째로 큰 수가 B가 됨을 알 수 있다.

gcd(A, B)를 gcd table에서 2번 제거해준다. 왜냐하면, 두 값의 gcd로 나온 값은 순서가 바꾸어 두번 나오기 때문이다.

위 작업을 반복해서 대충 해주면 항상 i번째 시점에서 i번째로 큰 수열의 원소를 구할 수 있다.

## 코드
```cpp
#include <bits/stdc++.h>

#define all(v) v.begin(), v.end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ld> vld;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<pld> vpld;
typedef unordered_map<int, int> mpii;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	cin >> n;
	multiset<int, greater<>> s;
	for (int i = 0; i < n * n; i++) {
		int a;
		cin >> a;
		s.insert(a);
	}

	vi vec;
	for (int i = 0; i < n; i++) {
		int top = *s.begin();
		s.erase(s.begin());
		
		for (const auto &j : vec) {
			int g = gcd(j, top);
			s.erase(s.find(g));
			s.erase(s.find(g));
		}
		vec.push_back(top);
	}

	for (const auto &i : vec) cout << i << " ";
}

```
