A = input()
B = input()

diff = ord(A[0]) - ord(B[0])
list_A = list(map(lambda x: (ord(x) - ord(A[0]))%26, A))
list_B = list(map(lambda x: (ord(x) - ord(B[0]))%26, B))

print("Yes") if list_A == list_B else print("No")