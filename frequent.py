from collections import Counter

def most_frequent_number(lst):
    if not lst:
        return None
    count = Counter(lst)
    return count.most_common(1)[0][0]

numbers = [1, 3, 1, 3, 2, 1]
print(most_frequent_number(numbers))  
