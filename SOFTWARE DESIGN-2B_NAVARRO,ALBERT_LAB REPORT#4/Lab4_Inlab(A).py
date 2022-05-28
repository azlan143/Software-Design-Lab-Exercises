#Python recursive function algo to
#find max and min val in a sequence

def recursiveMin(data, n):
    if (n==1):
        return data[0]
    return min(data[n-1], recursiveMin(data, n-1))

def recursiveMax(data, n):
    if (n==1):
        return data[0]
    return max(data[n-1], recursiveMax(data, n-1))

def main():
    data = [9, 1, 5, 8, 3, 4]
    n = len(data)
    print("Sequence: ", data)
    print("Minimum: ", recursiveMin(data, n))
    print("Maximum: ", recursiveMax(data, n))

if __name__ == "__main__":
    main()

