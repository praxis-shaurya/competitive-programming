t = int(input()) 
for _ in range(t): # Read A, B, C from the current line 
    a, b, c = map(int, input().split()) 
    # Check if the average of A and B is strictly greater than C 
    if (a + b) / 2 > c: 
        print("YES") 
    else: 
        print("NO")

'''
Basic Manipulation

input().split() breaks "5 9 6" at spaces into a list of strings: ['5', '9', '6'].

map(int, ...) converts each string in that list to an integer.

Note - Don’t close brackets of 

Unpacking ( a, b, c = ... ) assigns the three integers directly to your variables.
Iterable Unpacking (or Sequence Unpacking)

x, y = [10, 20]

# x = 10 and y = 20

# same with tuples, strings, range


print("YES" if (a + b) > 2 * c else "NO")

This is a good habit, have inequalities linear to avoid having float errors and use if else in a single line (ternary operator)





'''
