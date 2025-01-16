char_count = {}

def main():
    with open("books/frankenstein.txt") as f:
        files_contents = f.read()

    lowercased_text = to_lower(files_contents)
    count_char_occurence(lowercased_text)
    word_count = count_words(lowercased_text)
    gen_report(word_count)

    #print(char_count) #prints number of character appeared
    #print(f"Word count: {word_count}") #prints word count

def count_words(text):
    words = text.split()
    return len(words)

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

def gen_report(word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    sorted_char_count = sort_dict(char_count)
    for char in sorted_char_count:
        if char.isalpha():
            char_occured = sorted_char_count[char]
            print(f"The '{char}' character was found {char_occured} times")

    print("--- End report ---")

main()