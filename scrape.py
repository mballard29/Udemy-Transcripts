import os
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from fpdf import FPDF
import docx

# CHANGE to your project folder
if os.name == 'posix':  # mac
    project = Path('<Path to Project>/Udemy Transcripts/')
else:                   # windows is 'nt'
    project = Path('<Path to Project>/Udemy-Transcripts/')
    

def clean_folder(name):
    if name == 'output': 
        path = project / 'output' / 'docx'
        old_out = os.listdir(path)
        for o in old_out:
            os.remove(Path('output/docx') / o)
        path = project / 'output' / 'pdf'
        old_out = os.listdir(path)
        for o in old_out:
            os.remove(Path('output/pdf') / o)
        return
    elif name == 'sources':
        path = project / 'sources'
        old_out = os.listdir(path)
        for o in old_out:
            os.remove(Path('sources') / o)
        return
    print('Folder selected for cleaning is not a valid choice. Must be "sources" or "output".')
    return
  
if __name__ == '__main__':
    clean_folder('output')

    # USAGE: python3 scrapy.py -prep
    # input: the video number of the first video transcript to scrape and the last
    # output: clean out old source files, creates new HTML files with numbered names
    if len(sys.argv) > 1 and sys.argv[1] == '-prep':
        clean_folder('sources')
        # create first html file
        first = input("What number is the first video? ")
        last = input("What is the number of the last video? ")
        for i in range(int(first), int(last)+1): 
            video = str(i)+".html"   
            with open((Path('sources') / video), "w") as touch:
                touch.write('')
    
    # USAGE: python3 scrape.py
    else:
        # open sources
        path = project / 'sources'
        sources = os.listdir(path)

        # get doc body, format filename and save location
        for s in sources:
            transcript = ''
            title = ''
            if s.find('DS_Store') == -1:
                with open((Path('sources') / s), "r") as inf:
                    try:
                        soup = BeautifulSoup(inf, 'html.parser')
                        lines = soup.find_all('p', class_='transcript--underline-cue---xybZ')
                        for l in lines:
                            transcript += (l.get_text() + ' ')
                        transcript = transcript.replace('                                ', ' ').replace('/n', ' ').replace('   ', ' ')
                        if transcript[0] == ' ':
                            transcript = transcript[1:]
                        title = soup.find('section', class_='lecture-view--container--mrZSm')['aria-label']
                        transcript = title + '\n\n' + transcript
                    except:
                        print(f"EXCEPTION CAUGHT: Error occurred reading {s}\n")
                
                # output filenames/formats and locations
                # CHANGE title parsing based on the course you are taking
                # Original parses: 'Section X: Example Section Title, Lecture Y: Example Lecture Title'
                # to 'Lecture Y - Example Lecture Title.<ext>'
                title = title[(title.find('Lecture')):(title.find('(')-1)].replace(':', ' -')
                # txt_doc_fn = Path('output/txt/') / (title + '.txt')
                doc_fn = Path('output/docx/') / (title + '.docx')
                pdf_fn = Path('output/pdf/') / (title + '.pdf')

                # output to textfile
                # with open(txt_fn, 'w') as txt:
                #     txt.write(transcript)

                # output to docx
                doc = docx.Document()
                doc_para = doc.add_paragraph()
                doc_para.paragraph_format.space_after = 1
                doc_para = doc_para.add_run(transcript)
                doc_para.font.name = 'Roboto'
                doc.save(doc_fn)

                # output to pdf
                pdf = FPDF(format='letter', unit='in')
                pdf.add_page()
                pdf.set_font("helvetica", size = 12)
                pdf.set_margins(1, 1)
                effective_page_width = pdf.w - 2*pdf.l_margin
                pdf.multi_cell(
                    w=effective_page_width, 
                    h=0.22, 
                    text=transcript,
                    align='J'
                    )
                pdf.output(pdf_fn)

