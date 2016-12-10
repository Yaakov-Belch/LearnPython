from itertools import chain, accumulate
from collections import Counter

zero='0'*10;
def flip(k,n): return k[:n]+('1' if k[n]=='0' else '0')+k[n+1:]

def solution(s):
  cc=Counter(accumulate(chain((zero,),map(int,s)),flip))
  res=0
  for k,v in cc.items():
    res+=v*(v-1)
    for n in range(10): res+=v*cc[flip(k,n)]
  return (res//2) % 1000000007

result=solution("02002")
print(result)
