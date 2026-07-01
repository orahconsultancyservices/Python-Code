#!/usr/bin/env python3
"""
Generates a small, real coding practice file each time it runs.

Every run:
  - picks a random problem template from PROBLEMS
  - fills in random parameters (so the same "type" of problem still looks different)
  - writes a real, working solution to practice/<date>/<slug>_<n>.py
  - appends a one-line log entry to practice/log.md

This produces genuine content (not empty/fake commits) - each file actually
contains a problem statement and a working solution you can read back later.
"""

import os
import random
import textwrap
from datetime import date, datetime

PRACTICE_DIR = "practice"
LOG_FILE = os.path.join(PRACTICE_DIR, "log.md")


def problem_two_sum():
    n = random.randint(6, 12)
    nums = random.sample(range(-20, 20), n)
    a, b = random.sample(range(n), 2)
    target = nums[a] + nums[b]
    code = textwrap.dedent(f'''
        """
        Problem: Two Sum
        Given nums = {nums} and target = {target},
        return the indices of the two numbers that add up to target.
        """

        def two_sum(nums, target):
            seen = {{}}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i
            return None


        if __name__ == "__main__":
            nums = {nums}
            target = {target}
            print("Input:", nums, "Target:", target)
            print("Result indices:", two_sum(nums, target))
    ''').strip() + "\n"
    return "two_sum", code


def problem_fizzbuzz_variant():
    a = random.randint(2, 5)
    b = random.randint(6, 9)
    limit = random.randint(20, 50)
    code = textwrap.dedent(f'''
        """
        Problem: FizzBuzz variant
        Print numbers 1..{limit}. Multiples of {a} -> "Fizz",
        multiples of {b} -> "Buzz", multiples of both -> "FizzBuzz".
        """

        def fizzbuzz_variant(limit={limit}, a={a}, b={b}):
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
    ''').strip() + "\n"
    return "fizzbuzz_variant", code


def problem_reverse_words():
    sentences = [
        "the quick brown fox jumps over the lazy dog",
        "practice makes progress not perfection",
        "small daily habits compound over time",
        "consistency beats intensity in the long run",
    ]
    s = random.choice(sentences)
    code = textwrap.dedent(f'''
        """
        Problem: Reverse the order of words in a sentence.
        Input: "{s}"
        """

        def reverse_words(sentence):
            return " ".join(sentence.split()[::-1])


        if __name__ == "__main__":
            sentence = "{s}"
            print("Input: ", sentence)
            print("Output:", reverse_words(sentence))
    ''').strip() + "\n"
    return "reverse_words", code


def problem_prime_check():
    n = random.randint(50, 500)
    code = textwrap.dedent(f'''
        """
        Problem: List all primes up to {n} using the Sieve of Eratosthenes.
        """

        def primes_up_to(n={n}):
            is_prime = [True] * (n + 1)
            is_prime[0:2] = [False, False]
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for multiple in range(i * i, n + 1, i):
                        is_prime[multiple] = False
            return [i for i, prime in enumerate(is_prime) if prime]


        if __name__ == "__main__":
            result = primes_up_to()
            print(f"Primes up to {n}:", result)
            print("Count:", len(result))
    ''').strip() + "\n"
    return "prime_sieve", code


PROBLEMS = [
    problem_two_sum,
    problem_fizzbuzz_variant,
    problem_reverse_words,
    problem_prime_check,
]


def write_snippet(index: int) -> str:
    today = date.today().isoformat()
    day_dir = os.path.join(PRACTICE_DIR, today)
    os.makedirs(day_dir, exist_ok=True)

    slug, code = random.choice(PROBLEMS)()
    filename = f"{slug}_{index}.py"
    filepath = os.path.join(day_dir, filename)

    with open(filepath, "w") as f:
        f.write(code)

    with open(LOG_FILE, "a") as f:
        f.write(f"- {datetime.now().isoformat(timespec='seconds')}: {filepath}\n")

    print(f"Wrote {filepath}")
    return filepath


def main():
    os.makedirs(PRACTICE_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# Daily practice log\n\n")

    # Number of snippets today, randomized (this is the "multiple tasks daily" part)
    count = int(os.environ.get("SNIPPET_COUNT", random.randint(1, 3)))
    for i in range(1, count + 1):
        write_snippet(i)


if __name__ == "__main__":
    main()
