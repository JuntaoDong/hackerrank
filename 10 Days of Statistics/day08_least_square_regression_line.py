# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st
x = []
y = []

for i in range(5):
    n, m = map(int, input().strip().split())
    x.append(n)
    y.append(m)

sigma_x = st.pstdev(x)
mean_x = st.mean(x)
sigma_y = st.pstdev(y)
mean_y = st.mean(y)
n = len(x)

p = sum((x[i]-mean_x)*(y[i]-mean_y)/(n*sigma_x*sigma_y) for i in range(n))
b = p * sigma_y / sigma_x
a = mean_y - b * mean_x

print(round(a+b*80, 3))