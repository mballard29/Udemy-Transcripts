# Udemy Trancripts
Make Udemy transcripts more accessible, make learning more active, take advantage of multiple learning types. Takes Udemy course video pages, and outputs video transcripts. Takes practice test reviews, and outputs a clean, printable, editable documented. Outputs can be in .docx or .pdf formats or both. Annotate .pdf files on iPad or tablet. Edit .docx files, highlight, underline, italicize in your preferred word processor. Included is the main script (`scrape.py`), example files of Udemy HTML video lesson pages and HTML practice test pages, and example outputs. This repo is based on parsing Jason Dion's CompTIA Udemy video lessons and Practice Review pages. Anyone is free to explore this repo, but trying this tool independly will require a basic knowledge of Python as well as modifying the script to fit how your Udemy course instructor presents information (e.g., another course instructor will likely not use the same video title format). Made with [Python](https://www.python.org/downloads/) and [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), [FPDF2](https://pypi.org/project/fpdf2/), and [Python DOCX](https://pypi.org/project/python-docx/) modules. 

### Download:
- Clone repo
- Create virtual environment: `python3 -m venv env`
- Activate virtual environment:
    - Mac: `source env/bin/activate`
    - Windows (Powershell): `env\Scripts\Activate.ps1`
    - VS code: accept if prompt pops up asking if you'd like to make virtual environment default way to run and debug (integrated terminal automatically have env activated and run all commands through it)
- Install required packages: `pip3 install -r requirements.txt`
    - if this gives issues, can try: `python3 -m pip install -r requirements.txt`
- Review `scrapy.py` and make necessary changes. Suggested customizations are written in the `scrape.py` script in comments that start with `CUSTOMIZE`

### Workflow:
- Common steps and workflows and their commands are listed in `runbook.sh` (should *not* be run as a start bash script)

### Common Errors
1. Project folder structure incorrect
2. Missing dependencies (in active venv, run `pip freeze` to check if it matches `requirements.txt`, check if venv is using pip or pip3)
3. Incorrectly copied HTML pages
   - transcript was not opened and visible in webpage when copying and pasting HTML
   - when scraping transcripts from a batch of videos, may miss a video, copy and paste one twice, accidentally toggle off transcript in between repeat copy and pasting, etc. (double check your work)

### Roadblocks During Implementation and To Further Tool Expansion:
- Udemy must authenticate to see page
- Udemy does not provide a publicly available API for regular users. (Only instructors, Affiliate program discontinued)
- Pages are dynamically loaded. HTML only shows explicitly visible content (sensitive triggers/toggles). A visual inspection of the window while the Inspect window is open is necessary to ensure all desire info is accessible.
- No FETCH/XHR requests are discernably for transcript data

##### Note:
- Udemy is a content hosting platform where creators can provide paid online classes. This is **not** a "outsmart the paywall" tool. It is a supplementary study tool to increase engagement with the material and increase the existing accessibility features of the Udemy platform. Anyone who chooses to use this tool, clone this repo, or customize it, acknowledges all course material is the instructor's intellectual property, and therefore, any content created from it should be used for personal use only. Anyone who clones this repo, customizes it, and uses this tool is responsible for any resulting copyright infringement, violation of IP, or violation of fair use.

##### Other notes:
- Control (Ctrl) on Windows = Command (Cmd) button on Mac
- Windows systems use the `py` command, Linux and MacOS uses `python` or `python3`
- For first time VS code Github source control setup, may have to run
  <pre>
      git config --global user.email "your email" 
      git config --global user.name "your name"
  </pre>
