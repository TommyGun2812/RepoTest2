def average(numbers): 
    sum = 0

    for i in numbers: 
        sum += i
    
    return sum / len(numbers)

print(f"The average is: {(average([1,2,3]))}")