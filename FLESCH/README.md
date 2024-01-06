# Flesch–Kincaid readability tests
This is a programme that reads files in a directory and calculates the Flesch score of all text/paragraphs in the file.
Flesch score of all files are then written into a new text file.

The formula used to calculate the is:
***206.835 – 1.015 x (words/sentences) – 84.6 x (syllables/words)***

The package used to obtain the number of syllables is:
https://github.com/mholtzscher/syllapy
