def main():
    book_path = "books/frankenstein.txt"
    #print(book_path)
    book_text = read_book(book_path)
    #print(book_text)
    c_words = count_words(book_text)
    #print (c_words)
    c_char = count_char(book_text)
    #print(c_char)

def read_book(bp):
    with open(bp) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    cw = len(text.split())
    #print(cw)
    return cw

def count_char(text):
    text_lowered = text.lower()
    result_dic = {}
    for letter in text_lowered:
        if letter in result_dic:
            result_dic[letter] += 1
        else:
            result_dic[letter] = 1
    #print(result_dic)
    return result_dic

main()