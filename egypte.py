def multiplicationEgyptienne(n, p):
    produit = 0
    while n != 0:
        if n % 2 == 1: 
            produit += p
        n //= 2 
        p += p 
    return produit

a = int(input())
b = int(input())
test = multiplicationEgyptienne(a, b)
print(test)