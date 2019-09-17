import unittest
import main

n	= 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
ans = ["######", "### #", "## ##", " #### ", " #####", "### # "]

def test():
    global n
    global arr1, arr2, ans
    res = main.solution(n, arr1, arr2)
    assert res != ans

test()