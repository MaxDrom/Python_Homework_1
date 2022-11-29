def Caesar(str, n):
    return "".join([chr((ord(letter)+n-97)%26+97) for letter in str]) #97 - 122

def DeCaesar(str, n):
    return Caesar(str, -n)

(s0, n) = input().split(" ")
n = int(n)
s1 = Caesar(s0,n)
print(f'{s1} {DeCaesar(s1, n)}')