def main():
    book = read_text("books/frankenstein.txt")
    amount_of_words = count_words(book)
    print("--Start of Report--")
    print(f"{amount_of_words} words found in the document")
    collection = book.split()
    letters = count_letters(collection)
    sorted_list = dict_to_list(letters)
    sorted_list.sort(reverse=True, key=sort_on)
    new_lett = revert(sorted_list)
    print_letter(new_lett)
    print("--End--")


def read_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents


def count_words(content):
    words = content.split()
    count = len(words)
    return count


def count_letters(content):
    collection = {}
    for n in content:
        lowered = n.lower()
        for i in lowered:
            if i.isalpha():
                if i in collection:
                    collection[i]+=1
                else:
                    collection[i]=1
    return collection


def print_letter(content):
    for i in content:
        print(f"{i} is found {content[i]} times")


def dict_to_list(dict):
    list = []
    for i in dict:
        list.append({"name":i,"amount":dict[i]})
    return list


def sort_on(dict):
    return dict["amount"]


def revert(list):
    dict = {}
    for n in list:
        dict[n["name"]]=n["amount"]
    return dict


main()
