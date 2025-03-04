import sys
from stats import count_words

char_count = {}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path) as f:
        files_contents = f.read()

    lowercased_text = to_lower(files_contents)
    count_char_occurence(lowercased_text)
    char_sorted_count = sort_dict(char_count)
    word_count = count_words(lowercased_text)
    gen_report(book_path, word_count, char_sorted_count)

    #print(char_count) #prints number of character appeared
    #print(f"Word count: {word_count}") #prints word count

def to_lower(text):
    return text.lower()

def count_char_occurence(text):
    for character in text:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

def sort_dict(unsorted_dict):
    sorted_dict = sorted(unsorted_dict.items(), reverse = True, key=lambda x:x[1])
    return dict(sorted_dict)

def gen_report(book_path, word_count, char_sorted_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, num in char_sorted_count.items():
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")

main()