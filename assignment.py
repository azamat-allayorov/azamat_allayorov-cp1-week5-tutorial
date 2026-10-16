count = int(input("Enter the number of rice bags: "))

def classify(value):
    if value < 498:
        return "Below range"
    elif value <= 502:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return round(total/count, 1)

total = 0
below = 0 
in_range = 0
above = 0

for i in range(count):

    value = int(input("Enter the rice bag weight: "))
    total += value
    result = classify(value)
    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range += 1
    else:
        above += 1
    print(result)

print(f"Total weight: {total} g")
print(f"Average weight: {calculate_average(total, count)} g")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")
