#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <queue>
#define lengthof(x) (sizeof(x) / sizeof(*(x)))

using namespace std;

int MOD = 998244353;
int N, S;
int cache[3000+1][3000+1];
int A[3000+1];

int f(int s, int i) {
  if(s < 0) {
    return 0;
  }
  if(i == N) {
    if(s == 0) {
      return 1;
    }
    return 0;
  }
  if(cache[i][s] != -1) {
    return cache[i][s];
  }
  cache[i][s] = (2 * f(s, i+1) % MOD + f(s-A[i], i+1)) % MOD;
  return cache[i][s];
}

int main(){
  std::fill((int*) cache, (int*) (cache + lengthof(cache)), -1);
  cin >> N >> S;
  for(int i = 0; i < N; ++i){
    cin >> A[i];
  }
  cout << f(S, 0) << endl;
  return 0;
}
