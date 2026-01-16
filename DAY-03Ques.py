'''Question – Decorators
	A module containing a function write_numbers_to_file(filename)
	Write a decorator called @execution_time that:
	1. Measures the execution time of a function
	2. Prints the function name and execution time
	3. Apply this decorator to a function that calculates the factorial of a number using recursion			'''


import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function Name: {func.__name__}")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(2)
print("Factorial Result:", result)


'''Question – Functions, Modules, File Handling & Exceptions 
Create a small Python package with: 
1. A module containing a function write_numbers_to_file(filename) 
2. The function should write numbers 1–100 into a file 
3. Handle possible exceptions such as: File not found Permission denied 
4. Create another module that imports this function and reads the file content safely'''


# writer

def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written to file successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)



# reader

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("File Content:\n")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)


# Program Execution
file_name = "numbers.txt"
write_numbers_to_file(file_name)
read_file(file_name)
