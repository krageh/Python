def minmax(data):
    smallest = largest = data[0]
    for val in data:
        if val > largest: largest = val
        elif val < smallest: smallest = val
    return smallest, largest
