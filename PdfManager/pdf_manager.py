import sys
from PyPDF2 import PdfWriter,PdfReader

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

def split_pdf(args) :

    if len(args) < 3 :
        print(f'Invalid arguments, required atleast 3 provided {len(args)}')
        return

    input_file_name = args[0]
    input_file = open(input_file_name, 'rb')

    input_file_reader = PdfReader(input_file)

    output_file_writer = PdfWriter()
    output_file_name = args[1]

    start = int(args[2]) - 1
    if len(args) == 3 :
        end = start + 1
    else :
        end = int(args[3])

    for page in range(start, end) :
        output_file_writer.add_page(input_file_reader.pages[page])

    output_file_writer.write(output_file_name)
    output_file_writer.close()

    print(f'PDF splited to {output_file_name}')

if __name__ == '__main__':
    args = sys.argv
    len_args = len(sys.argv)
    if len_args == 1 :
        print('No command provided, refer to help by --help')
    elif args[1] == 'merge' :
        merge_pdf(sys.argv[2:])
    elif args[1] =='split' :
        split_pdf(sys.argv[2:])
    elif args[1] == "--help" :
        print("merge [input_pdfs_path ...] output_path")
    else :
        print('No command provided, refer to help by --help')
