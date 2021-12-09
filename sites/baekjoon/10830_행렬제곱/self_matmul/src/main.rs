// ========== general ==================
// idea1. 가장 느린 것. 다 곱하기 (x. 비효율적)
// => O(n^3 * 1조) => 무조건 TLE

// idea2. 그것보다 좀 더 빠른 것. 두 개씩 묶어서 곱하기 (o)
// => (log N) => 125*40 = 5000 => 가능

// idea3. GeMM..? (x. 굳이 불필요)
// => cache hit가 높아져서 성능이 좋아질 것
// =>  다만 지금 matrix는 사이즈가 작아서 충분히 cache에서 재사용 될 것이고, 굳이 여기까지 필요 없을 듯
// => cache는 L3 cache가 수백 KB에서 MB 단위라서 int 5^3 개는 충분히 다 들어옴

// idea4. loop optimization(unrolling, blocking, loop permutation, vectorization) (x. 굳이 불필요)
// => matrix의 사이즈가 크지 않아서 큰 효과들이 없을 것
// => unrolling: 비교 연산 횟수가 별로 줄어들지 않음
// => vectorization: 밑에서 별도 언급
// => permutation: loop의 사이즈가 정방행렬이라서 permutation은 필요가 없음
// => blocking: matrix size가 작아서 cache에 충분히 다 들어옴

// idea5. vectorization(SIMD) (x. 다음에 적용 해보고 싶음)
// => 다음에 시도해 볼 수 있을 듯. 효과 있을 것으로 기대. 연산횟수가 O(n^3 * b) = 125 * 40 번에서 125가 1로 되어 40번 연산으로 끝날 듯

// idea6. 빠른 언어로 구현 (o)
// => rust
// => 소유권 개념이 아직은 좀 낯설어서, zero copy를 충분히 구현하지 못 했음

// ========== factorization ==================
// idea7. power method (x. not large matrix)
// => 큰 sparse matrix의 경우에 power method로 eigen value를 구하는 것이 빨라질 수 있는데, matrix가 작음
// => https://ergodic.ugr.es/cphys/LECCIONES/FORTRAN/power_method.pdf

// idea8. EVD(with modular) (x. 추후 적용하고 싶음)
// => EVD 자체 O(m x n^2) 소요 + eigen values 1조번 곱하면 연산횟수(1조 x 5) + 최종 계산
// => idea2와 연결하면 5^3 + 40x5 + 3 = 125 + 200 + 3x5^2 = 400번 연산
// => 정확도가 조금 떨어질 수 있지만, idea2 대비 1/10로 연산 횟수 줄었음
// => https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra
// => https://www.tutorialspoint.com/cplusplus-program-to-find-inverse-of-a-graph-matrix

// idea9. fast and stable EVD
// => 작은 matrix이기 때문에 houseHolderQR 또는 ColPivHouseHolderQR 분해가 좋을 듯
// => https://eigen.tuxfamily.org/dox/group__TutorialLinearAlgebra.html

// =============================================
// quick & dirty(idea 2, 6): maxium calculation: 5^3 * 40 = 125*40 = 5000
// 
// further(idea 2, 5, 6, 8, 9): 5 + 40x5 + 3 = 약 200번 연산 (1/20으로 지금에 비해서 더 빠를 수 있을 듯)

use std::io;
use std::fmt::Write;

fn main() {
    let mut mat: [[[u32; 5]; 5]; 40] = [[[0u32; 5]; 5]; 40];
    
    // get input
    let v: Vec<u64> = read_numbers64();
    let n: u32 = v[0] as u32;
    let b: u64 = v[1];

    // initialize matrix
    for i in 0..n as usize{
        let num: Vec<u32> = read_numbers32();
        for j in 0..n as usize{
            mat[0][i][j] = num[j];
        }
    }

    // check max iteration
    let mut max_iter = 0;
    let mut b_copy = b;
    while b_copy > 0 {
        max_iter+=1;
        b_copy /= 2;
    }

    // it's hard to zero copy
    for i in 1..(max_iter+1) as usize {
        let mut mat_result: [[u32; 5]; 5] = [[0u32; 5]; 5];
        matmul_self(&mat[i-1], &mut mat_result, n);
        for j in 0..n as usize {
            for k in 0..n as usize {
                mat[i][j][k] = mat_result[j][k];
            }
        }
    }
    let mut result: [[u32; 5];5] = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ];
    let mut b_copy = b;
    for i in 0..max_iter as usize {
        let mut tmp_result: [[u32; 5];5] = [[0u32; 5]; 5];
        if b_copy % 2 == 1 {
            matmul(&mat[i], &result, &mut tmp_result, n);
            result = tmp_result;
        }
        b_copy /= 2;
    }

    let mut result_buf = String::new();
    for i in 0..n as usize {
        for j in 0..n as usize {
            write!(&mut result_buf, "{} ", result[i][j]).unwrap();
        }
        writeln!(&mut result_buf, "").unwrap();
    }
    print!("{}", result_buf);
}


fn read_numbers64()-> Vec<u64>{
    let mut s = String::new();
    io::stdin()
        .read_line(&mut s)
        .expect("Unexpected EOL");
    let v: Vec<u64> = s
    .trim()
    .split_whitespace()
    .map(|x| x.parse().unwrap())
    .collect();

    return v;
}

fn read_numbers32()-> Vec<u32>{
    let mut s = String::new();
    io::stdin()
        .read_line(&mut s)
        .expect("Unexpected EOL");
    let v: Vec<u32> = s
    .trim()
    .split_whitespace()
    .map(|x| x.parse().unwrap())
    .collect();

    return v;
}

fn matmul_self(mat: &[[u32; 5]; 5], result: &mut [[u32; 5]; 5], len: u32){
    for i in 0..len as usize {
        for j in 0..len as usize{
            for k in 0..len as usize{
                result[i][j] += mat[i][k]*mat[k][j];
                result[i][j] %= 1000;
            }
        }
    }
}

fn matmul(mat1: &[[u32; 5]; 5], mat2: &[[u32; 5]; 5], result: &mut [[u32; 5]; 5], len: u32){
    for i in 0..len as usize {
        for j in 0..len as usize{
            for k in 0..len as usize{
                result[i][j] += mat1[i][k]*mat2[k][j];
                result[i][j] %= 1000;
            }
        }
    }
}