n = input()
k = int(input())
char = (ord(n) - ord('A')+k)%26 +65
print(chr(char))