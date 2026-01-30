import string as str

def amplitude(x,y):
    return abs(x-y)

def imprime_string(s):
    for char in s:
        print(char)
    
def valor_peso(peso):
    if peso <= 10:
        return "R$ 50"
    if peso > 10 and peso <= 20: 
        return "R$ 80"
    return "Não aceita a carga" 

print(amplitude(5,-3))
imprime_string("Hello World")
print(valor_peso(10))
print(valor_peso(20))
print(valor_peso(360))

s = [1,2,3,4,5]
string = "Hello"
for c in range(len(s)):
    print(s[c])

for c in s:
    print(c)

