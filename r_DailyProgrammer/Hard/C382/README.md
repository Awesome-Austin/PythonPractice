Given the numbering of a crossword puzzle's clues, find its grid.

# Background

For the purpose of today's challenge, a standard American crossword grid (like you would typically find in the New York Times) is an odd-dimension square grid of black and white squares with the following requirements:

1. The grid has 180 degree rotational symmetry.
2. The white squares form a single connected component. Squares are connected horizontally or vertically.
3. Every word is at least 3 letters long. A word is a horizontal (Across) or vertical (Down) run of white squares.
4. Every white square is checked, meaning it appears in both an Across word and a Down word. (Equivalently, there are no 1-letter words either.)

[Here are some examples of valid and invalid grids](https://gist.github.com/cosmologicon/918623145c549b9b4968d690550b3662), using `.` for white squares and `#` for black squares.

Some of the squares in the crossword grid are numbered ([here's an example if you're not familiar with crosswords](https://en.wikipedia.org/wiki/Crossword#/media/File:CrosswordUSA.svg)). The numbers that appear in the grid are determined by the layout of black and white squares in the grid as follows:

The first white square in each word is numbered, starting at 1, then 2, 3, etc. "First" here means the leftmost square for Across clues, and the topmost square for Down clues. If a square is the first square in both an Across word and a Down word, it only gets one number. The numbering starts at the top left and goes left to right and then top to bottom.

The set of Across word numbers is the numbers in the squares that start Across clues, and the set of Down word numbers is the numbers in the squares that start Down clues.

# Challenge

Given a grid size and two lists of Across word numbers and Down word numbers, find a valid grid that matches the numbers. Inputs are guaranteed to have at least one valid solution, but it's not guaranteed to be unique. Any valid output that matches the input is acceptable.

To complete this challenge, you must run your program all the way through to completion for at least one challenge input.

# Example input

You are not required to use any particular input/output format. Feel free to hard code the input into your program.

    EXAMPLE: 15x15
    A: 1,4,7,10,13,14,16,17,18,20,21,23,24,26,28,29,33,35,36,38,39,42,44,45,47,49,50,52,55,56,58,59,61,63,67,69,70,71,72,73,74,75,76
    D: 1,2,3,4,5,6,7,8,9,11,12,15,19,22,25,27,29,30,31,32,34,37,40,41,43,46,48,51,53,54,57,60,62,64,65,66,68


# Example output

    . . . # # # . . . # . . . # #
    . . . . . # . . . # . . . . #
    . . . . . # . . . # . . . . .
    . . . . . # . . . . # . . . .
    # # # . . . # . . . . # . . .
    . . . . . . . # . . . . . . .
    . . . # # . . . # . . . . . .
    . . . . . # . . . # . . . . .
    . . . . . . # . . . # # . . .
    . . . . . . . # . . . . . . .
    . . . # . . . . # . . . # # #
    . . . . # . . . . # . . . . .
    . . . . . # . . . # . . . . .
    # . . . . # . . . # . . . . .
    # # . . . # . . . # # # . . .

# Challenge inputs

    #1: 15x15
    A: 1,6,10,12,13,14,16,17,19,20,21,23,25,27,29,30,31,33,34,35,37,38,40,41,42,44,45,46,49,50
    D: 1,2,3,4,5,6,7,8,9,10,11,12,15,17,18,20,21,22,24,26,28,32,33,36,39,41,43,45,47,48

    #2: 21x21
    A: 1,4,7,10,12,14,16,17,18,19,21,24,25,26,27,29,30,32,34,35,36,38,39,40,42,45,46,48,49,51,52,54,55,56,57,58,59,61,63,64,66,67,69,70,73,74,75,76,77,79,81,82,84,85,87,89,90,92,94,96,97,99,100,101,102,103,104,105
    D: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20,22,23,24,28,31,33,37,38,41,42,43,44,45,47,50,52,53,60,62,63,64,65,67,68,71,72,74,78,80,81,83,84,86,88,89,91,93,95,98

    #3: 27x27
    A: 1,5,10,15,18,22,25,27,29,32,33,34,35,36,37,38,39,40,42,44,46,47,48,49,51,52,54,55,56,57,59,61,65,67,69,70,71,73,74,77,80,82,84,86,87,88,89,91,93,94,96,99,101,102,103,104,106,108,110,112,114,115,116,119,121,123,125,126,128,129,132,133,135,136,138,139,140,142,144,147,148,149,151,153,154,156,158,162,166,167,169,170,171,173,174,176,177,178,179,181,182,185,186,187,188,189,191,192,193,195,201,202,203,204,205,206,207,208
    D: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,26,28,30,31,37,39,40,41,43,45,46,47,50,53,54,55,56,58,60,62,63,64,66,68,72,74,75,76,78,79,81,83,85,88,90,92,94,95,97,98,100,103,105,106,107,109,111,113,117,118,120,122,124,127,128,130,131,134,137,139,141,143,144,145,146,148,150,152,155,157,159,160,161,163,164,165,168,172,175,176,177,178,180,181,183,184,185,186,190,192,193,194,196,197,198,199,200

    #4: 33x33
    A: 1,5,13,19,23,25,28,29,30,33,34,35,36,37,38,42,43,48,49,50,51,56,58,60,61,62,64,65,66,67,68,69,70,71,72,73,76,78,79,80,81,83,86,88,89,90,93,94,96,100,101,102,105,107,108,109,110,111,112,114,116,117,118,120,121,122,126,127,128,130,131,133,134,135,138,139,141,142,143,145,146,149,151,152,154,155,159,160,163,165,166,167,168,172,173,174,175,176,178,180,181,183,185,187,188,189,190,191,192,193,194,197,199,200,201,202,203,205,207,208,209,210,212,213,215,216,217,220,222,223,224,226,227,228,230,233,234,235,236,238,242,244,246,247,248,249,250,252,253,254,255,256,259,260,263,265,271,276,277,278,279,280,281,282
    D: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,35,38,39,40,41,42,43,44,45,46,47,51,52,53,54,55,56,57,59,61,63,73,74,75,77,82,83,84,85,87,88,89,90,91,92,95,97,98,99,100,101,102,103,104,106,110,113,115,116,118,119,123,124,125,126,127,129,132,134,135,136,137,140,142,143,144,147,148,149,150,151,153,154,156,157,158,159,160,161,162,164,167,168,169,170,171,176,177,178,179,182,184,185,186,187,192,194,195,196,198,201,202,204,206,208,209,211,213,214,215,216,217,218,219,221,223,225,226,229,231,232,233,237,239,240,241,243,244,245,248,251,253,255,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/etf0al/20200124_challenge_382_hard_crossword_grids/