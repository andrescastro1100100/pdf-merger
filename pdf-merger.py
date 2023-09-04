import PyPDF2 # pip install PyPDF2 - library to work with PDF files


files= [] # list of files to merge

output_file_name = "merged.pdf" # output file name

final_pdf = PyPDF2.PdfMerger()

for file_name in files:
    final_pdf.append(file_name)


final_pdf.write(output_file_name)

final_pdf.close()