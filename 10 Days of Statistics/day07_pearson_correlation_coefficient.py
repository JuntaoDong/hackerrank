# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st
n = int(input())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))

sigma_x = st.pstdev(x)
mean_x = st.mean(x)
sigma_y = st.pstdev(y)
mean_y = st.mean(y)

#print(sigma_x, sigma_y, mean_x, mean_y)
print(round(sum((x[i]-mean_x)*(y[i]-mean_y)/(n*sigma_x*sigma_y) for i in range(n)), 3))