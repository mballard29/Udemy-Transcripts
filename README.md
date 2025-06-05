# Udemy Trancripts
Make Udemy transcripts more accessible. Outputs video transcript to .docx and .pdf files with the ability to also output to .txt files. Annotate .pdf files on iPad or tablet. Edit .docx files, highlight, underline, italicize in your preferred word processor. Included is the main script (`scrape.py`), example files of Udemy HTML pages, and example outputs. If you'd like to test this tool, you will need to change the file paths listed on lines 9 and 11 to match the path where you have cloned your project folder to. If you use Mac and Windows, you will need to change both. If you only use one, you can exchange the if-else block for a single `project = Path('<path to project folder>')`. You will also need to change the parsing of the video title attribute to match the formatting of the video titles you are trying to scrape the title from and what you would like it parsed to (on line 80)(in order to follow file naming rules for your filesystem). Made with Python and BeautifulSoup, FPDF2, and docx modules. 


### Download:
- Clone repo
- Create virtual environment: `python3 -m venv env`
- Activate:
    - Mac: `source env/bin/activate`
    - Windows (Powershell): `.\env\Scripts\Activate.ps1`
- Install required packages: `pip3 install -r requirements.txt`
    - if this giving issues, can try: `python3 -m pip install -r requirements.txt`
- Review `scrapy.py` and make necessary changes (lines 8-12 project path, line 80 video title parsing)

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
2. Incorrect project path variable in `scrape.py` script
3. Missing dependencies (in active venv, run `pip freeze` to check if it matches `requirements.txt`, check if venv is using pip or pip3)
4. Incorrectly copied HTML pages
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