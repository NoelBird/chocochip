import sys
input = sys.stdin.readline

def heappush(heap, h_len, item):
    heap[h_len] = item
    startpos, pos = 1, h_len
    while pos > startpos:
        parentpos = pos >> 1
        parent = heap[parentpos]
        if item < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = item

def heappop(heap, h_len):
    if h_len <= 1:
        return heap[h_len]
    returnitem, heap[1] = heap[1], heap[h_len]
    endpos = h_len
    pos = 1
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = pos >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
    return returnitem

def sol():
    N = int(input())
    ans = [0]*N
    h_small = [0]*100001 # root: 1
    h_big = [0]*100001 # root: 1
    len_small = 0
    len_big = 0

    for i in range(N):
        a = int(input())
        if i % 2:
            len_big += 1
            heappush(h_big, len_big, a)
        else:
            len_small += 1
            heappush(h_small, len_small, -a)
        
        if len_big and -h_small[1] > h_big[1]:
            tmp1 = -heappop(h_small, len_small)
            tmp2 = -heappop(h_big, len_big)
            heappush(h_small, len_small, tmp2)
            heappush(h_big, len_big, tmp1)
        ans[i] = -h_small[1]
    sys.stdout.write("\n".join(map(str, ans)))

if __name__ == "__main__":
    sol()