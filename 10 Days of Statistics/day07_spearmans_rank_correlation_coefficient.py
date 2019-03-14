# Enter your code here. Read input from STDIN. Print output to STDOUT

def rank(lst):
    lst_sort = list(sorted(set(lst)))
    return [lst_sort.index(x)+1 for x in lst]

n = int(input())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))
x_rank = rank(x)
y_rank = rank(y)

r = 1 - 6 * sum((x_rank[i] - y_rank[i])**2 for i in range(n))/(n*(n**2-1))
print(round(r, 3))