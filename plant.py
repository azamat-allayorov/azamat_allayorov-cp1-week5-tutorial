heights = []

n = int(input("enter the number of days: "))

for i in range (1, n+1):
    m = int(input(f"enter day {i} height: "))
    heights.append(m)

print()

for i in range (1, n+1):
    print(f"Day {i}: {heights[i-1]} cm")

print()

change = heights[-1] - heights[0]

print(f"first day height: {heights[0]}")
print(f"last day height: {heights[-1]}")
print(f"change: {change}")
