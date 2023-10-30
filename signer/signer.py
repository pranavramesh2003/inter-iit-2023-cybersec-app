# Do NOT modify this file

import os

try:
    from Crypto.Cipher import AES
except ImportError:
    from Cryptodome.Cipher import AES

INTER_IIT = b'InterIIT-2023'

class Signer:
    def __init__(self):
        self.__key = os.urandom(16)

    def split_chunk(data, chunk_size):
        return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    def pad_right(data, pad_align):
        b = pad_align - len(data) % pad_align
        return data + bytes([b] * b)

    def xor(a, b):
        return bytes(aa ^ bb for aa, bb in zip(a, b))

    def __sign(data, key):
        data = Signer.pad_right(data, 16)
        blocks = Signer.split_chunk(data, 16)
        mac = b'\0' * 16

        aes = AES.new(key, AES.MODE_ECB)
        for block in blocks:
            mac = Signer.xor(mac, block)
            mac = aes.encrypt(mac)

        mac = aes.encrypt(mac)
        return mac

    def __verify(data, key):
        if len(data) < 16:
            return False, ''

        tag, data = data[:16], data[16:]
        correct_tag = Signer.__sign(data, key)
        if tag != correct_tag:
            return False, ''

        return True, data

    def execute(self, action, data):
        if action == 'sign':
            data = bytes.fromhex(data)

            if INTER_IIT in data:
                return -1, "Nope, not that easy!"

            return 1, (Signer.__sign(data, self.__key) + data).hex()

        elif action == 'verify':
            data = bytes.fromhex(data)

            ok, data = Signer.__verify(data, self.__key)
            if ok:
                if INTER_IIT in data:
                    return 2, "Congratulations, you did it!"
                else:
                    return 0, "Signature checks out!"
            else:
                return -2, "Wrong signature!"

        else:
            return -3, "Can't do that for you! Can only sign and verify..."
