#  Задание 1
s = input().strip()
is_palindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("yes")
else:
    print("no")


#  Задание 2
s = input().strip()
s = ' '.join(s.split())
print(s)
