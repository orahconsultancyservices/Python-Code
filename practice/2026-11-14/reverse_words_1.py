"""
Problem: Reverse the order of words in a sentence.
Input: "consistency beats intensity in the long run"
"""

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sentence = "consistency beats intensity in the long run"
    print("Input: ", sentence)
    print("Output:", reverse_words(sentence))
