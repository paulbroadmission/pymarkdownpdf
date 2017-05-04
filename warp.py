import codecs
import os, sys
from markdown import markdown
import pdfkit
from doclist import typelist, output_path, css

options = {
    'page-size': 'Letter',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'no-outline': None,
    #'enable-internal-links': '',
    #'enable-external-links': '',
    'quiet': ''
}


def traverse_dir(entry_dir):
    for root, dirs, files in os.walk(entry_dir):
        for file in files:
            fname, fextension = os.path.splitext(file)
            if fextension in typelist:
                p=os.path.join(root,file)
                covert_pdf(p)
                

def covert_pdf(filename):
    print "converting %s ..."%(filename)
    with codecs.open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
        type(text)
        html_text = markdown(text, output_format='html5')
    pdfkit.from_string(html_text, str(filename)+'.pdf', options=options, css=css)
    os.system('mv \'{}\'.pdf {}'.format(str(filename), output_path))
    #output_file = codecs.open(todofile+'.html', "w", 
    #                      encoding="utf-8", 
    #                      errors="xmlcharrefreplace"
    #)
    #output_file.write(html_text)

if __name__ == '__main__':
    traverse_dir('.')
