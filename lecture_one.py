import unittest
import time

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("divide by zero")
    return x / y

class TestCalculator(unittest.TestCase):

    def report(self, test_name, expected, actual, exec_time):
        status = "PASS" if expected == actual else "FAIL"
        print(f"\n{test_name}")
        print(f"Expected       : {expected}")
        print(f"Actual         : {actual}")
        print(f"Status         : {status}")
        print(f"Execution Time : {exec_time:.4f} ms")

    def test_add(self):
        start = time.perf_counter()

        expected = 5
        actual = add(2, 3)

        end = time.perf_counter()
        exec_time = (end - start) * 1000

        self.report("test_add", expected, actual, exec_time)
        self.assertEqual(actual, expected)

    def test_sub(self):
        start = time.perf_counter()

        expected = 6
        actual = sub(10, 4)

        end = time.perf_counter()
        exec_time = (end - start) * 1000

        self.report("test_sub", expected, actual, exec_time)
        self.assertEqual(actual, expected)

    def test_multiply(self):
        start = time.perf_counter()

        expected = 15
        actual = multiply(3, 5)

        end = time.perf_counter()
        exec_time = (end - start) * 1000

        self.report("test_multiply", expected, actual, exec_time)
        self.assertEqual(actual, expected)

    def test_divide(self):
        start = time.perf_counter()

        expected = 5
        actual = div(20, 4)

        end = time.perf_counter()
        exec_time = (end - start) * 1000

        self.report("test_divide", expected, actual, exec_time)
        self.assertEqual(actual, expected)

    def test_divide_by_zero(self):
        start = time.perf_counter()

        expected = "ValueError"
        try:
            div(20, 0)
            actual = "No Exception"
        except ValueError as e:
            actual = type(e).__name__

        end = time.perf_counter()
        exec_time = (end - start) * 1000

        self.report("test_divide_by_zero", expected, actual, exec_time)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
