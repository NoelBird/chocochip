while True:
  N = input()
  if N == "0":
    break
  isPal = True
  for i in range(len(N)//2):
    if N[i] != N[len(N)-1-i]:
      print("no")
      isPal = False
      break
  if isPal:
    print("yes")