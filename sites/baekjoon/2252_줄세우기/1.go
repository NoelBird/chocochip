// too slow(1400ms) - because of io
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

type node struct {
	outNode   []int
	cntInNode int
}

func main() {
	var N, M int
	fmt.Fscanln(reader, &N, &M)

	graph := []node{}
	graph = append(graph, node{[]int{}, -1}) // dummy node

	// 1. construct graph - linked list
	for i := 1; i < N+1; i++ {
		graph = append(graph, node{[]int{}, 0})
	}

	for i := 0; i < M; i++ {
		var a, b int
		fmt.Fscanln(reader, &a, &b)
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

	q := make([]int, 0)

	for i := 1; i < len(graph); i++ {
		if graph[i].cntInNode == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]

		// save to result slice
		result = append(result, cur)

		lenCurOutNode := len(graph[cur].outNode)
		for i := 0; i < lenCurOutNode; i++ {
			targetNode := graph[cur].outNode[i]
			graph[targetNode].cntInNode--
			if graph[targetNode].cntInNode == 0 {
				q = append(q, targetNode)
			}
		}
	}

	return result
}
