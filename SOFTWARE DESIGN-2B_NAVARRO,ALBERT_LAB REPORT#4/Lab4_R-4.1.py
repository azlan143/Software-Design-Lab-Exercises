#function to find max ele in a seq, S, of n ele recursively
def find_max(S, n):
    """Find the maximum element in a sequence S, of n elements."""
    if n == 1:  # reached the left most item
        return S[n-1]
    else:
        previous = find_max(S, n-1)
        current = S[n-1]
        if previous > current:
            return previous
        else:
            return current

if __name__ == '__main__':
    print(find_max([1, 5, 8, 3, 4], 5))