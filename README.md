# CS337 Project 3 -- Recipe Transformer
# Group 3 - Recipe Parsing & Recipe Transformer

In this project we implemented the following required transformations:

- To and from vegetarian
- To and from healthy
- Style of cuisine ~ to Italian

and the following optional transformations:

- Additional Style of cuisine ~ to Mexican
- Double the amount
- Cut the amount by half 
- To gluten-free
- To lactose-free

## Setup Instructions

Please run "pip install -r requirements.txt" to recreate the environment necessary.
The python version used is Python 3.12.1.

## Libraries/Packages Overview
1. **requests**: The Requests is a Python library that allows you to send HTTP/1.1 requests extremely easily.
   
2. **re**: re is a Python built-in package, which can be used to work with Regular Expressions.
   
3. **bs4**: Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
      
4. **NLTK**: The Natural Language Toolkit (NLTK) is a comprehensive library for working with human language data (text) in Python, including text classification, tokenization, stemming, tagging, parsing, and more.

## Group 3 Github Repository
 You can access our group's project-3 Github repository through following address: 
https://github.com/scui24/Transformer.git

## Demo video
Our demo video is in the zip file for the project submission. 

## Steps to run the the python file in the submission folder

Step 1: Open and run the **"Transformer.py"** python file.

The command line will ask which recipe you would like to transform. 

Step 2:  Input any recipe url from https://www.allrecipes.com.

The command link will ask which transformation you would like to perform and they will be numbered.

Step 3: Select the corresponding number of the transformation you would like to perform. 

The output will be saved as a txt file, named after the title of the Recipe and the transformation done on it, and containing the name of the transformation, the input reicpe, and the transformed recipe. To perform a new transformation run the file again and repeat the steps. 


