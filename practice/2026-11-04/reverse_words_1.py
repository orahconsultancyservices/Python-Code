"""
Problem: Reverse the order of words in a sentence.
Input: "small daily habits compound over time"
"""

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sentence = "small daily habits compound over time"
    print("Input: ", sentence)
    print("Output:", reverse_words(sentence))
