#!/usr/bin/python3
import os, re, sys, zipfile
from shutil import copyfile

filename = 'resume.docx' # hardcoded for user convenience

job = str(sys.argv[1])
company = str(sys.argv[2])
city = str(sys.argv[3])
keywords = ""
if len(sys.argv) == 5: #sys.argv[4] is None):
    keywords = str(sys.argv[4])
temp_loc = '/tmp/rez/'
temp_loc_d = '/tmp/rez/word/document.xml'
temp_loc_f = '/tmp/rez/word/footer1.xml'

new_resume_name = 'MCEvans_resume.docx' # hardcoded for my convience

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def modify_document(document):
    f = open(document, 'r')
    content = f.read()
    p = re.compile('(J0B)')
    output = p.sub(job, content)
    p = re.compile('(COMPANY)')
    output = p.sub(company, output)
    p = re.compile('(CITY)')
    output = p.sub(city, output)
    f.close()
    g = open(temp_loc_d, 'w')
    g.write(output)
    g.close()

def modify_footer(footer):
    f = open(footer, 'r')
    content = f.read()
    str = '<w:t xml:space="preserve">Keywords: '
    p = re.compile(str)
    if keywords == "":
        var = '<w:t>' 
    else:
        var = str
        var += keywords
    output = p.sub(var, content)
    print(var)
    print(output)
    f.close()
    g = open(temp_loc_f, 'w')
    g.write(output)
    g.close()

def dir2zip(dir_to_zip):
    zip = zipfile.ZipFile('z.zip', 'w', zipfile.ZIP_DEFLATED)
    for dirname, subdirs, files in os.walk(dir_to_zip):
        zippy.write(dirname, dir_to_zip)
        for file in files:
            zip.write(os.path.join(dirname, file))
    zippy.close()

def make_zipfile(output_filename, source_dir):
    dir_to_zip = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.Zipfile(output_filename, 'a', zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            zip.write(root, os.path.relpath(root, dir_to_zip))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename):
                    zipped = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, zipped)
                    
def make_new_docx(new_resume):
    list = ['/tmp/rez/word/', '/tmp/rez/_rels/', '/tmp/rez/docProps']
    for i in list:
        make_zipfile(new_resume, i)
    zip = zipfile.ZipFile(new_resume, "a")
    zip.write('/tmp/rez/[Content_Types].xml', '[Content_Types].xml')

def main():
    unzip(filename, temp_loc)
    modify_document(temp_loc_d)
    modify_footer(temp_loc_f)
    make_new_docx(new_resume_name)
    copyfile('MCEvans_resume.docx', 'Desktop/MCEvans_resume.docx')

main()
