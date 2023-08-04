import os 
import sys
import json

ROOTFOLDER = os.path.dirname(os.path.dirname(__file__))
PATHTOMETADATA = 'paper'

# a function that creates a file main.tex and writes a single line into it 
def generateMain(pathToMetadata=PATHTOMETADATA):
    metadatapath = os.path.join(ROOTFOLDER, pathToMetadata, 'metadata.json')
    f = open(file=metadatapath, mode='r')
    metadata = json.load(f)
    f.close()
    mainpath = os.path.join(ROOTFOLDER, 'paper', 'src', 'main.tex')
    # print(metadata)
    # open a file named main.tex in write mode
    f = open(mainpath, "w")
    # # write a single line into the file
    f.write("\\documentclass[12pt]{article}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\usepackage{amssymb}\n")
    f.write("\\usepackage{hyperref}\n")
    f.write("\\usepackage{float}\n")
    f.write("\\usepackage{subcaption}\n")
    f.write("\\usepackage{geometry}\n")
    f.write("\\geometry{\n")
    f.write("    a4paper,\n")
    f.write("    total={170mm,257mm},\n")
    f.write("    left=20mm,\n")
    f.write("    top=20mm,\n")
    f.write("}\n")
    f.write("\\begin{document}\n")
    f.write("\\title{" + metadata.get("title", "not known title") + "}\n")
    f.write("\\author{" + metadata.get("author-name", "not known author") + "}\n")
    f.write("\\date{\\today}\n")
    f.write("\\maketitle\n")
    f.write("\\input{src/abstract.tex}\n")
    f.write("\\input{src/introduction.tex}\n")
    f.write("\\input{src/methods.tex}\n")
    f.write("\\input{src/results.tex}\n")
    f.write("\\input{src/conclusion.tex}\n")
    f.write("\\bibliographystyle{unsrt}\n")
    f.write("\\bibliography{src/refs}\n")
    f.write("\\end{document}\n")

    # close the file
    f.close()    

generateMain()