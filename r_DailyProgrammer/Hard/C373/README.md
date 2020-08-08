Today's challenge requires an understanding of trees in the sense of graph theory. If you're not familiar with the concept, [read up on Wikipedia](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29) or some other resource before diving in.

Today we're dealing with *unlabeled, rooted trees*. We'll need to be able to represent fairly large trees. I'll use a representation I just made up (but you can use anything you want that's understandable):

* A leaf node is represented by the string `"()"`.
* A non-leaf node is represented by `"("`, followed by the representations of its children concatenated together, followed by `")"`.
* A tree's representation is the same as that of its root node.

For instance, if a node has two children, one with representation `()`, and one with representation `(()())`, then that node's representation is `( + () + (()()) + ) = (()(()()))`. [This image illustrates the following example trees:](https://i.imgur.com/2lkQS07.jpg)

* `((()))`
* `(()())`
* `((())(()))`
* `((((()()))(()))((((()()))))((())(())(())))`

In this image, I've colored some of the nodes so you can more easily see which parentheses correspond to which nodes, but the colors are not significant: the nodes are actually unlabeled.

## Warmup 1: equal trees

The ordering of child nodes is unimportant. Two trees are equal if you can rearrange the children of each one to produce the same representation. [This image shows the following pairs of equal trees](https://i.imgur.com/dpS44kV.jpg):

* `((())()) = (()(()))`
* `((()((())()))(())) = ((())(()(()(()))))`

Given representations of two trees, determine whether the two trees are equal.

    equal("((()((())()))(()))", "((())(()(()(()))))") => true
    equal("((()))", "(()())") => false
    equal("(((()())())()())", "(((()())()())())") => false

It's easy to make a mistake, so I highly recommend checking yourself before submitting your answer! [Here's a list of 200 randomly-generated pairs of trees](https://gist.githubusercontent.com/cosmologicon/be38523b48f7da5ab9c886fca94a57b4/raw/37abb03b7365ff17056f7f59beb77d999fd6c81b/tree-equal.txt), one pair on each line, separated by a space. For how many pairs is the first tree equal to the second?

## Warmup 2: embeddable trees

One tree is *homeomorphically embeddable* into another - which we write as `<=` - if it's possible to label the trees' nodes such that:

* Every label is unique within each tree.
* Every label in the first tree appears in the second tree.
* If two nodes appear in the first tree with labels X and Y, and their [lowest common ancestor](https://en.wikipedia.org/wiki/Lowest_common_ancestor) is labeled Z in the first tree, then nodes X and Y in the second tree must also have Z as their lowest common ancestor.

[This image shows a few examples](https://i.imgur.com/YmNC3cR.jpg):

* `(()) <= (()())`
* `(()()) <= (((())()))`
* `(()()())` is not embeddable in `((()())())`. The image shows one incorrect attempt to label them: in the first graph, B and C have a lowest common ancestor of A, but in the second graph, B and C's lowest common ancestor is the unlabeled node.
* `(()(()())) <= (((((())()))())((()())))`. There are several different valid labelings in this case. The image shows one.

Given representations of two trees, determine whether the first is embeddable in the second.

    embeddable("(())", "(()())") => true
    embeddable("(()()())", "((()())())") => false

It's easy to make a mistake, so I highly recommend checking yourself before submitting your answer! [Here's a list of 200 randomly-generated pairs of trees](https://gist.githubusercontent.com/cosmologicon/dcf49d29c563dfc36a3d1c5053124be4/raw/9c663c5a9071571f041d11b08bf3c8958a22b3dd/tree-embed.txt), one pair on each line, separated by a space. For how many pairs is the first embeddable into the second?

## Challenge: embeddable tree list

Generate a list of trees as long as possible such that:

1. The first tree has no more than 4 nodes, the second has no more than 5, the third has no more than 6, etc.
2. No tree in the list is embeddable into a tree that appears later in the list. That is, there is no pair of indices i and j such that i < j and the i'th tree <= the j'th tree.

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/ajunxe/20190125_challenge_373_hard_embeddable_trees/