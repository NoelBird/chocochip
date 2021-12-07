// 2 5
// 1 2
// 3 4

// idea1. 가장 느린 것. 다 곱하기
// idea2. 그것보다 좀 더 빠른 것. 두 개씩 묶어서 곱하기 (log N) => 125*40 => 가능
// idea3. GeMM..?
// idea4. loop optimization(unrolling, blocking)
// idea5. power method(https://ergodic.ugr.es/cphys/LECCIONES/FORTRAN/power_method.pdf) - not large matrix
// idea6. vectorization(SIMD)
// idea7. EVD(with modular) - https://www.tutorialspoint.com/cplusplus-program-to-find-inverse-of-a-graph-matrix
// idea8. 