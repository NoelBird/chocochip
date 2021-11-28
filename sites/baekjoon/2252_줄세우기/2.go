// 48ms
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type node struct {
	outNode   []int
	cntInNode int
}

const MAX_Q_LEN int = 32001

func main() {
	var N, M int
	// fmt.Fscanln(reader, &N, &M)
	N = nextInt()
	M = nextInt()

	graph := []node{}
	graph = append(graph, node{[]int{}, -1}) // dummy node

	// 1. construct graph - linked list
	for i := 1; i < N+1; i++ {
		graph = append(graph, node{[]int{}, 0})
	}

	for i := 0; i < M; i++ {
		var a, b int
		a = nextInt()
		b = nextInt()
		// fmt.Fscanln(reader, &a, &b)
		graph[a].outNode = append(graph[a].outNode, b)
		graph[b].cntInNode++
	}

	// 2. solve
	result := solve(graph)
	s := strings.Trim(fmt.Sprint(result), "[]")
	fmt.Println(s)

}

func solve(graph []node) []int {
	// topological sort
	// khan algorithm

	var result []int

	q := queue{}
	q.init()

	for i := 1; i < len(graph); i++ {
		if graph[i].cntInNode == 0 {
			q.push(i)
		}
	}
	for q.len() > 0 {
		cur := q.pop()

		// save to result slice
		result = append(result, cur)

		lenCurOutNode := len(graph[cur].outNode)
		for i := 0; i < lenCurOutNode; i++ {
			targetNode := graph[cur].outNode[i]
			graph[targetNode].cntInNode--
			if graph[targetNode].cntInNode == 0 {
				q.push(targetNode)
			}
		}
	}

	return result
}

// io
var scanner *bufio.Scanner

func init() {
	scanner = bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
}

func nextInt() int {
	scanner.Scan()
	sign, x := 1, 0
	for _, b := range scanner.Bytes() {
		if b == '-' {
			sign = -1
			continue
		}
		x *= 10
		x += int(b - '0')
	}
	return sign * x
}

// queue
type queue struct {
	data   [MAX_Q_LEN]int
	maxlen int
	start  int
	end    int
}

func (q *queue) init() {
	q.maxlen = MAX_Q_LEN
	q.start = 0
	q.end = 0
}

func (q *queue) push(n int) {
	q.data[q.end] = n
	q.end++
}

func (q *queue) pop() int {
	popData := q.data[q.start]
	q.start++
	return popData
}

func (q *queue) len() int {
	return q.end - q.start
}
