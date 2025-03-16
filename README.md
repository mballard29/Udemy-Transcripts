# Udemy Trancripts

### Download:
- Clone repo
- Add folders: 
    -  `output/docx/`
    -  `output/pdf/`
    -  `sources/`
- Create virtual environment: `python3 -m venv env`
- Activate:
    - Mac: `source env/bin/activate`
    - Windows (Powershell): `.\env\Scripts\Activate.ps1`
- Install required packages: `pip3 install -r requirements.txt`
    - if this giving issues, can try: `python3 -m pip install -r requirements.txt`
- Review `scrapy.py` and make any necessary changes (e.g., project folder path variable)

### Workflow:
- For each Udemy video:
    -   Click the `open transcript` button
    -   Right-click somewhere on page > `Inspect` to open the inspector window (when window is on the right, resize window to as small as possible to make sure all dynamic content is visible and therefore visible in the DOM)
    -   Select the 'html' tagged element, Control+C to copy
    -   In `sources` project folder, create a new file, paste html contents (will paste 'html' tag and child nodes, i.e, whole page)    
- To run:
    -   Run `python3 scrape.py`
    -   Output will be placed in `output` folder
       -  (Title string parsing based on Udemy course videos by Jason Dion)
    -   Check for missing files, rerun if necessary
    -   Copy+Paste to target folder (such as iCloud to annotate pdfs on iPad, or a save folder and edit in word processor)
- Note:
    - The output folder is cleaned out before every run, comment out that line to disable this behavior
    - The sources are left after each run in the case of unexpected behavior, uncomment the line at the end of the `scrape.py` script to enable cleaning out that folder automatically after each run

### Roadblocks:
- Udemy must authenticate to see page. Testing to see if there is an automated way to grab video transcripts. As it standings available methods are (prohibitively) slow.
- Udemy 'Instructors' have an API. The Affiliate API has been discontinued 1/1/25, and the Udemy Affiliate Program requires a special applicate. TLDR: No API available for regular users.
- There is no script tag that seems to obviously/directly point to metadata or resource fetch requests that would allow static scraping
- A lot of content on the page is dynamically loaded, including the content I am targeting. Looking at the Inspect window, the HTML only shows explicitly visible content (sensitive triggers/toggles), making resizing the Inspect window necessary to see all available data.
- No FETCH/XHR requests are discernably for transcript data
