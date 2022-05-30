# Language_Analytics_Assignment_1
## ------ SCRIPT DESCRIPTION ------
This repository contains a script that takes a user-defined text, search term and window size, and then finds the all collocates in the window + their MI-score.

The model will:
1. Load a user defined text.
2. Tokenize and normalize the text.
3. Count how many times the collocates appear in the designated window and the whole text.
4. Calculate the collocates MI-score
5. Save a .csv file with the information from point 3. and 4. 

## ------ DATA ------
The data used in the creation and testing of the model was a large collection of english models in .txt format.

The data can be found here: https://github.com/computationalstylistics/100_english_novels

## ------ REPO STRUCTURE ------
"src" FOLDER:
- This folder contains the collocation .py script.

"in" FOLDER:
- This is where the data used in the scripts should be placed. Ie. where the '.txt' files used should be placd.

"out" FOLDER:
- This is where the .csv will be saved.

"utils" FOLDER:
- This folder should include all utility scripts used by the main script. In this case none.

## ------ SCRIPT USAGE ------
### Arguments

**Required**
Argument         | What it specifies / does
---------------- | -------------------------
"-k" / "--keyword" | The keyword / search term you want to use.
"-t" / "--text" | The text you want to use. Remember to include '.txt'.
"-w" / "--window_size" | The collocates window size you want to use.

## ------ RESULTS ------
The model achieves what it sets out to do. It is also surprisingly fast!

It should be noted that a single instance of a collocate appearing three times in the windows, but only once in the whole text, occurred. This could mean that the word was surrounded by keywords.
