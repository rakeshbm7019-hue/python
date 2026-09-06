
numbers = [10, 20, 30, 40, 50]


print(numbers[1:4])
print(numbers[::-1])  


numbers.insert(2, 25)
print(numbers)       
numbers.extend([60, 70])
print(numbers)     
squares = [n**2 for n in numbers]
print(squares)

odds = [n for n in numbers if n % 2 != 0]
print(odds)

print(max(numbers))   
print(min(numbers))   
print(sum(numbers))   
