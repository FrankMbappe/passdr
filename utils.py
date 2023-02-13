import csv
from difflib import SequenceMatcher
from urllib.parse import urlparse


def read(path: str):
    reader = csv.reader(open(path, newline=""))
    header = next(reader)
    rows = [row for row in reader]
    print(f"Read {len(rows)} rows from '{path}'.")
    return rows, header


def contains_similar(str_list: list[str], search: str, min_similarity_ratio=0.9, verbose=False) -> bool:
    for string in str_list:
        similarity_ratio = SequenceMatcher(None, string, search).ratio()
        if verbose:
            print(f"Checking '{search}' and '{string}': {similarity_ratio * 100}% similarity")
        if similarity_ratio >= min_similarity_ratio:
            print(f"'{search}' is similar to '{string}'")
            return True
    return False


def contains_similar_url(url_list: list[str], url: str, verbose=False) -> bool:
    for list_url in url_list:
        url_obj = urlparse(url)
        list_url_obj = urlparse(list_url)
        if url_obj.hostname == list_url_obj.hostname:
            if verbose:
                print(f"'{url_obj.hostname}' is similar to '{list_url_obj.hostname}'")
            return True
    return False


def write_rows_to_file(rows: list[list[str]], filename: str):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Written {len(rows)} rows to '{filename}'.")
