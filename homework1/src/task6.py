# Task 6 - File Handling and Metaprogramming

# Count the words
def word_count(filename):
    with open(filename, "r") as file:
        doc = file.read()

    words = doc.split()
    return len(words)    

