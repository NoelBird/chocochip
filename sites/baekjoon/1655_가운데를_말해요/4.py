# pypy에서는 충분히 빠르지만
# python에서는 라이브러리에서 캐시가 생성되는 것에 비해, 여기에서는 캐시가 없어서 느렸음
# 시간 초과

import sys
input = sys.stdin.readline

def heappush(heap, item):
    heap.append(item)
    startpos, pos = 0, len(heap)-1
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if item < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = item

def heappop(heap):
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        pos = 0
        heap[0] = lastelt
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        heap[pos] = newitem
        newitem = heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem
        return returnitem
    return lastelt

def sol():
    N = int(input())
    ans = [0]*N
    h_small = []
    h_big = []
    for i in range(N):
        a = int(input())
        if i % 2:
            heappush(h_big, a)
        else:
            heappush(h_small, -a)
        if h_big and -h_small[0] > h_big[0]:
            tmp1 = -heappop(h_small)
            tmp2 = -heappop(h_big)
            heappush(h_small, tmp2)
            heappush(h_big, tmp1)
        ans[i] = -h_small[0]
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    sol()