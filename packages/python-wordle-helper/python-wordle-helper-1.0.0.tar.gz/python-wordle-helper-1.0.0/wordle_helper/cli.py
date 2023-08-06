from argparse import ArgumentParser
import logging
from uuid import uuid4
from typing import List

import numpy as np
import requests
from wordfreq import zipf_frequency


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("wordle-helper")
WORDS_URLS = [
    "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/dde79fe924c5869e18d02d04c26f37db1c3c1553/wordle-nyt-answers-alphabetical.txt",
    "https://gist.githubusercontent.com/cfreshman/d5fb56316158a1575898bba1eed3b5da/raw/25d00e56705240135119d4b604d78c3d30c46094/wordle-nyt-allowed-guesses-update-12546.txt",
]


def filter_n_occurrences(letter: str, bounds: List[int], words: np.array) -> np.array:
    """
    Filters out words with fewer than `min` or greater than `max` occurrences of `letter`

    :param letter: The letter to filter out
    :type letter: str
    :param bounds: The minimum and maximum number of times the letter should occur
    :type min_: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)
    _max = max(bounds)
    _min = min(bounds)
    mask = [_max >= (word == ordinal).sum() >= _min for word in words]
    return words[mask]


def filter_out_letter(letter: str, words: np.array) -> np.array:
    """
    Removes all words containing the letter `letter`

    :param letter: The letter to filter out
    :type letter: str
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)
    mask = [ordinal not in word for word in words]
    return words[mask]


def filter_multiple_locations(
    letter: str, locations: int, count: List[int], words: np.array
) -> np.array:
    """
    Removes words without the letter `letter` and words with `letter` in at least one of the
    locations in `locations`

    :param letter: The letter to consider
    :type letter: str
    :param locations: The locations that the letter cannot be in
    :type locations: int
    :param count: The minimum and maximum number of times the letter must occur in the word
    :type count: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """
    ordinal = ord(letter)

    # Remove words containing `letter` at each given location
    for location in locations:
        words = words[words[:, location - 1] != ordinal, :]

    # Remove words not containing the desired occurrences of `letter`
    return filter_n_occurrences(letter, count, words)


def filter_single_location(
    letter: str, locations: List[int], count: List[int], words: np.array
) -> np.array:
    """
    Removes words without `letter` at `locations'.

    :param letter: The letter that must exist at `locations`
    :type letter: str
    :param locations: The locations that `letter` must be
    :type locations: List[int]
    :param count: The minimum and maximum number of times the letter must occur in the word
    :type count: List[int]
    :param words: The current list of remaining valid words
    :type words: np.array
    :rtype: np.array
    """

    for location in locations:
        # Remove words without `letter` at `location`
        words = words[words[:, location - 1] == ord(letter), :]

    # Remove words not containing the desired occurrences of `letter`
    return filter_n_occurrences(letter, count, words)


def guesses_to_constraints(guesses: List[str]) -> dict:
    """
    Parses the list of guesses into a dictionary. Each element of the list takes the form of
    <word>,<result>, where <word> is the word guessed and <result> is the result from Wordle after
    guessing. See the readme for more information.

    :param guesses: The list of guesses to interpret
    :type guesses: list[str]
    :rtype: dict
    """
    constraint_dict = {}
    for word_constraint in guesses:
        letters, colors = word_constraint.split(",")
        word_dict = {}

        # Parse individual guesses
        for position, (letter, operation) in enumerate(zip(letters, colors), 1):
            assert operation in ["b", "g", "y"]
            assert 1 <= position <= 5

            if letter not in word_dict:
                word_dict[letter] = {}
            if operation not in word_dict[letter]:
                word_dict[letter][operation] = []

            word_dict[letter][operation].append(int(position))

        # Post-process to determine min/max letter occurrences and combine individual guess
        # constraints with all previous constraints
        for letter, op_dict in word_dict.items():
            min_occ = 0
            max_occ = 5
            n_green = len(op_dict.get("g", []))
            n_yellow = len(op_dict.get("y", []))
            n_black = len(op_dict.get("b", []))

            if n_green:
                # There are at least `n_green` occurrences of `letter`
                min_occ = n_green

                if n_yellow:
                    # There is at least one more than `n_green` occurrences of `letter`
                    min_occ += 1
            elif n_yellow:
                # There is at least 1 occurence of `letter`
                min_occ = 1

            if n_black:
                # There are no more occurrences of `letter` than the identified minimum
                max_occ = min_occ

            # Update global constraints with current guess
            for op, positions in op_dict.items():
                if letter not in constraint_dict:
                    constraint_dict[letter] = {}
                if op not in constraint_dict[letter]:
                    constraint_dict[letter][op] = []
                constraint_dict[letter][op].extend(positions)

            if "c" in constraint_dict[letter]:
                min_max = constraint_dict[letter]["c"]
                if min_occ > min_max[0]:
                    min_max[0] = min_occ
                if max_occ < min_max[1]:
                    min_max[1] = max_occ
            else:
                constraint_dict[letter]["c"] = [min_occ, max_occ]

    return constraint_dict


