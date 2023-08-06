'''
Created on Sep 13, 2022

@author: vladislavkargin

This code was written by Lizzie Hernandez 
for Math 68 Algebraic Combinatorics course in Fall 2021 
at Darmouth College
'''

# Some useful, pretty print functions

# Params: shape - non-increasing integer list specifying a tableau's shape
# Prints a tableau of given shape
def print_tableau(shape):
    print(" ___" * shape[0])
    for l in shape:
        print("|" + "   |" * l)
        print("|" + "___|" * l)

# Params: original - non-increasing integer list specifying the shape of original tableau
#         reduced - non-increasing integer list specifying the shape of "reduced" tableau (with removed ribbon)
# Prints reduced tableau
def print_red_tableau(original, reduced, tab=""):
    print(tab + " ___" * original[0])
    for r in range(len(original)):
        l = original[r]
        cells = tab + "|"
        for i in range(l):
            cells += " " + (" " if (r < len(reduced) and i < reduced[r]) else "X") + " |"
        print(cells)
        print(tab + "|" + "___|" * l)

# Params: shape - 𝜆, a non-increasing integer list
#         s - 𝑠, size of a ribbon
# Return: A list of tuples (𝜆/𝑟, ht(𝑟)) for all ribbons 𝑟 of 𝜆 of size 𝑠
def reduce(shape, s):
    th_list = [] # list of (𝜆∖𝑟, ℎ(𝑟)) pairs
    
    border_size = [] # list containing number of border cells in every row
    for r in range(len(shape)):
        border_size.append(shape[r] if r == len(shape) - 1
                           else shape[r] - shape[r + 1] + 1)
    
    for r_start_idx in range(len(shape)):
        new_shape = shape.copy()
        
        removed = 0 # number of removed border cells
        r_idx = r_start_idx # index of row from which to remove cells
        while removed < s and r_idx < len(shape):
            rrem = min(border_size[r_idx], s - removed) # number of cells to remove from row at rem_idx
            new_shape[r_idx] -= rrem # remove cells from shape
            
            removed += rrem
            r_idx += 1
        
        # check that shape is valid and that exactly s cells have been removed
        if removed != s or (r_idx < len(shape) and new_shape[r_idx - 1] < new_shape[r_idx]):
            continue
        else:
            # remove 0s from new shape
            new_shape = list(filter(lambda x: x != 0, new_shape))
            th_list.append((new_shape, r_idx - r_start_idx - 1))
    
    return th_list

# Example
def show_reduced_tableaux(shape, s):
    print("An example with 𝜆 = " + str(tuple(shape)) + " and 𝑠 = " + str(s))
    print("This example shows all 𝜆/𝑟 for ribbons 𝑟 size 𝑠 (marked with X)" )
    print_tableau(shape)
    th_list = reduce(shape, s)
    
    for t, h in th_list:
        print_red_tableau(shape, t)
        print("height: ", h)

show_reduced_tableaux([5, 4, 4, 3], 4)

from IPython.display import display, Math

memo = {} # dictionary used to memoize already computed character values, 
          # so as to avoid multiple computation of the same characters

# Params: lda - 𝜆, non-increasing integer list
#         mu - 𝜇, non-increasing integer list
#         idx - (defaults to 0) index at which rho starts
#         print_flag - (defaults to False) whether to print the tableaux at every step
# Returns 𝜒𝜆_𝜌
def character(lda, mu, idx=0, print_flag=False):
    key = (tuple(lda), tuple(mu)) # to index into memo
    
    if key in memo: # return from memo if already computed
        if print_flag:
            print("\t\t"*(idx + 1) + "returns ", memo[key], "from memo")
        return memo[key]
    
    if idx == 0 and print_flag:
        print_tableau(lda)
    if len(lda) == 0 and idx == len(mu):
        if print_flag:
            print("\t\t"*(idx + 1) + "⊥")
            print("\t\t"*(idx + 1) + "returns 1")
        return 1
    
    th_list = reduce(lda, mu[idx])
    char = 0
    
    for t, h in th_list:
        if print_flag:
            print_red_tableau(lda, t, tab="\t\t"*(idx + 1))
        
        ind = -1 if h % 2 == 1 else 1
        char_t = character(t, mu, idx + 1, print_flag)
        char += ind * char_t
    
        if print_flag:
            print("\t\t"*(idx + 1) + "returns ", char_t)
    
    memo[key] = char
    return char

# Example
print("")
display(Math(r'Example: \chi_{(3, 3, 1, 1)}^{(5, 2, 1)}'))
print("\nCharacter value: ", character([5, 2, 1], [3, 3, 2], print_flag=True))

# Helper method for partitions below
def partitions_recursive(n, max_size):
    if n == 0:
        return [[]]
    
    max_size = min(max_size, n)
    p = []
    for i in range(max_size, 0, -1):
        p_pr = partitions_recursive(n - i, i)
        for part in p_pr:
            part.append(i)
            p.append(part)
    
    return p

# Params: n - int
# Returns: list of integer partitions of n (as non-increasing integer lists)
def partitions(n):
    p = partitions_recursive(n, n)
    for part in p:
        part.reverse()
    return p

from pandas import DataFrame

# Params: n - int
# Return: character table for 𝑆𝑛, as a pandas DataFrame indexed by partitions of 𝑛
def character_table(n):
    p = partitions(n)
    n_parts = len(p)
    mat = {}
    
    for j in range(n_parts):
        mat_row = []
        for i in range(n_parts):
            mat_row.append(character(list(p[i]), list(p[j])))
        mat[str(tuple(p[j]))] = mat_row
    
    return DataFrame(mat, index=[tuple(part) for part in p])

print("Character table of 𝑆_3")
table3 = character_table(3)
print(table3)

print("Character table of 𝑆_10")
table10 = character_table(10)
print(table10)