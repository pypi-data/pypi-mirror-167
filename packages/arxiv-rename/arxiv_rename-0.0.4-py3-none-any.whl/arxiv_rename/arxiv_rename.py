import arxiv
from slugify import slugify
import sys
from os import path, rename

from arxiv_rename.arxiv_detect import detect_arxiv, detect_arxiv_no_cat


def arxivRename(filepath):
    filename = path.basename(filepath)
    arxiv_id = filename[:filename.rfind('.')]

    if not detect_arxiv(filename):
        if not detect_arxiv_no_cat(filename):
            return
        cat = input(f'Enter the category for {filename} (default: hep-th): ')
        prefix = ('hep-th' if cat == '' else cat) + '/'
        if not detect_arxiv(prefix + filename):
            print('Invalid category name entered')
            return
        arxiv_id = prefix + arxiv_id

    result = list(arxiv.Search(id_list=[arxiv_id]).results())[0]

    title = result.title

    authors = ' '.join(map(lambda x: x.name.split()[-1], result.authors))

    slug = slugify(arxiv_id + ' ' + authors + ' ' + title) + '.pdf'

    print(arxiv_id + ': ' + title)

    try:
        rename(filepath, path.dirname(filepath) + '/' + slug)
    except Exception as e:
        print('Error renaming ' + filepath)


def main():
    arxivRename(sys.argv[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: $ python arxiv-rename.py <path-to-pdf-downloaded-from-arxiv>")
        print(
            "\t*The pdf file is expected to have as name the arXiv id: e.g: '1103.0261.pdf'")
        exit()
    main()
