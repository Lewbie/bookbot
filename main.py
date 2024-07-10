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
    letter_list = []
    for k, v in dict.items():
        pair = {"letter":k,"count":v}
        letter_list.append(pair)
    letter_list.sort(reverse=True,key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(count) + " words found in the document\n")
    
    for i in range(len(letter_list)):
        if letter_list[i]["letter"].isalpha():
            print("The '" + letter_list[i]["letter"] + "' character was found " + str(letter_list[i]["count"]) + " times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()