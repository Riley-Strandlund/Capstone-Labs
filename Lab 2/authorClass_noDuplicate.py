class Author:
    def __init__(self, authorName):
        self.name = authorName
        self.books = []

    def publish(self, bookTitle):
        if bookTitle in self.books: # using 'in' allows code to compare bookTitle to the items in the array without using a for loop. Some cases it may not be good to use though.
            print(f'\nThe book "{bookTitle}" is already published.')
        else:
            self.books.append(bookTitle)
        #for book in self.books: #iterates through self.books array
            #if book != bookTitle: #compares books in array to the book attempting publication
                #self.books.append(bookTitle)
            #else:
                #print("error cannot publish same title")
    
    def __str__(self):
        book_list = ', '.join(self.books) # takes all things in a list and makes a string out of it.
        return f"\n\nName: {self.name}. Books: {book_list}"


def main():
    dominic = Author('Dominic Arbatelli') # sets authors name or the first arguments value
    dominic.publish('How to Build a Tree?') #anything with .publish attempts to publish a book
    dominic.publish('How to Build a Tree?')
    print(dominic)

    charlene = Author('Charlene Sucrox') 
    charlene.publish('The Perfect Blend')
    charlene.publish('The Secret Recipe')
    print(charlene)

main()