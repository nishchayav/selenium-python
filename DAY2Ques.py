'''Topic: Iterators & Generators
1. Create a custom iterator class that iterates over numbers from 1 to N
2. Create a generator function that yields the first N Fibonacci numbers
3. Demonstrate the difference between using the iterator and generator by printing values using a for loop'''


class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

print("Using Iterator:")
for num in NumberIterator(10):
    print(num)



def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nUsing Generator:")
for num in fibonacci(10):
    print(num)

