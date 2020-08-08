# Definitions

Given two different strings of equal length, the *spacing* between them is the number of other strings you would need to connect them on a [word ladder](https://en.wikipedia.org/wiki/Word_ladder). Alternately, this is 1 less than the number of letters that differ between the two strings. Examples:

    spacing("shift", "shirt") => 0
    spacing("shift", "whist") => 1
    spacing("shift", "wrist") => 2
    spacing("shift", "taffy") => 3
    spacing("shift", "hints") => 4

The *total spacing* of a word list is the sum of the spacing between each consecutive pair of words on the word list, i.e. the number of (not necessarily distinct) strings you'd need to insert to make it into a word ladder. For example, the list:

    daily
    doily
    golly
    guilt

has a total spacing of 0 + 1 + 2 = 3

# Challenge

Given an input list of unique words and a maximum total spacing, output a list of distinct words taken from the input list. The output list's total spacing must not exceed the given maximum. The output list should be as long as possible.

You are allowed to use existing libraries and research in forming your solution. (I'm guessing there's some graph theory algorithm that solves this instantly, but I don't know it.)

# Example input

    abuzz
    carts
    curbs
    degas
    fruit
    ghost
    jupes
    sooth
    weirs
    zebra

Maximum total spacing: 10

# Example output

The longest possible output given this input has length of 6:

    zebra
    weirs
    degas
    jupes
    curbs
    carts

# Challenge input

[This list of 1000 4-letter words randomly chosen from enable1](https://gist.githubusercontent.com/cosmologicon/0a4448e8fdb79ee620a68ed131eac58e/raw/a8831d08019f73e7d5a52042e2c4afe6fea70011/363-hard-words.txt).

Maximum total spacing of 100.

My best solution has a length of 602. How much higher can you get?

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/99yl83/20180824_challenge_366_hard_incomplete_word/