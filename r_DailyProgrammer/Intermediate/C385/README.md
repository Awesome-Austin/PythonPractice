Today's challenge is to implement the solution to a well-known math puzzle involving prisoners and a chessboard. I won't state the puzzle or give the solution here, but you can find many writeups online:

* [Yet another prisoner puzzle](http://olivernash.org/2009/10/31/yet-another-prisoner-puzzle/index.html) blog post
* [Impossible Escape?](http://datagenetics.com/blog/december12014/index.html) blog post
* [The Almost Impossible Chessboard Puzzle video on Stand-Up Maths](https://www.youtube.com/watch?v=as7Gkm7Y7h4): 32 minutes

You need to know the solution for today's challenge, but you're welcome to look it up, either in those links or others. If you try to find the solution yourself, be warned it's pretty hard!

# Challenge

First, assume that there exists a function `flip` that takes a series of 64 bits (0 or 1) and a number from 0 to 63. This function returns the same series of bits with the corresponding bit flipped. e.g.:

    flip([0, 0, 0, 0, ...], 2) => [0, 0, 1, 0, ...]
    flip([0, 1, 0, 1, ...], 1) => [0, 0, 0, 1, ...]

Now, you need to write two functions.

Function `prisoner1` takes two inputs: a series `S` of 64 bits, and a number `X` from 0 to 63 (inclusive). It returns a number `Y` from 0 to 63.

Function `prisoner2` takes one input: a series `T` of 64 bits. It returns a number from 0 to 63.

Now, you must make it so that if you flip `S` using the output of `prisoner1` and pass the result to `prisoner2`, you get back the number `X`. Put another way, the following function must return `True` for every possible valid input `S` and `X`.

    def solve(S, X):
        Y = prisoner1(S, X)
        T = flip(S, Y)
        return prisoner2(T) == X

Essentially, `prisoner1` is encoding the value `X` into the sequence with a single flip, and `prisoner2` is decoding it. In the puzzle statement, `X` is the location of the key, `Y` is the coin that gets flipped, `S` is the starting state of the board, and `T` is the state after the flip occurs.

Good luck!

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/hrujc5/20200715_challenge_385_intermediate_the_almost/