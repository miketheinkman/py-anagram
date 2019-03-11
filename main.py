import json
from itertools import permutations, combinations
from time import sleep

# establish wordlist
with open('adjusted_words.json') as f:
    words = json.load(f)
    start_len = len(words)
    print(start_len)


def record_changes():
    print("\n\nUpdating wordlist. ")
    with open('adjusted_words.json', 'w') as f:
        json.dump(words, f)
        print("Start length: {}".format(start_len))
        print("End length: {}".format(len(words)))


def main(training=False):
    """
    Print each possible wordlist verified permutation one at a time with option to delete or add
    words to wordlist

    returns None
    """

    # used try to catch ctrl+c and do some cleanup
    try:

        # get letters for combinations/permutations
        word = input("Enter word to generate anagrams")
        count = len(word)
        reduce = 0
        results = []

        # iterate all combinations from full length down to 3 letters
        while count - reduce >= 3:
            combination = combinations(word, count - reduce)

            # for all combinations iterate all permutations
            for c in combination:
                permutation = permutations(c, count - reduce)

                # check each permutation against wordlist and store in list
                for p in permutation:
                    perm = ''.join(p)
                    if perm in words and perm != word and perm not in results:
                        results.append(perm)

            # reduce length of combinations by 1
            reduce += 1

        # eliminate possible duplicates with set and print all anagrams
        results.sort(key=len, reverse=True)
        for num, result in enumerate(results):

            if training:
                # add new words, delete bogus words, or pass if word is good
                print("{} out of {}: {}".format(num, len(results), result))
                action = input("To delete, press 'D'. To add word, press 'A'. To continue, hit ENTER.")
                if action.lower() == 'a':
                    new_word = input("Enter new word.")
                    words[new_word] = 1
                elif action.lower() == 'd':
                    words.pop(result, None)
                else:
                    pass

            else:
                # dump list
                print("{} out of {}: {}".format(num, len(results), result))

        # write modified wordlist to file
        record_changes()

    # write modified wordlist to file if KeyboardInterrupt
    except KeyboardInterrupt:
        record_changes()
        sleep(3)


if __name__ == '__main__':
    main(training=False)
