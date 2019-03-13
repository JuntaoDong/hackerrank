# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
ar = list(map(int, input().rstrip().split()))

# Mean
mean = sum(ar)/len(ar)

# Median
ar.sort()
if N%2 == 0:
    median = (ar[int(N/2)] + ar[int(N/2-1)])/2
else:
    median = ar[round(N/2-1)]

# Mode
mode = max(ar, key=ar.count)
print("%.1f" % mean)
print("%.1f" % median)
print(mode)
