import re
from pathlib import Path
from bs4 import BeautifulSoup
from fpdf import FPDF
import docx
import argparse

def add_section():
    first = input('What is the number of the first video? ')
    last = input('What is the number of the last video? ')
    for i in range(int(first), int(last)+1):
        with open(Path('sources')/ f"{i}.html", 'w') as touch:
            touch.write('')

def clean_output():
    # clean output folder
    folders = list(Path('output/docx').iterdir()) + list(Path('output/pdf').iterdir())
    for folder in folders:
        for file in folder.iterdir():
            file.unlink()
        folder.rmdir()

    # remove .DS_Store files
    items = Path.cwd().rglob('*')
    for item in items:
        if str(item).find('DS_Store') != -1:
            item.unlink()

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clean', action='store_true', required=False, help='Empty all output')
parser.add_argument('-p', '--prep', action='store_true', required=False, help='Create blank html files for videos')
parser.add_argument('-a', '--add', action='store_true', required=False, help='Add a section of videos')
args = parser.parse_args()

if args.clean:
    clean_output()

elif args.prep:
    clean_output()
    for item in Path('sources').iterdir():
        item.unlink()

    # create blank html files
    add_section()

elif args.add:
    add_section()

else:
    for source in Path('sources').iterdir():
        if str(source).find('DS_Store') != -1:
            continue
        with open(source, 'r') as inf:
            transcript = ''
            try:
                soup = BeautifulSoup(inf, 'html.parser')

                # get and format transcript
                lines = soup.find_all('p', class_='transcript--underline-cue---xybZ')
                for l in lines:
                    transcript += l.get_text() + ' '
                transcript = transcript.replace('\n', '')
                transcript = re.sub('\s+', ' ', transcript)
                if transcript[0] == ' ':
                    transcript = transcript[1:]
            
                # get title and prepend to transcript
                title = soup.find('section', class_='lecture-view--container--mrZSm')['aria-label']
                transcript = title + '\n\n' + transcript
            except:
                print(f"EXCEPTION CAUGHT: Error occurred reading {source}\n")
            else:
                # extract a filename based on the lecture title
                fn = title[title.find('Lecture'):] \
                    .replace(':', ' -') \
                    .replace('/', ', ')
                if 'OBJ' in fn:
                    fn = fn[ : fn.find('(OBJ')-1 ]
                sctn = title[ : title.find(', Lecture')] \
                    .replace(':', ' -') \
                    .replace('/', ', ')
                
                # create and export to docx
                doc = docx.Document()
                section = doc.sections[0]
                section.page_width = docx.shared.Inches(5.5)
                section.page_height = docx.shared.Inches(8.5)
                section.top_margin = docx.shared.Inches(0.5)
                section.bottom_margin = docx.shared.Inches(0.5)
                section.left_margin = docx.shared.Inches(0.5)
                section.right_margin = docx.shared.Inches(0.5)
                doc_para = doc.add_paragraph()
                doc_para.paragraph_format.space_after = 1
                doc_para = doc_para.add_run(transcript)
                doc_para.font.name = 'Roboto'
                (Path(f'output/docx/{sctn}')).mkdir(exist_ok=True)
                doc.save(Path('output/docx') / sctn / f'{fn}.docx')

                # create and export to pdf
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
                (Path(f'output/pdf/{sctn}')).mkdir(exist_ok=True)
                pdf.output(Path('output/pdf') / sctn / f'{fn}.pdf')
