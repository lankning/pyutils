"""
Codes from https://www.jianshu.com/p/f3107ecb8bbe
@author: Yuanyang Shao
"""

import PyPDF2
import os
import re


def main():
    # find all the pdf files in current directory.
    mypath = os.getcwd()
    pattern = r"\.pdf$"
    file_names_lst = [mypath + "/" + f for f in os.listdir(mypath) if re.search(pattern, f, re.IGNORECASE) 
    and not re.search(r'Merged.pdf',f)]
    file_names_lst.sort()
    print(file_names_lst)
    
    # merge the file.
    opened_file = [open(file_name,'rb') for file_name in file_names_lst]
    pdfFM = PyPDF2.PdfFileMerger()
    for file in opened_file:
        pdfFM.append(file)

    # output the file.
    with open(mypath + "/Merged.pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    # close all the input files.
    for file in opened_file:
        file.close()

if __name__ == '__main__':
    main()
