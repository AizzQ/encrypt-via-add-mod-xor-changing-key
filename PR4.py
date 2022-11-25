def encrypt_by_add_mod(message, key):
    ...
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    ...
    ret = ''
    for i in message:
        new_byte = (ord(message[0]) + key % 256
        ret += chr(new_byte)

    return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()

