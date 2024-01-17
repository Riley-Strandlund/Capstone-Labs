class Author:
    def __init__(self, authorName):
        self.name = authorName 
        self.books = [] # creates a list

    def publish(self, bookTitle):
        self.books.append(bookTitle) # adds book titles to 'self.books'. Call publish to add book title "dominic.publish('how to build a tree')""
    
    def __str__(self):
        book_list = ', '.join(self.books) # adds comma between listed books. join() adds all elements of an iterable into a single string.
        return f"\n\nName: {self.name}. Books: {book_list}"


def main():
    dominic = Author('Dominic Arbatelli')
    dominic.publish('How to Build a Tree?')
    dominic.publish('How to Build a Tree?') # Prints identical title. No duplicate preventions
    print(dominic)

    charlene = Author('Charlene Sucrox')
    charlene.publish('The Perfect Blend') # uses publish method to add a book under the authors name
    charlene.publish('The Secret Recipe')
    print(charlene)

main()