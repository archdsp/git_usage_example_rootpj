testFunc = None
try:
    import module_a as A
    testFunc = A.a.test()
except ImportError:
    print("import module A failed")

try:
    import module_b as B
    testFunc = B.b.test()
except ImportError:
    print("import module B failed")


if __name__ == "__main__":
    if testFunc is not None:
        testFunc()
