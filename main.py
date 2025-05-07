def stack():
    s=[]
    return s
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return(s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size(s):
    return(len(s))

ekspresi = input("Masukkan ekspresi matematika: ")
st = stack()
seimbang = True
pasangan = {')': '(', ']': '[', '}': '{'}

for char in ekspresi:
    if char in "([{":
        push(st, char)
    elif char in ")]}":
        if isEmpty(st) or peek(st) != pasangan[char]:
            seimbang = False
            break
        else:
            pop(st)

if not isEmpty(st):
    seimbang = False

if seimbang:
    print("Kurung seimbang")
else:
    print("Kurung tidak seimbang")

