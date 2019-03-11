# py-anagram

Simple script in Python3 to iterate through combinations and permutations
of a word or group of letters. Basically made it as a cheat for Wordscapes.

## usage
Just run main.py to generate and dump a list of anagrams. To train the
word list, run main(training=True):
 ```python

 # dump list
 if __name__ == '__main__':
    main()

 # iterate list with options to add/delete words
 if __name__ == '__main__':
    main(training=True)
 ```
