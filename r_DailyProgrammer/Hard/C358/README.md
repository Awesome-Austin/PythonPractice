# Description

First they took our jerbs, now they're taking our puzzles! (with your help)

Today we're gonna find a way to solve jigsaw puzzles using computers

# Input Description

As I am no designer the input will be purely numerical, feel free to make some visual version of the jigsaw puzzles :)

You will first be given the dimension as X, Y

Afterwards you will be given list of puzzle pieces and what type their 4 sides connect to (given as up, right, down, left)

Their side-connection is given as a number, They connect with their negated number

this means that a 1 and -1 connects, 2 and -2 connects etc.

0 means that it doesnt connect with anything.

Assume pieces are rotated in the correct direction.

fx:
  
    2, 2
    0: 0,1,2,0
    1: 0,0,2,-1
    2: -2,0,0,2
    3: -2,-2,0,0

# Output Description

Output is a 2D picture/matrix of the pieces in their correct position

for the example this would be 

    0 1
    3 2

# Challenge Input

Challenges are generated, so there is a slight chance of multiple solutions :P

##### 5 by 5

https://pastebin.com/raw/rgrAdmnd

##### 10 by 10

https://pastebin.com/raw/DRik2yrA

##### 100 by 100

https://pastebin.com/raw/J8U6GxhL

# Bonus

The pieces are randomly rotated and might need to be rotated to fit.

The example:

    0: 0,1,2,0
    1: 0,0,2,-1
    2: -2,0,0,2
    3: -2,-2,0,0

Could look like:

    0: 0,1,2,0
    1: 0,2,-1,0
    2: 2,-2,0,0
    3: -2,-2,0,0

# Bonus challenge

https://pastebin.com/Ut79qk3X

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/8fbqhw/20180427_challenge_358_hard_puzzle_me_this/