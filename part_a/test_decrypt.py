import unittest
from decrypt import xor_decrypt,  xor_encrypt, key_generator, try_single_key
class TestDecrypt(unittest.TestCase):
    def test_xor_decrypt(self):
        res = xor_decrypt([24, 24, 26, 30, 28], "yz")
        self.assertEqual(res, 'abcde')

    def test_xor_encrypt(self):
        res = xor_encrypt('abcde', "yz")
        self.assertEqual(res, [24, 24, 26, 30, 28])

    def test_key_generator_limit(self):
        keygen = key_generator(2, 0 , 3)
        end=False
        try:
            a = next(keygen)
            b = next(keygen)
            c = next(keygen)
            d = next(keygen)
        except StopIteration:
            end = True

        self.assertEqual(a, 'aa')
        self.assertEqual(b, 'ab')
        self.assertEqual(c, 'ac')
        try:
            print(d)
        except UnboundLocalError:
            d ='UnboundLocalError'

        self.assertEqual(d, 'UnboundLocalError')
        self.assertEqual(end, True)

    def test_key_generator_offset(self):
        keygen = key_generator(2, 673)
        end = False
        try:
            a = next(keygen)
            b = next(keygen)
            c = next(keygen)
            d = next(keygen)
        except StopIteration:
            end = True

        self.assertEqual(a, 'zx')
        self.assertEqual(b, 'zy')
        self.assertEqual(c, 'zz')
        try:
            print(d)
        except UnboundLocalError:
            d = 'UnboundLocalError'

        self.assertEqual(d, 'UnboundLocalError')
        self.assertEqual(end, True)

    def test_try_single_key(self):
        res, key = try_single_key([2], 'b') # 2 is result of backtick ^ b
        res2, key2 = try_single_key([3], 'b') # 3 is result of a ^ b
        self.assertEqual(res, False)
        self.assertEqual(res2, 'a')
        self.assertEqual(key2, 'b')

if __name__ == '__main__':
    unittest.main()

