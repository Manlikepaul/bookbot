def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Add this new function here
def get_sorted_chars(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        
        # Modify your print statements to match the format
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        
        # Get the sorted list and print each character count
        char_list = get_sorted_chars(char_count)
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
        
        print("--- End report ---")

if __name__ == '__main__':
    main()