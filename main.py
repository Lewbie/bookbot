def main():
    with open("books/frankenstein.txt") as book:
        open_book = book.read()
        word_total = word_count(open_book)
        l_dict = letter_count(open_book)
        report(l_dict, word_total)

    #returns the total word count
def word_count(book):
    words_total = len(book.split())
    return words_total

    #returns the number of times each character appears
def letter_count(book):
    total = book.lower()
    dict = {}
    for i in range(len(total)):
        if total[i] in dict:
            dict[total[i]] += 1
        else:
            dict[total[i]] = 1
    return dict

def report(dict,count):
    #converting dictionary of letter:count pairs into a list of dictionaries
    letter_list = []
    for key, value in dict.items():
        pair = {"letter":key,"count":value}
        letter_list.append(pair)
    
    #sorting the order
    letter_list.sort(reverse=True,key=sort_on)

    #printing out the report
    print("  --- Begin report of books/frankenstein.txt ---")
    print(f"\t{count} words found in the document\n")
    for i in range(len(letter_list)):
        if letter_list[i]["letter"].isalpha():
            print(f"\tThe '{letter_list[i]['letter']}' character was found {letter_list[i]['count']} times")      
    print("\t\t--- End report ---")

    #function for sorting the order
def sort_on(dict):
    return dict["count"]

main()