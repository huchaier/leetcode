def reverseBits(n):
    print(bin(n))
    print(bin(n >> 16))
    n = (n >> 16) | (n << 16)
    print(bin(n))
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    print(bin(n))
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    print(bin(n))
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    print(bin(n))
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    print(bin(n))
    print(n)

reverseBits(43261596)

