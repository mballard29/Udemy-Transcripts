#!/bin/bash


# CLEANING PROJECT FOLDER
find . -name ".DS_Store" -delete

# ACTIVATING PYTHON ENVIRONMENT
source env/bin/activate

# CLEAN OUTPUT FOLDER BETWEEN RUNS or FOR FEATURE DEV TESTING
python3 scrape.py --clean


# --------------------- WORKING WITH TRANSCRIPTS ---------------------
# CREATING empty TRANSCRIPT FILES - clears output and sources folder
python3 scrape.py --prep
    # enter first video's video number
    # enter video number of last video in section
    # C + P video HTMLs


# ADDING ANOTHER SECTION - deletes nothing, creates empty htmls
python3 scrape.py --add
    # enter first video's video number
    # enter video number of last video in section
    # C + P video HTMLs


# CREATE TRANSCRIPT DOCUMENTS
python3 scrape.py --transcripts --wordOnly


# --------------------- REVIEWING PRACTICE TESTS ---------------------
# CREATING TEST SOURCE FILE
python3 scrape.py --addTest
    # enter the number of the test, source file will be named `Practice Test <number>`
    # C + P test review HTML


# CREATING TEST REVIEW
python3 scrape.py --reviews --wordOnly



