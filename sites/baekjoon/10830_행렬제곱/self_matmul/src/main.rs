// idea1. 가장 느린 것. 다 곱하기
// idea2. 그것보다 좀 더 빠른 것. 두 개씩 묶어서 곱하기 (log N) => 125*40 => 가능
// idea3. GeMM..?
// idea4. loop optimization(unrolling, blocking)
// idea5. power method(https://ergodic.ugr.es/cphys/LECCIONES/FORTRAN/power_method.pdf) - not large matrix
// idea6. vectorization(SIMD)
// idea7. EVD(with modular) - https://www.tutorialspoint.com/cplusplus-program-to-find-inverse-of-a-graph-matrix
// idea8. 빠른 언어로 구현
// =============================================
// maxium calculation: 5^3 * 40 = 125*40 = 5000

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