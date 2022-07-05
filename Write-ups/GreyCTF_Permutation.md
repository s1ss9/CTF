# Permutation

## CATEGORY

Crypto

## Challenge

n!

MD5 (permutation.zip) = e7920324a0db237e1860f98be5846bb2

mechfrog88

[Challenge File](./Resources/permutation.zip)

## Solution

**Note:** As a beginner in Crypto, my method of solving is rather basic. Check out a more advanced and shorter [solution here.](https://ariana1729.github.io/writeups/2022/GreyCTF/Permutation/2022-06-10-Permutation.html) 

Although $g^i$ can be any of $n!$ lists (permutations), **each element** in $g^i$ cycles through some subset of 
$\\{0,1\cdots, n-1\\}$ 
with a cycle length at most $n$, when $i$ increases from $0$. ( e.g. 12341234... is a cycle of length 4)


## Proof

The above can be proved by considering the following ([relevant interesting video](https://youtu.be/iSNsgj1OCLA?t=660)):

> The multiplication by $g$ is equivalent to an one-to-one mapping function (i.e. has inverse). 
> 
> Multiplication  is `x[i] = x[g[i]]`. 
> 
> Inverse is `x[i] = x[g.index(i)]`. 

So let's look at any single elment, say the one at index 0. Let the following be the sequence of values it take when multiplied by $g$, starting from $g^1[0] = g[0]$.

$$
g[0]\to g^2[0]=g[g[0]] \to\cdots\to g^n[0]\to g^{n+1}[0]
$$

Since any element can only take integer value in $\[0, n-1\]$, there must exist some $1\leq a\< b\leq n+1$ such that $g^{a}[0]=g^b[0]$. (by pigeonhole)

$$
g[0]\to\cdots\to g^a[0] \to\cdots\to g^b[0] \to\cdots
$$

Using the inverse property highlighted above, because $g[0]=(g^{1-a}g^a)[0]$ (take inverse $a-1$ times on $g^a[0]$),

we obtain:

$$
g^{b-a+1}[0]=(g^{1-a}g^b)[0] = (g^{1-a}g^a)[0] = g[0]
$$

which indicates a cycle of length $b-a$ which is $g[0] \cdots g^{b-a}[0]$. 

## Solution (Continued)

So we go through $2n$ iterations ($g^1,\cdots ,g^{2n+1}$) and find the first and second time any element of $g^i$ is same as the given $B$. In this way we obtain $n$ simultaneous linear congruence equations about $b$,  which can easily be solved using Chinese Remainder Theorem.

> iteration count of first match -> remainders
>
> iteration count of second match - iteration count of first match -> cycle length

Use CRT to compute $b$ (modulo values are the cycle lengths).

Compute key $S=A^b$ and run the encrypt function on the ciphertext to reverse it (as it uses XOR). 

## Flag

grey{DLP_Is_Not_Hard_In_Symmetric_group_nzDwH49jGbdJz5NU}
