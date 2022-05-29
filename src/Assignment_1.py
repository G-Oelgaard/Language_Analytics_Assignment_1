## Import packages ##
import os
import re 
import math
import pandas as pd
import argparse

## Define functions ##
# Load text
def data_load(text):
    filepath = os.path.join("..", "in", text)
    
    with open(filepath, "r") as f:
        text_full = f.read()
    
    return text_full

# define tokenize function
def tokenize(text_full):
    tokenizer = re.compile(r"\W+")
    
    return tokenizer.split(text_full)

# Make text lowercase and remove punctuation
def normalize(text_full):
    token_text = []

    for word in tokenize(text_full):
        lowercase_word = word.lower() # Lowercase
        word_npunct = re.sub(r"[^\w\s]", "", lowercase_word) # Remove punctuation
        token_text.append(word_npunct)
        
    return token_text

# Find all occurrences of search term in text
def search_index(token_text, keyword, window_size):
    window_size = int(window_size)
    
    index = []

    for idx, token in enumerate(token_text):
        if token == keyword:
            before = idx - window_size
            after = idx + window_size
            all_colls = token_text[before:idx] + token_text[idx+1:after] # +1 so we don't include the keyword
            index.append(all_colls)
    
    flat_index = [] # flatten the index 

    for list in index:
        for item in list:
            flat_index.append(item)
            
    return flat_index

# List of collocates and how many times they appear
def coll_count(flat_index):
    collocate_counts = []
    
    for coll in set(flat_index):
        count = flat_index.count(coll)
        collocate_counts.append((coll, count))
        
    return collocate_counts

# Text and search term count
def count(token_text, keyword):
    text_length = len(token_text) # full text length
    term_counter = token_text.count(keyword)

    return term_counter, text_length

# Create list of scores
def outlist(collocate_counts, token_text, term_counter, window_size, text_length):
    window_size = int(window_size)
    
    out_list = []
    
    for index, coll in enumerate(collocate_counts):
        coll_text = coll[0]
        coll_count = coll[1]
        total_occurrences = token_text.count(coll_text)
        score = math.log((total_occurrences * text_length) / (term_counter * coll_count * window_size)) / math.log(2)
        image_data = [term_counter, coll_count, total_occurrences, score]
        out_list.insert(index, image_data)
        
    out_list = sorted(out_list, key=lambda x:x[3], reverse=True) #Sorting list by MI score
        
    return out_list

# Creating and saving dataframe
def output_data(keyword, out_list):
    outpath = os.path.join("..", "out", keyword+"_word_collocation.csv")
    
    output_data = pd.DataFrame(out_list, columns = ["Collocate", "Collocate Count", "Total Count", "MI"])

    output_data.to_csv(outpath, index = False)
    
# args_parse
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", "--keyword", required = True, help="The keyword / search term you want to use.")
    ap.add_argument("-t", "--text", required = True, help="The text you want to use. Remember to include '.txt'")
    ap.add_argument("-w", "--window_size", required = True, help="The window size you want to use.")
    args = vars(ap.parse_args())
    return args

## Main ##
# Defining main
def main():
    args = parse_args()
    text_full = data_load(args["text"])
    token_text = normalize(text_full)
    flat_index = search_index(token_text, args["keyword"], args["window_size"])
    collocate_counts = coll_count(flat_index)
    term_counter, text_length = count(token_text, args["keyword"])
    out_list = outlist(collocate_counts, token_text, term_counter, args["window_size"], text_length)
    output_data(args["keyword"], out_list)
    
# Running main
if __name__ == "__main__":
    main()