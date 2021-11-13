import unittest
import solution


class Test(unittest.TestCase):
    def test(self):
        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        ans = [3,4,2,1,5]
        self.assertEqual(solution.solution(N, stages), ans)

if __name__ == "__main__":
    unittest.main()