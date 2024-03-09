def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  letters = get_letter_count(text)
  print(f"--- Begin report of {book_path} ---")

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
    if lowered in letter_count:
      letter_count[lowered] += 1
    else:
      letter_count[lowered] = 1
  return letter_count

main()