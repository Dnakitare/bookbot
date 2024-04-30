import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = word_count(text)
  num_letters = count_letters(text)

  # Print the original report
  print_report(num_letters, num_words, book_path)

def print_report(num_letters, num_words, path):
  print(f'--- Begin report for {path} ---')
  print(f'The total number of words in the text is {num_words}\n')
  
   # Create a DataFrame from the letter count dictionary
  letter_df = pd.DataFrame.from_dict(num_letters, orient='index', columns=['Count'])
  letter_df.index.name = 'Letter'
  letter_df.reset_index(inplace=True)

  # Print the DataFrame
  print(letter_df)

  print('\n--- End report ---')

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def word_count(file_contents):
  words = file_contents.split()
  return len(words)

def count_letters(file_contents):
  # convert file_contents to lowercase
  file_contents_lower = file_contents.lower()
  # lets remove any non-alphabetic characters
  file_contents_lower = ''.join(filter(str.isalpha, file_contents_lower))
  # count each letter using a dictionary
  count = dict(Counter(file_contents_lower))
  # return the sorted dictionary by value in descending order
  sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
  return sorted_count


main()

