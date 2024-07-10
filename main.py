def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = word_count(file_contents)
        dict = letter_count(file_contents)
        report(dict,count)

def word_count(book):
    words = len(book.split())
    return words

def letter_count(book):
    letter = book.lower()
    letter_dict = {}
    for i in range(len(letter)):
        if letter[i] in letter_dict:
            letter_dict[letter[i]] += 1
        else:
            letter_dict[letter[i]] = 1
    return letter_dict
    
def report(dict,count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(count) + " words found in the document\n")
    for i in range(len(dict)):
        print(dict)
        
    print("--- End report ---")

main()