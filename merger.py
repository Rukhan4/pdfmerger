import PyPDF2
import sys
import os


# Initialize merger object
merger = PyPDF2.PdfMerger()

# Set download directory
download_dir = "/mnt/c/Users/18687/Downloads/"
# print(download_dir)

filename = str(input("Enter save file name: "))


def merge_curdir_pdfs():
    '''
    Merge all pdfs in current directory
    and save to download directory
    '''
    for item in os.listdir(os.curdir):
        if item.endswith('.pdf'):
            merger.append(item)
    merger.write(download_dir + filename + '.pdf')


def merge_cmdline_pdfs(pdf_list):
    '''
    Merge all pdfs in command line
    and save to download directory
    pdf_list: ListOf Str
    '''
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(download_dir + filename + '.pdf')


def main():

    print(len(sys.argv))

    if len(sys.argv) == 1:  # no command line arguments
        merge_curdir_pdfs()
        print("PDFs merged successfully!")
        sys.exit(0)
    else:  # command line arguments present
        pdf_list = sys.argv[1:]
        # Cross-platform compatibility between wsl and windows
        wsl_pdf_list = [pdf.replace("C:", "/mnt/c").replace("\\", "/") for pdf in pdf_list]
        merge_cmdline_pdfs(wsl_pdf_list)
        print("PDFs merged successfully!")
        sys.exit(0)


if __name__ == '__main__':
    main()
