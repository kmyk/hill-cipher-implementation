#!/usr/bin/env python3
import numpy as np
import gmpy2
import math

def modinv(a_f, m):
    f = np.copy(a_f)
    assert isinstance(f, np.ndarray)
    assert isinstance(m, int)
    n = a_f.shape[0]
    g = np.identity(n, dtype=int)
    for i in range(n):
        for j in range(i+1,n):
            try:
                gmpy2.invert(int(f[j,i]), m)
                f[i], f[j] = np.copy(f[j]), np.copy(f[i])
                g[i], g[j] = np.copy(g[j]), np.copy(g[i])
                break
            except:
                pass
        inv = int(gmpy2.invert(int(f[i,i]), m))
        f[i] = f[i] * inv % m
        g[i] = g[i] * inv % m
        for j in range(n):
            if j != i:
                p = f[j,i]
                f[j] = (f[j] - f[i] * p) % m
                g[j] = (g[j] - g[i] * p) % m
    assert np.array_equal(f, np.identity(n, dtype=int))
    assert np.array_equal(a_f.dot(g) % m, np.identity(n, dtype=int))
    assert isinstance(g, np.ndarray)
    return g

stov = lambda s, alphabet: [alphabet.index(c) for c in s]
vtos = lambda x, alphabet: ''.join([alphabet[i] for i in x])

is_square = lambda n: int(math.sqrt(n)) ** 2 == n
chunk = lambda s, n: [s[i:i+n] for i in range(0, len(s), n)]

def encrypt(plaintext, alphabet, key):
    assert isinstance(plaintext, str)
    assert isinstance(alphabet, str)
    assert isinstance(key, str)
    m = len(alphabet) # modulo
    assert is_square(len(key))
    n = int(math.sqrt(len(key)))
    f = np.array(chunk(stov(key, alphabet), n)) # n x n matrix
    assert len(plaintext) % n == 0

    ciphertext = ''
    for s in chunk(plaintext, n):
        x = np.array(stov(s, alphabet))
        y = np.dot(f, x) % m
        ciphertext += vtos(y.tolist(), alphabet)
    return ciphertext

def decrypt(ciphertext, alphabet, key):
    assert isinstance(alphabet, str)
    assert isinstance(key, str)
    m = len(alphabet) # modulo
    assert is_square(len(key))
    n = int(math.sqrt(len(key)))
    f = np.array(chunk(stov(key, alphabet), n))

    g = modinv(f, m)
    invkey = vtos(sum(g.tolist(), []), alphabet)
    return encrypt(ciphertext, alphabet, invkey)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=[ 'e', 'encrypt', 'd', 'decrypt' ])
    parser.add_argument('text', nargs='*')
    parser.add_argument('-a', '--alphabet', required=True)
    parser.add_argument('-k', '--key', required=True)
    args = parser.parse_args()

    if not is_square(len(args.key)):
        parser.error('key must be a square matrix')

    if not args.text:
        import sys
        args.text = map(lambda line: line.strip(), sys.stdin)
    for s in args.text:
        if args.command[0] == 'e': # ncrypt
            print(encrypt(s, alphabet=args.alphabet, key=args.key))
        elif args.command[0] == 'd': # ecrypt
            print(decrypt(s, alphabet=args.alphabet, key=args.key))
