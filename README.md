# Various Automation Scripts for the Iridium Browser

## Overview
Housed in this repository are various scripts for manipulating the Iridium Browser, found here [iridiumbrowser.de](iridiumbrowser.de).

## Features
- Retrieve active URLs from Iridium and save them to a file.
- Open saved URLs in a new instance of Iridium.
- Retrieve and save URLs from Iridium's browser history.

## Usage
For `open_iridium_files.py`, invoke python and file name, then after that, a text file containing any amount of urls.

For `extract_iridium_tabs.py`, simply invoke python and file name.

For `extract_iridium_files`, use the 2 params from `open_iridium_files.py`, and additionally the path to your iridium executable.

### Example
```plaintext
py -m extract_iridium_files
py -m open_iridium_files active_current_urls.txt
py -m open_iridium_files active_current_urls.txt "C:\...\...\iridium.exe"
```

## Potential Additions
I made these scripts on a whim, and they are purely for conveience. Whenever I need more automation for this browser, those scripts will be pushed here

## Known Issues
- 1 of the scripts includes your history to be the bookmarks as well
- 1 of the sctipts does not open all the windows in the text file, confusing bug

## How to run
1. Clone the Repository:
```plaintext
git clone 
https://github.com/Isaac-Herbst/Scripts-for-iridium.git
cd Scripts-for-iridium
```

2. Run the Program:
Use Python to run the scripts above.

## Dependencies
- Python 3.X
- Selenium
- ChromeDriver

Make sure Python is installed on your machine. You can download it from [python.org](python.org).