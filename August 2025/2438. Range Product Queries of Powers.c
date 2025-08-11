/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007

long long modPow(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int* productQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int powers[32]; // max 32 bits needed since n <= 1e9
    int count = 0;
    for (int bit = 0; bit < 32; bit++) {
        if (n & (1LL << bit)) {
    powers[count++] = (int)(1LL << bit);
        }
    }

    // Step 2: Precompute prefix products
    long long prefixProd[32];
    prefixProd[0] = powers[0] % MOD;
    for (int i = 1; i < count; i++) {
        prefixProd[i] = (prefixProd[i - 1] * powers[i]) % MOD;
    }

    // Step 3: Answer queries
    *returnSize = queriesSize;
    int* ans = (int*)malloc(sizeof(int) * queriesSize);

    for (int i = 0; i < queriesSize; i++) {
        int l = queries[i][0];
        int r = queries[i][1];
        if (l == 0) {
            ans[i] = (int)prefixProd[r];
        } else {
            long long inv = modPow(prefixProd[l - 1], MOD - 2); // modular inverse
            ans[i] = (int)((prefixProd[r] * inv) % MOD);
        }
    }

    return ans;
}
