#Python recursive algo to compute a product
#positive int m and n using only add and sub

def product(m, n):
    if (m and n >= 1):
        if (n<=1):
            return m
        else:
            return m+product(m, n-1)
    else:
        print("Input/s must be all positive int")

if __name__=="__main__":
    print("The product of m and n is:", product(3, 3))

