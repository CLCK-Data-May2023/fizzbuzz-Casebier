number_list = range(101)
for i in number_list:
    if i > 0 and i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    if i > 0 and i % 5 == 0 and not i % 3 == 0: 
        print("Buzz")
    if i > 0 and i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i > 0 and i % 3 > 0 and i % 5 > 0:
        print(i)# add your code here

