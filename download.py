import requests
from bs4 import BeautifulSoup
import wget
import os
import codecs
import sys


def extract_pdf_link(
        url="http://link.springer.com/openurl?genre=book&isbn=978-3-662-44874-8",
        saved_folder="download"):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    item = soup.find('a', {'title': 'Download this book in PDF format'})
    pdf_link = "http://link.springer.com/" + item['href']
    file_name = url[url.rfind("=")+1:]
    wget.download(pdf_link, "{}/{}.pdf".format(saved_folder, file_name))
    return pdf_link


if __name__ == '__main__':
    springer_link_file, saved_folder = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("springer_links.txt", "download")

    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)

    with codecs.open(springer_link_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, link in enumerate(lines):
            try:
                link = link.strip()
                print("downloading ... {}".format(link))
                pdf_link = extract_pdf_link(link, saved_folder)
                print("\ndownloaded {}/{}: {} (pdf: {})".format(i, len(lines), link, pdf_link))
            except:
                print("error: ", link)
