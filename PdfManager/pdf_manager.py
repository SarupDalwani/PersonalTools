# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyPDF2 import PdfWriter

def merge_pdf(args) :

    if len(args) < 3 :
        print(f'Invalid arguments, required atleast 3 provided {len(args)}')
        return

    pdfs = args[:-1]

    merger = PdfWriter()
    for pdf in pdfs :
        merger.append(pdf)

    merged_pdf = args[-1]
    merger.write(merged_pdf)
    merger.close()
    print(f'PDF merged to {merged_pdf}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv
    len_args = len(sys.argv)
    if len_args == 1 :
        print('No command provided, refer to help by --help')
    elif args[1] == 'merge' :
        merge_pdf(sys.argv[2:])
    elif args[1] == "--help" :
        print("merge [input_pdfs_path ...] output_path")
    else :
        print('No command provided, refer to help by --help')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
