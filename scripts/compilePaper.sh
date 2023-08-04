#! /bin/bash

# check if pdflatex is installed. If not issue a warning and exit, otherwise procede

if ! command -v pdflatex &> /dev/null
then
    echo "pdflatex could not be found"
    echo "Please install pdflatex and try again"
    exit
fi

# check if bibtex is installed. If not issue a warning and exit, otherwise procede

if ! command -v bibtex &> /dev/null
then
    echo "bibtex could not be found"
    echo "Please install bibtex and try again"
    exit
fi

# check if python3 is installed. If not issue a warning and exit, otherwise procede

if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    echo "Please install python3 and try again"
    exit
fi

# run the generation of the main.tex
paper/.venv/bin/python3 paper/generateMain.py
cd paper
# Generate the pdflatex
./generatePdf.sh &> /dev/null
cd ..

# echo that pdf has been generated
echo ">>> PDF has been generated"
echo ">>> PDF can be found in paper/dist/draft.pdf"



