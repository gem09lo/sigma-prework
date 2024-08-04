#L3 Challenge 3: Task 2 - Max and Min
#python maxmin.py

def maxmin(numbers):
    numbers_ordered = sorted(numbers)
    max_min = []
    max_min.append(numbers_ordered[0])
    max_min.append(numbers_ordered[-1])
    return max_min

print(maxmin([20, 50, 12, 6, 14, 8]))
print(maxmin([100, -100]))
