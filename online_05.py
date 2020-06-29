# 05. ID 확인 (model solution)

n = int(input())

# 유효한 문자열이 있는지 검사한다.
def check(s):
  if len(s) == 0:
    return False
  for c in s:
    if c.isalnum():
      continue
    elif c == '-' or c == '.':
      continue
    else:
      return False
  
  return True

# 문자열을 로컬과 도메인으로 분리한다.
def getLocalAndDomain(s):
  i = s.find('@')
  if i < 0:
    return '', ''
  local = s[0:i]
  domain = s[i+1:]
  return local, domain

# 이메일을 검사한다.  
def checkEmail(s):
  local, domain = getLocalAndDomain(s)
  # print(local, domain)
  if check(local) == False:
    return False

  if check(domain) == False:
    return False
    
  return True
  
for i in range(n):
  s = input()
  if checkEmail(s):
    print('Yes')
  else:
    print('No')