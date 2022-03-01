
def suite_syracuse(n):
   

    seq = [n]                  
    while seq[-1] != 1:           
        if seq[-1] % 2 == 0:      
            seq.append(seq[-1] // 2)  
        else:                   
            seq.append(seq[-1] * 3 + 1)

    return seq


def temps_syracuse(n, altitude=False):


    seq = suite_syracuse(n)
    if not altitude:            
        return len(seq) - 1
    else:                       
        alt = []
        for i in seq:
            if i >= n:
                alt.append(i)
            else:
                break
        return len(alt) - 1

if __name__ == '__main__':

    n = 15
    print("Suite de Syracuse pour n =", n)
    print(suite_syracuse(n))
    print("Temps de vol total:      ", temps_syracuse(n))
    print("Temps de vol en altitude:", temps_syracuse(n, altitude=True))