import os, re, sys, zipfile

filename = 'resume.docx' # hardcoded for user convenience

job = str(sys.argv[1])
company = str(sys.argv[2])
city = str(sys.argv[3])
#seo = str(sys.argv[4]) # to be added in the GUI version

new_resume_name = 'MCEvans_resume.docx' # me

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def modify_xml(document):
    f = open(document, 'r')
    content = f.read()
    p = re.compile('(J0B)')
    output = p.sub(job, content)
    p = re.compile('(COMPANY)')
    output = p.sub(company, output)
    p = re.compile('(CITY)')
    output = p.sub(city, output)
    f.close()
    g = open('/tmp/rez/word/document.xml', 'w')
    g.write(output)
    g.close()


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


unzip(filename, '/tmp/rez/')
modify_xml('/tmp/rez/word/document.xml')
make_new_docx(new_resume_name)

