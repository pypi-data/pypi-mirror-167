import doctest
import unittest

import pymultihash
import pymultihash.funcs
import pymultihash.codecs
import pymultihash.multihash


def suite():
    tests = unittest.TestSuite()
    for module in [pymultihash.funcs, pymultihash.codecs, pymultihash.multihash, pymultihash]:
        tests.addTests(doctest.DocTestSuite(module))
    return tests


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
