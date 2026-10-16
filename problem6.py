bins = int(input("Enter the number of bins: "))

total = 0
total_emp = 0

'''
                    #version1
for i in range (1, bins+1):
    bottle = int(input("Enter the bottle count: "))
    total += bottle
    if bottle == 0:
        total_emp += 1
'''

                    #version2
i = 1
while i <= bins:
    bottle = int(input("Enter the bottle count: "))
    total += bottle
    if bottle == 0:
        total_emp += 1
    i += 1


print(f"Total bottles: {total}")
print(f"Total empty bins: {total_emp}")
