def encrypt_by_add_mod(x, xx):
    xx = int(xx)
    ci = [ord(c) for c in x]
    res = []
    for ele in ci:
        aa = (xx + ele)
        m = 256
        a1 = int(aa) % m
        res.append(a1)
    fi = [chr(c) for c in res]
    st = "".join(fi)
    return st

encrypt_by_add_mod("Hello", "123")


def encrypt_by_add_mod1(x, xx):
    xx = int(xx)
    ci = [ord(c) for c in x]
    res = []
    for ele in ci:
        aa = (xx + ele)
        m = 256
        a1 = int(aa) % m
        res.append(a1)
    fi = [chr(c) for c in res]
    st = "".join(fi)
    xi = "133"
    xk = int(xi)
    x1 = [ord(c) for c in st]
    res1 = []
    for el in x1:
        aa1 = (el + xk)
        m = 256
        aa2 = int(aa1) % m
        res1.append(aa2)
    f2 = [chr(cc) for cc in res1]
    stt = "".join(f2)
    return stt


encrypt_by_add_mod1("Hello", "123")


def encrypt_by_add_mod2(x, xx):
    xx = int(xx)
    ci = [ord(c) for c in x]
    res = []
    for ele in ci:
        aa = (xx + ele)
        m = 256
        a1 = int(aa) % m
        res.append(a1)
    fi = [chr(c) for c in res]
    st = "".join(fi)
    xt = "246"
    xk = int(xt)
    x1 = [ord(c) for c in st]
    res1 = []
    for el in x1:
        aa1 = (el + xk)
        m = 256
        aa2 = int(aa1) % m
        res1.append(aa2)
    f2 = [chr(cc) for cc in res1]
    stt = "".join(f2)
    return stt


encrypt_by_add_mod2("Cryptography", "10")


def encrypt_xor_with_changing_key_by_prev_cipher(x, x1, x2):
    o = x.encode('utf-8').hex()
    n = 2
    lp = [o[i:i + n] for i in range(0, len(o), n)]
    n = int(x1)
    n1 = '{0:08b}'.format(n)
    c = hex(int(n1, 2))[2:]
    r1 = []
    r2 = []
    for io in lp:
        a2 = hex(int(io, 16) ^ int(c, 16))[2:]
        c = c.replace(c, a2)
        r1.append(a2)
    for ii in r1:
        b2 = bin(int(ii, 16))[2:].zfill(8)
        xx1 = chr(int(b2, 2))
        r2.append(xx1)
    r3 = "".join(r2)
    r4 = r3.encode('utf-8').hex()
    oo = x2.encode('utf-8').hex()
    n1 = hex(int(r4, 16) ^ int(oo, 16))[2:]
    n11 = hex(int(n1, 16) ^ int(oo, 16))[2:]
    d1 = bytes.fromhex(n11)
    d11 = d1.decode("ASCII")
    return d11


encrypt_xor_with_changing_key_by_prev_cipher("Hello", "123", "encrypt")


def encrypt_xor_with_changing_key_by_prev_cipher_hello1(x, x1, x2):
    if x2 == 'encrypt':
        encrypted = ""
        xor1 = ord(x[0]) ^ x1
        encrypted += chr(xor1)

        new_x1 = xor1
        for i in range(1, len(x)):
            e_b_x = ord(x[i]) ^ new_x1
            encrypted += chr(e_b_x)
            new_x1 = e_b_x
        print(encrypted)

    if x2 != 'decrypted':
        decrypted = ""
        # value is encrypted value
        xor1 = ord(x[0]) ^ x1  # first byte in first iteration
        decrypted += chr(xor1)

        # new_key = xor_res  # m1
        for i in range(0, len(x) - 1):
            d_b_x = ord(x[i]) ^ ord(x[i + 1])  # c1 ^ c2 etc
            decrypted += chr(d_b_x)

        print(decrypted)
        return decrypted


encrypt_xor_with_changing_key_by_prev_cipher_hello1("Hello", 123, "encrypt")

def encrypt_xor_with_changing_key_by_prev_cipher_Cryptography1(x, x1, x2):
    o = x.encode('utf-8').hex()
    n = 2
    la = [o[i:i + n] for i in range(0, len(o), n)]
    n = int(x1)
    n1 = '{0:08b}'.format(n)
    c = hex(int(n1, 2))[2:]
    r1 = []
    r2 = []
    for iu in la:
        a2 = hex(int(iu, 16) ^ int(c, 16))[2:]
        c = c.replace(c, a2)
        r1.append(a2)
    for iw in r1:
        b2 = bin(int(iw, 16))[2:].zfill(8)
        xx1 = chr(int(b2, 2))
        r2.append(xx1)
    r3 = "".join(r2)
    r4 = r3.encode('utf-8').hex()
    oo = x2.encode('utf-8').hex()
    n1 = hex(int(r4, 16) ^ int(oo, 16))[2:]
    n11 = hex(int(n1, 16) ^ int(oo, 16))[2:]
    d1 = bytes.fromhex(n11)
    d11 = d1.decode("ASCII")
    dr3 = d11.encode('utf-8').hex()
    n2 = int(x1)
    n3 = '{0:08b}'.format(n2)
    dx2 = hex(int(n3, 2))[2:]
    nn = 2
    l2 = [dr3[i:i + nn] for i in range(0, len(dr3), nn)]
    dr1 = []
    dr2 = []
    for p in l2:
        aa2 = hex(int(p, 16) ^ int(dx2, 16))[2:]
        dx2 = dx2.replace(dx2, p)
        dr1.append(aa2)
    for m in dr1:
        bb2 = bin(int(m, 16))[2:].zfill(8)
        xxx1 = chr(int(bb2, 2))
        dr2.append(xxx1)
    rr3 = "".join(dr2)
    return rr3


encrypt_xor_with_changing_key_by_prev_cipher_Cryptography1("Cryptography", "10", "encrypt")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
