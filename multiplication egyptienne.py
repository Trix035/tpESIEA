def multiplicationEgyptienne(n, p):
    produit = 0
    while n != 0:
        if n % 2 == 1:  
            produit += p
        n //= 2 
        p *= 2 

    print(produit)        
    return produit
 
multiplicationEgyptienne()
