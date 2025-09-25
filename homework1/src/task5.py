# Task 5 - Lists and Dictionaries

# List of favorite books (title, author)
fav_books = [
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "Ender's Game", "author": "Orson Scott Card"},
    {"title": "The Cat in The Hat", "author": "Dr. Seuss"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
]

# Print first three books
def first_three():
    return fav_books[:3]


# Dictionary: student ID corresponds to student's name
student_db = {
    101: "John Smith",
    102: "Jane Doe",
    103: "Tony Stark",
    104: "Leroy Jenkins",
}

# Return student's name based off of a given ID number
def get_name(id: int):
    return student_db.get(id, None)



