import unittest
import solve

inarr = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
outarr = [37, 9, 3, 23, 5, -4, 59]

for i in range(len(inarr)):
    ans = solve.solution(inarr[i])
    print(ans, outarr[i])
    assert ans == outarr[i]