def find_remaining_words(word_list: List[str], constraints: dict) -> List[str]:
    """
    Finds the words that are valid once all constraints are considered. Returns the list of valid
    words sorted by frequency of use in the English language.

    :param word_list:
    :type word_list: list[str]
    :param constraints:
    :type constraints: dict
    :rtype: list[str]
    """
    default_bounds = [1, 5]
    word_arr = np.array([[ch for ch in wd] for wd in word_list])
    for letter, letter_constraints in constraints.items():
        bounds = letter_constraints.get("c", default_bounds)
        if "b" in letter_constraints:
            word_arr = filter_out_letter(letter, word_arr)
        if "y" in letter_constraints:
            word_arr = filter_multiple_locations(letter, letter_constraints["y"], bounds, word_arr)
        if "g" in letter_constraints:
            word_arr = filter_single_location(letter, letter_constraints["g"], bounds, word_arr)

    word_lst = ["".join(chr(ch) for ch in word) for word in word_arr]
    word_lst.sort(key=lambda wrd: zipf_frequency(wrd, "en"), reverse=True)
    return word_lst


def get_word_list_from_urls(list_urls: List[str]) -> List[str]:
    """
    Returns a list of 5 letter words

    :param list_urls: The URLs from which to get the words list. The content in the response is
                      expected to be a newline-delimited string of words.
    :type list_urls: list[str]
    :rtype: list[str]
    """
    word_list = set(
        word
        for url in list_urls
        for word in requests.get(url, allow_redirects=True).content.split(b"\n")
    )
    return list(word_list)


def print_or_save_word_list(word_list: str, cutoff_len: int = 42) -> None:
    """
    Prints or saves the remaining word list, depending on its length

    :param word_list: The list of words to print or save to a file
    :type word_list: str
    :param cutoff_len: If `word_list` is `cutoff_len` or longer, the list is saved to a file
    :type cutoff_len: int
    :rtype: None
    """
    """"""
    if word_list:
        LOGGER.info(f"Found {len(word_list)} possibilites, the most common one is '{word_list[0]}'")
        if len(word_list) < cutoff_len:
            all_guesses = "\n".join(word_list)
            LOGGER.info(f"All valid guesses, sorted by frequency:\n{all_guesses}")
        else:
            fn = f"words_{uuid4().hex}"
            with open(fn, "w") as fp:
                for word in word_list:
                    fp.writelines(f"{word}\n")
            LOGGER.info(f"Check '{fn}' for all possibilites, sorted by frequency")
    else:
        LOGGER.warning("No choices found!")


def main() -> None:
    parser = ArgumentParser(description="Cheat at wordle!")
    parser.add_argument("guesses", type=str, nargs="+")
    parser.add_argument("-l", "--lists", type=str, nargs="+")

    args = parser.parse_args()
    guesses = args.guesses
    word_list_urls = args.lists or WORDS_URLS

    constraint_dict = guesses_to_constraints(guesses)
    word_list = get_word_list_from_urls(word_list_urls)
    remaining_words = find_remaining_words(word_list, constraint_dict)
    print_or_save_word_list(remaining_words)


if __name__ == "__main__":
    main()
