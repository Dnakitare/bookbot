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

  # Additional insights using Pandas
  analyze_text(text)

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

def analyze_text(text):
  # Tokenize the text
  tokens = text.split()

  # Create a DataFrame from the word frequency count
  word_counts = pd.Series(tokens).value_counts().reset_index()
  word_counts.columns = ['Word', 'Frequency']

  # Print the top 10 most frequent words
  print('\n--- Top 10 most frequent words ---')
  print(word_counts.head(10))

  # Plot the distribution of word frequencies
  plt.figure(figsize=(10, 6))
  plt.bar(word_counts['Word'][:30], word_counts['Frequency'][:30], color='skyblue')
  plt.title('Top 30 Most Common Words')
  plt.xlabel('Word')
  plt.ylabel('Frequency')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show(block=False)
  
  # Prompt the user to save the plot as a PNG file
  save_plot = input('Would you like to save the plot? (y/n): ')
  if save_plot.lower() == 'y':
    file_name = input('Enter the file name: ')
    plt.savefig(f'{file_name}.png')
    print(f'Plot saved as {file_name}.png')

main()

