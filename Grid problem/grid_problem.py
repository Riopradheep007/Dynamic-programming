

"""
problem statement
  1.In a grid your are standing in the top left corner you have to reach the bottom right corner.
    your can move only right  and bottom.
    
    start
    |----|-----|-----|
    |----|-----|-----|                
    |----|-----|-----|end
    
"""

""" without using memization    complixity is O(n^2)"""








def grid(row,column):
    if row==1 and column==1:
        return 1
    elif row==0 or column==0:
        return 0
    return grid(row-1,column)+grid(row,column-1)
print("normal code")
print(grid(2,3))
    

"""  using dynamic programming """

def grid(row,column,memo={}):
    key=str(row)+","+str(column)
    if key in memo:
        return memo[key]
    if row==1 and column==1:
        return 1
    elif row==0 or column==0:
        return 0
    memo[key]=grid(row-1,column)+grid(row,column-1)
    return memo[key]
print("dynamic programming")
print(grid(18,18))
