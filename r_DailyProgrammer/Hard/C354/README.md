# Background

The *integer complexity* of a positive integer is the minimum possible sum of the numbers used in an expression - using only positive integers, addition, multiplication, and parentheses - that's equal to the given number. See [this week's Intermediate challenge](https://www.reddit.com/r/dailyprogrammer/comments/84f35x/20180314_challenge_354_intermediate_integer/?st=jerrhz81&sh=b536ffb2) for examples and more information.

The typical definition of integer complexity disallows all numbers in the expression other than 1. This definition is equivalent, so either one you want to use is fine.

As far as I know, efficiently determining the integer complexity of a given number is an open question. Your challenge is to provide as tight an upper limit as possible for a particular input.

# Challenge

Post an expression equal to 12345678910111213 - using only positive integers, addition, multiplication, and parentheses - such that the sum of the numbers in the expression is as small as possible.

Here's one example:

    1+4*3*3*3*(1+4*4*(1+3*(1+3*(1+5*3*3*(1+5*4*4*2*(1+4*3*(1+4*4*3*2*(2+5*(1+5*4*3*(1+3*(1+5*3*(2+5*1))))))))))))

If you add up all the numbers in this expression (`1+4+3+3+3+...+2+5+1`) you get a sum of 122. How much better can you do? When this post is 7 days old, the expression with the smallest sum will merit +1 gold medal flair.

# Challenge details

Don't worry about formatting it neatly. Output format doesn't matter as long as you can explain how to make sense of it.

In the event of a tie, also post an expression for 1234567891011121314, 123456789101112131415, etc. I'll break ties by looking at the first sum where your solutions differ.

If you post your solution to this thread, it's fair game for others to work off. You may PM me your solution instead of posting if you don't want people to use them for their own solutions, but it would be great if you also post the sum here so people have a goal to work for. I will verify anybody's claim, so for instance you can comment, "I found an expression with a sum of 118" and PM me the expression, and then I'll reply to your comment saying that I have confirmed that your expression is valid. After 10 days I'll post anybody's solution who PM'd me but didn't post it, so everything will eventually be public.

I reserve discretion to give the award to whoever made the largest contribution to the best solution, if my criterion would technically give it to someone else. But if you feel this is unfair, let me know and we'll work it out.

# Further reading

You are certainly allowed to use existing published literature and algorithms, if you want. There are a few papers on the asymptotic behavior of the integer complexity function, but I don't know how useful that is for this challenge.

If you do go that route, I recommend [starting with the links at OEIS](http://oeis.org/A005245). In particular, I found [this excellent program by Martin Fuller](https://oeis.org/A005245/a005245.c.txt) that can compute all integer complexities up to a few billion in a reasonable amount of time. The technique used in this program is I believe the same one written up in [this paper by de Reyna and van de Lune](https://arxiv.org/abs/1404.2183).

And of course, if you want to just start from scratch, that's perfectly valid too. I don't think it's necessary to use any existing work to have a good shot at winning this challenge. Good luck!

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/84uk5v/20180316_challenge_354_hard_integer_complexity_3/