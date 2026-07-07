"""
Problem: FizzBuzz variant
Print numbers 1..35. Multiples of 4 -> "Fizz",
multiples of 9 -> "Buzz", multiples of both -> "FizzBuzz".
"""

def fizzbuzz_variant(limit=35, a=4, b=9):
    out = []
    for i in range(1, limit + 1):
        if i % a == 0 and i % b == 0:
            out.append("FizzBuzz")
        elif i % a == 0:
            out.append("Fizz")
        elif i % b == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


if __name__ == "__main__":
    for line in fizzbuzz_variant():
        print(line)
