# Description

A Nonogram (picross or griddlers) is a puzzle where you are given a grid with numbers indicating how many cells should be colored in that row/column. [example.](https://en.wikipedia.org/wiki/Nonogram) The more complex the grid is, the longer it can take to solve the puzzle.

# Formal Inputs and Outputs

## Inputs

	num columns
	num rows
	columns
	rows

## Output

Draw the solved nonogram.

## Example Input

	5
	5
	"5","2,2","1,1","2,2","5"
	"5","2,2","1,1","2,2","5"


## Example Output

    *****
    ** **
    *   *
    ** **
    *****


# Bonus Challenge

Include color in your input (note: colors don't necessarily have a space between the numbers)

# Credit

This challenge was suggested by /u/bmac951, many thanks! Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideas and there's a good chance we'll use it.

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/am1x6o/20190201_challenge_374_hard_nonogram_solver/