"""
Problem: Reverse the order of words in a sentence.
Input: "the quick brown fox jumps over the lazy dog"
"""

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sentence = "the quick brown fox jumps over the lazy dog"
    print("Input: ", sentence)
    print("Output:", reverse_words(sentence))
