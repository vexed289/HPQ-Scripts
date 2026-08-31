# HPQ-Scripts
Collection of all scripts, snapshots and figures used within my Edexcel Level 2 Higher Project Qualification Dissertation titled "To what extent are the skills developed in Competitive Programming transferable to different areas and careers in Computer Science?"

## Candidate Information

Candidate Name: Ved Thakkar
Candidate Number: 2111
Centre Number: 14285
Qualification: P201

## Data sources
All data was retrieved using the Codeforces API: https://codeforces.com/apiHelp \
Snapshots of endpoint information were recorded with their specified script and date, this can be viewed in /snapshots. \
All figures also have their exact date and time recorded within their file name.

## Scripts

### graph.py
This script retrieves the current list of all Codeforces problems, and provides an analysis of their ratings using a graph, alongside statistics printed in the terminal.

### totalUsers.py
This script retrieves the total number of rated users on Codeforces, alongside an average rating.

### queryTracker.py
This script contains the methods used to snapshot all data within /snapshots and /figures.

## Reproducibility
These scripts require Python 3.x, alongside all packages mentioned in requirements.txt. These can be installed using the command:
```bash
pip install -r requirements.txt
```