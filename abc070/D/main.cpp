#include <bits/stdc++.h>
using namespace std;


void solve(long long N, std::vector<long long> a, std::vector<long long> b, std::vector<long long> c, long long Q, long long K, std::vector<long long> x, std::vector<long long> y){

}

// Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    long long N;
    scanf("%lld",&N);
    std::vector<long long> a(N-1);
    std::vector<long long> b(N-1);
    std::vector<long long> c(N-1);
    for(int i = 0 ; i < N-1 ; i++){
        scanf("%lld",&a[i]);
        scanf("%lld",&b[i]);
        scanf("%lld",&c[i]);
    }
    long long Q;
    scanf("%lld",&Q);
    long long K;
    scanf("%lld",&K);
    std::vector<long long> x(Q);
    std::vector<long long> y(Q);
    for(int i = 0 ; i < Q ; i++){
        scanf("%lld",&x[i]);
        scanf("%lld",&y[i]);
    }
    solve(N, std::move(a), std::move(b), std::move(c), Q, K, std::move(x), std::move(y));
    return 0;
}
