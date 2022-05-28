# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n, from_peg, to_peg, aux_peg):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_peg, aux_peg, to_peg)
    print("Move disk", n, "from peg", from_peg, "to peg", to_peg)
    TowerOfHanoi(n - 1, aux_peg, to_peg, from_peg)

n = 4
print("Tower of Hanoi solution with", n , "disks")
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods

