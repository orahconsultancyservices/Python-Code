"""
Problem: Reverse the order of words in a sentence.
Input: "practice makes progress not perfection"
"""

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sentence = "practice makes progress not perfection"
    print("Input: ", sentence)
    print("Output:", reverse_words(sentence))
