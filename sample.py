from collections import Counter

zero=tuple(0 for i in range(10))
def flip(k,v): k=list(k); k[v]=1-k[v]; return tuple(k)


print(Counter((flip(zero,2),)))


def solution(s):
  return 11

result=solution("02002")
print(result)
