# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(arr):
    arr.sort()
    if len(arr)%2 == 0:
        return int((arr[int(len(arr)/2)] + arr[int(len(arr)/2-1)])/2)
    else:
        return int(arr[int(len(arr)/2)])

N = int(input())
arr = list(map(int, input().rstrip().split()))
q2 = median(arr)
q1 = median(arr[:int(N/2)])
q3 = median(arr[round(N/2+0.1):])
print(q1)
print(q2)
print(q3)
