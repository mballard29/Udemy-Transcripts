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
- Review `scrapy.py` and make necessary changes. Example changes:
    - xxx

### Workflow:
- Run `python3 scrape.py -p` to empty sources folder. When prompted, input video number of first video to scrape and last (If videos are numbered in course, can use that. If not, can use 1 and number of input videos).
- (Open all created empy HTML files)
- For each Udemy video:
    - Maximize the video window so that all dynamic content is visible
    - Click the `open transcript` button
    - Right-click somewhere on page > `Inspect` to open the inspector window (when window is on the right, resize inspector window to be as small as possible to ensure all dynamic content is visible and therefore accessible in the DOM)
    - Select the 'html' tagged element, Control+C to copy
    - In `sources` project folder, paste html contents into created source file (will paste 'html' tag and child nodes; i.e, whole page)    
- To run:
    - Run `python3 scrape.py`
    - Output will be placed in `output` folder
       - (Title string parsing based initially based on Udemy course videos by Jason Dion)
    - Check for missing files output file. Check to see if it's in source folder and `transcript-cue` tags are visible (indicates transcript was not visible in browser when HTML was copied), rerun if necessary.
    - Copy+Paste to target folder (such as iCloud to annotate pdfs on iPad, or a save folder to edit in word processor)
- Note:
    - The output folder is cleaned out before every run, comment out that line to disable this behavior
    - On Mac, remove .DS_Store files with `find <in-this-directory> -name ".DS_Store" -delete`

### Common Errors
1. Project folder structure incorrect
2. Missing dependencies (in active venv, run `pip freeze` to check if it matches `requirements.txt`, check if venv is using pip or pip3)
3. Incorrectly copied HTML pages
   - transcript was not opened and visible in webpage when copying and pasting HTML
   - when scraping transcripts from a batch of videos, may miss a video, copy and paste one twice, accidentally toggle off transcript in between repeat copy and pasting, etc. (double check your work)

### Roadblocks During Implementation and To Further Tool Expansion:
- Udemy must authenticate to see page. Testing to see if there is an automated way to grab video transcripts. As it standings available methods are (prohibitively) slow.
- Udemy 'Instructors' have an API. The Affiliate API has been discontinued 1/1/25, and the Udemy Affiliate Program requires a special applicate. TLDR: No API available for regular users.
- There is no script tag that seems to obviously/directly point to metadata or resource fetch requests that would allow static scraping
- A lot of content on the page is dynamically loaded, including the content I am targeting. Looking at the Inspect window, the HTML only shows explicitly visible content (sensitive triggers/toggles), making resizing the browser window and inspection window necessary to see all available data.
- No FETCH/XHR requests are discernably for transcript data

##### Note:
- If you choose to test this tool, it is expected that you know some Python, some HTML, and have some understanding of file naming rules in the filesystem you use. This is a tool that I have tested and has worked for the applications for which I have tried to use it, but customization is necessary for use by others who may be interested.
- Udemy is a content hosting platform where creators can provide paid online classes. This tool cannot provide access to a user who does not already have a Udemy account and does not have access to a course (for which they have paid). This is an add-on tool to increase the accessibility of already existing accessibility features. If you choose to use this tool, you recognize that you are accessing someone's intellectual property for personal use, and the initial creator of this tool (Mason Ballard) is not liable for any copyright infringement or violation of IP fair use should you choose to distribute that content without the video creator's or course creator's express permission.

##### Other notes:
- For these instructions, Control (Ctrl) on Windows is functionally equivalent to Command (Cmd) button on Mac
- Windows systems use the `py` command instead of `python` or `python3` in Linux and MacOS systems
- For first time VS code Github source control setup, may have to run
  <pre>
      git config --global user.email "your email" 
        git config --global user.name "your name"
  </pre>
