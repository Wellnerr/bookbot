import stats
import sys

book = stats.book
count = stats.get_num_words()

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
stats.count_chars()
print("============= END ===============")
