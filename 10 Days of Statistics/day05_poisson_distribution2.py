# Enter your code here. Read input from STDIN. Print output to STDOUT

x, y = map(float, input().strip().split())
Ex = x + x * x
Ey = y + y * y

print(round(160+40*Ex, 3))
print(round(128+40*Ey, 3))