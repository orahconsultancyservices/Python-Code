"""
Problem: FizzBuzz variant
Print numbers 1..21. Multiples of 5 -> "Fizz",
multiples of 9 -> "Buzz", multiples of both -> "FizzBuzz".
"""

def fizzbuzz_variant(limit=21, a=5, b=9):
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
