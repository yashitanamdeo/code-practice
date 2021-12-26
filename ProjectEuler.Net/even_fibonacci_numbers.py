'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

n1, n2 = 0, 1
count = 0
numbers = []
while count < 4000000:
    numbers.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print(sum(numbers))