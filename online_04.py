# 04 요리제작

n = int(input())
arr1 = list(map(int, input().split())) # 창고
arr2 = list(map(int, input().split())) # 소모되는 재료수


def getCount(arr1, arr2):
  c = 0 # 스테이크 갯수
  while True:
    for i in range(len(arr1)):
      if arr1[i] < arr2[i]:
        return c
      else:
        arr1[i] -= arr2[i]
    c += 1
  

print(getCount(arr1, arr2))