def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  letters = get_letter_count(text)
  sorted_letters = sort_letters(letters)
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document\n")
  for letter in sorted_letters:
    print(f"The '{letter['letter']}' character was found {letter['count']} times")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_letter_count(text):
  letter_count = {}
  for letter in text:
    lowered = letter.lower()
    if lowered.isalpha():
      if lowered in letter_count:
        letter_count[lowered] += 1
      else:
        letter_count[lowered] = 1
  return letter_count

def sort_letters(dict):
  letter_list = [
    {'letter': key, 'count': value} for key, value in dict.items()
  ]
  sorted_letters = sorted(letter_list, key=lambda x: x['count'], reverse=True)
  return sorted_letters


main()