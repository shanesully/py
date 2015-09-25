# shanesully

fizzbuzz = []

for num in [ num for num in range(1,101)]:
    if num%15 == 0:
        fizzbuzz.append("Fizzbuzz!")
    elif num%3 == 0:
        fizzbuzz.append("Fizz!")
    elif num%5 == 0:
        fizzbuzz.append("Buzz!")
    else:
        fizzbuzz.append(num)

print(fizzbuzz)

