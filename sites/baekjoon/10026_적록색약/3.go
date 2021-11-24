// 4ms - optimized
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

type Queue struct {
	data         [400]Point
	start        int
	end          int
	maxQueueSize int
}

func (q *Queue) init() {
	q.maxQueueSize = 400
	q.start = 0
	q.end = 0
}

func (q *Queue) push(p Point) {
	q.data[q.end] = p
	if q.end == q.maxQueueSize-1 {
		q.end = 0
	} else {
		q.end++
	}
}

func (q *Queue) pop() Point {
	ret := q.data[q.start]
	if q.start == q.maxQueueSize-1 {
		q.start = 0
	} else {
		q.start++
	}

	return ret
}

func (q *Queue) len() int {
	if q.end-q.start >= 0 {
		return q.end - q.start
	} else {
		return q.maxQueueSize + q.end - q.start
	}
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

			q := Queue{}
			q.init()
			q.push(Point{j, i, Mat[i][j]})

			for q.len() > 0 {
				// pop
				cur := q.pop()
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
					q.push(Point{x - 1, y, c})
				}
				if x < N-1 && Mat[y][x+1] == c {
					q.push(Point{x + 1, y, c})
				}
				if y > 0 && Mat[y-1][x] == c {
					q.push(Point{x, y - 1, c})
				}
				if y < N-1 && Mat[y+1][x] == c {
					q.push(Point{x, y + 1, c})
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
