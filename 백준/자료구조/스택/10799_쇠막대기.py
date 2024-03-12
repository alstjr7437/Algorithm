s = input()

stack = []
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append('(')
  else: 
    stack.pop()
    if s[i-1] == ')':
      cnt+=1
    else:
      cnt += len(stack)
print(cnt)