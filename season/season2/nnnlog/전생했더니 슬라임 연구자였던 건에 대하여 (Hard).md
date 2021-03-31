# 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
https://www.acmicpc.net/problem/14698

## 풀이
i, j번째 슬라임을 합성하면 A_i * A_j인 슬라임이 만들어지며, 비용에도 A_i * A_j가 곱해집니다.

곰셈에서 답을 최소화하려면, 매순간 가장 작은 슬라임만 선택해주면 됩니다.

문제는 합성한 슬라임을 "적절한" 위치에 넣어주어야 하는데, 이는 우선순위큐를 사용하면 logN에 삽입할 수 있습니다.

에너지가 2 * 10^18이므로, 답은 long long int의 범위를 충분히 넘어갈 수 있으므로, 매번 곱할 때마다 mod 연산을 하여 오버플로에 조심해야 합니다.

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

std::ostream&
operator<<( std::ostream& dest, __int128_t value )
{
	std::ostream::sentry s( dest );
	if ( s ) {
		__uint128_t tmp = value < 0 ? -value : value;
		char buffer[ 128 ];
		char* d = std::end( buffer );
		do
		{
			-- d;
			*d = "0123456789"[ tmp % 10 ];
			tmp /= 10;
		} while ( tmp != 0 );
		if ( value < 0 ) {
			-- d;
			*d = '-';
		}
		int len = std::end( buffer ) - d;
		if ( dest.rdbuf()->sputn( d, len ) != len ) {
			dest.setstate( std::ios_base::badbit );
		}
	}
	return dest;
}

typedef __int128 i128;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int T; cin >> T;
	while (T--) {
		int n; cin >> n;
		i128 ans = 1;
		priority_queue<i128, vector<i128>, greater<>> pq;
		while (n--) {
			ll a; cin >> a;
			pq.push(a);
		}
		while (pq.size() > 1) {
			i128 a = pq.top(); pq.pop();
			i128 b = pq.top(); pq.pop();
			ans *= a * b;
			ans %= 1000000007;
			pq.push(a * b);
		}
		cout << ans << "\n";
	}
}

```
