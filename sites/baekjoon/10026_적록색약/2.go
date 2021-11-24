// 8ms - quite faster
// TODO1: make circular queue
package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

type Point struct {
	x int
	y int
	c uint8
}

func solve(N int, Mat [100][100]uint8) int {
	MatVisited := [100][100]int{{0}}

	var cnt int = 0
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {

			if MatVisited[i][j] != 0 {
				continue
			}
			cnt++

			q := []Point{}
			q = append(q, Point{j, i, Mat[i][j]})

			for len(q) > 0 {
				// pop
				cur := q[0]
				q = q[1:]
				x := cur.x
				y := cur.y
				c := cur.c

				// if visited
				if MatVisited[y][x] != 0 {
					continue
				}
				if Mat[y][x] != c {
					continue
				}

				if x > 0 && Mat[y][x-1] == c {
					q = append(q, Point{x - 1, y, c})
				}
				if x < N-1 && Mat[y][x+1] == c {
					q = append(q, Point{x + 1, y, c})
				}
				if y > 0 && Mat[y-1][x] == c {
					q = append(q, Point{x, y - 1, c})
				}
				if y < N-1 && Mat[y+1][x] == c {
					q = append(q, Point{x, y + 1, c})
				}
				MatVisited[y][x] = cnt
			}
		}
	}
	return cnt
}

func main() {
	var N int
	Mat := [100][100]uint8{{0}}
	MatBlind := [100][100]uint8{{0}}

	_, err := fmt.Fscanln(reader, &N)
	if err != nil {
		fmt.Println(err)
		return
	}

	for i := 0; i < N; i++ {
		var str string
		_, err := fmt.Fscanln(reader, &str)
		if err != nil {
			fmt.Println(err)
			return
		}
		for j := 0; j < N; j++ {
			Mat[i][j] = str[j]
			if str[j] == 'G' {
				MatBlind[i][j] = 'R'
			} else {
				MatBlind[i][j] = str[j]
			}
		}
	}
	fmt.Print(solve(N, Mat), solve(N, MatBlind), "\n")
}
