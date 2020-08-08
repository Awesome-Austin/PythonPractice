*Smooshed Morse code* means Morse code with the spaces between encoded letters left out. [See this week's Easy challenge for more detail.](https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/) We'll also be stripping all punctuation, capitalization, and spacing, so the only encoded characters are the letters a-z.

Your challenge today is to decode smooshed Morse code representations of English text. As I said in the Easy challenge, the decoding is ambiguous. You're not expected to do a perfect job, but the more your output resembles English, the better you're doing. You are not expected to reproduce the punctuation, just the spacing between words.

A standard approach involves training on a corpus of English text. Last time I posted a similar challenge, [u/dreugeworst got excellent results this way](https://www.reddit.com/r/dailyprogrammer/comments/1z6flq/022814_challenge_151_hard_reemvoweler_2/cfqy5mx/). You can use any training data sources you want, but your program must run autonomously on the input, without human intervention.

The challenge inputs this time are all English-language movie quotes, some of which involve proper names, contractions (without the apostrophe), or other words you might not find in a standard word list.

(I have no idea how difficult this is, so I'll be happy to provide challenge inputs that are easier/harder/shorter/longer/whatever.)

# Example input

    -.---..--.....--.--..-..-.--....--.--..-.--.-.....--.-......-....-......-...-.-......-.--.--.--

# Example output

    no im simply saying that life uh finds a way

# Challenge inputs

Input 1

    ......---.--..--...-....-..-----.....-..-.--.-.-.-..-.--.-....-.-.-.....--..-..-...-.--.-...--..--.----.-.--..--...-.-.-.....--.--.....----.-.....-.-..----..-.-.-..-....--...-........-.---.-.....-..-.-.-.---.--.--...-....-...----....----.---.-..-..--...-...-..-.-.-..----.

Input 2 (contains proper names)

    ...--.--.-----.......---.---.-----..-...-----.-......-.--.....----.--.-.-..-..---......-...--.-...-..-------.--.-..-..---.....-...-....-....-.-...-.-.....-.--.---...-..-.-.--.-.-....--..-.-....-.--..--....-.---.....-...-..-..----...--.....-.-.-----..--.-..--......-...-.-.-----.---.--..-.-..-......--..-...-.-..----..-..-.---.........----..-.-..--.-....-.-..--.-....-.-..-..--.-.----.-.-.---.-...-...-..-...-.--.---..-...-.-..--....-.....-...-..--...-.---......---.-.--..--...........--...-.-.----.-.-..--.-.----.-.....--....---.-.-.....---.....-.--..--..-.-----.....-..-.-..-.-.-..-.--.--.-.--.-..-...-..-...--....---.-...-..-.-----.---..-.......--........-.....-.-.......---..-......--..-...-...-.-....-...-.-.......

Input 3

    -.-----..-.-..-......-.......-..........------..-..-.-..--.-..-.-....-.---..-..--...--.-....-.-...--.-.-..-...--.-..-.--..----...-.......-..-.------......--..-.-----..-..-----..-.--.---..-.-.....--.--.-...-..--.-----..-.-.-..-.........-.-.-..-.-.-....--.-----..-..--..--.-----.-.-..-.--.--......-.-.....-.......--...-.---.--.....-.-.-...-.....-...-...-.---.-.-..........-...-.-.....-...--..--....-...----..-....--..-..--...-..-.-----.--.....--.....----......-..--.......-.....-.-.------.-.-----..-.--.--.....--.--..-.-..-.-...--..-..-.-........----..--.......-.....-.-..--.-..-.....--.....-.-.-...-..-........-....----..-....-..-.--.-...----..-...-....-.....-.----..--..-..-.--..-.-.-.-...--.-..-......-...-.-----....-.------.-...---..-.....-.-..---..-.-.-.----.-.-.---.-...--......-.-..........-....-...-..-.-----..-..-..-..----.-..--....-..-.--......-..

*Thanks to u/Separate_Memory for inspiring this challenge on r/dailyprogrammer_ideas!*

Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/co5i4t/20190809_challenge_380_hard_smooshed_morse_code_3/