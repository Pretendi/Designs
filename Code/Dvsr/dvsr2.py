from math import sqrt

def prob501():
  def isqrt(n):
    if n <= 0:
      return 0

    x = int(sqrt(n) * (1 + 1e-12))
    while True:
      y = (x + n // x) >> 1
      if y >= x:
        return x
      x = y
  
  def icbrt(n):
    if n <= 0:
      return 0

    x = int(n ** (1. / 3.) * (1 + 1e-12))
    while True:
      y = (2 * x + n // (x * x)) // 3
      if y >= x:
        return x
      x = y

  def prime_sieve(N):
    if N < 2:
      return []

    size = (N + 1) // 2
    is_prime = [1] * size
    is_prime[0] = 0
    v = int(N ** 0.5) // 2 + 1
    for p in range(1, v):
      if not is_prime[p]:
        continue
      for k in range(2 * p * (p + 1), size, 2 * p + 1):
        is_prime[k] = 0

    primes = [2]
    primes.extend([2 * p + 1 for p in range(1, size) if is_prime[p]])
    return primes

  def tabulate_pis(N):
    if N <= 1:
      raise ValueError(N)
    v = int(N ** 0.5)
    smalls = [i - 1 for i in range(v + 1)]
    larges = [0 if i == 0 else N // i - 1 for i in range(v + 1)]

    for p in range(2, v + 1):
      if smalls[p - 1] == smalls[p]:
        continue

      p_cnt = smalls[p - 1]
      q = p * p
      end = min(v, N // q)
      for i in range(1, end + 1):
        d = i * p
        if d <= v:
          larges[i] -= larges[d] - p_cnt
        else:
          larges[i] -= smalls[N // d] - p_cnt
      for i in range(v, q - 1, -1):
        smalls[i] -= smalls[i // p] - p_cnt
    return smalls, larges

  N = 10 ** 12
  smalls, larges = tabulate_pis(N)

  ans = 0

  # p * q * r
  primes = prime_sieve(isqrt(N))
  for pi in range(smalls[icbrt(N)]):
    p = primes[pi]
    if p ** 3 >= N:
      break
    M = N // p
    for pj in range(pi + 1, smalls[isqrt(M)]):
      q = primes[pj]
      r = M // q
      ans += (smalls[r] if r < len(smalls) else larges[p * q]) - smalls[q]

  # p^3 * q
  for p in primes[:smalls[icbrt(N)]]:
    r = N // p ** 3
    if r <= 1:
      break
    ans += smalls[r] if r < len(smalls) else larges[p ** 3]

  # p^4
  ans -= smalls[isqrt(isqrt(N))]

  # p^7
  sth_root = int(pow(N, 1. / 7))
  while sth_root ** 7 <= N:
    sth_root += 1
  while sth_root ** 7 > N:
    sth_root -= 1
  ans += smalls[sth_root]
  print(ans)

prob501()
