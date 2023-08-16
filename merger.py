import PyPDF2
import sys
import os


# Initialize merger object
merger = PyPDF2.PdfMerger()

# Set download directory
download_dir = "/mnt/c/Users/18687/Downloads/"
# print(download_dir)


def merge_curdir_pdfs():
    '''
    Merge all pdfs in current directory
    and save to download directory
    '''
    for item in os.listdir(os.curdir):
        if item.endswith('.pdf'):
            merger.append(item)
    merger.write(download_dir + 'curdir_merge.pdf')


def main():

    print(len(sys.argv))

    if len(sys.argv) == 1:  # no command line arguments
        merge_curdir_pdfs()
        sys.exit(0)


if __name__ == '__main__':
    main()
