# pymarkdownpdf
Coverting Markdown files to PDFs by Python

## Where to place files?
Pymarkdownpdf is designed to attached with a group of document folders and markdown files.
People can put their document folders to anywhere of the tree structure except doc/ which
is the output folder for PDFs.

## How do I use?
1. Copy Markdown files / folders in directory.
2. ./build  (now only on Linux)
3. Search for PDFs in doc/

## Notes
- Default extension name for Markdown files is '.md'. You can add more in doclist.py.
- It is convenient to use automatic build pipline in Github, so that you can check in markdown and later get PDF results automatically.
- Some advance functions are depending on wkhtmltopdf, you can install [wkhtmltopdf](https://github.com/wkhtmltopdf/qt/tree/c745cfd57fbba4f2fe6e17dc95d7a8a3a4c57829) qt patched version if you like.
