# BookBot

BookBot is a command-line text analysis tool developed as part of the [Boot.dev](https://www.boot.dev) curriculum. This utility analyzes text files and provides insightful statistics about their content.

## Features

- Count the total number of words in a text file
- Count and display the frequency of each alphabetical character
- Sort and present character frequency in a readable format

## How to Use

1. Clone this repository to your local machine
2. Navigate to the project directory
3. Run the program with the path to your text file:

```bash
python main.py path/to/your/textfile.txt
```

## Example

When you run BookBot on a text file, you'll see output similar to this:
```
============ BOOKBOT ============
Analyzing book found at books/prideandprejudice.txt...
----------- Word Count ----------
Found 130410 total words
--------- Character Count -------
e: 74451
t: 50837
a: 44834
...
```

## Project Structure

- `main.py`: Entry point for the application
- `stats.py`: Contains text analysis functions
- `.gitignore`: Specifies files to ignore in version control

## Learning Objectives

This project demonstrates:
- File I/O operations in Python
- Text processing and analysis
- Command-line argument handling
- Function organization and code structure