from utils import read, contains_similar_url, write_rows_to_file

# This script extracts unique entries between Firefox and Bitwarden logins. #

# Set script filenames
OUTPUT_FILENAME = "unique_firefox_logins.csv"
FIREFOX_LOGINS_FILENAME = "logins_firefox.csv"
BITWARDEN_LOGINS_FILENAME = "logins_bwd.csv"

# We will assert difference between entries based on the URL column
FIREFOX_URL_COLUMN_INDEX = 0
BITWARDEN_URL_COLUMN_INDEX = 7

# Extract Firefox and Bitwarden login files' rows
fire_rows, fire_header = read(FIREFOX_LOGINS_FILENAME)  # Indexes: url=0, username=1, password=2
bwd_rows, bwd_header = read(BITWARDEN_LOGINS_FILENAME)  # Indexes: url=7, username=8, password=9

# From Bitwarden rows, extract URLs only
bwd_urls = [bwd_row[BITWARDEN_URL_COLUMN_INDEX] for bwd_row in bwd_rows]

# Pick only rows from Firefox where URLs are different from Bitwarden
unique_fire_rows = list(
    filter(
        lambda fire_row: not contains_similar_url(
            url=fire_row[FIREFOX_URL_COLUMN_INDEX],
            url_list=bwd_urls
        ),
        fire_rows
    )
)

# Report unique URLs (just for verification)
unique_urls = list(map(lambda r: r[0], unique_fire_rows))
print(f"Found {len(unique_fire_rows)} unique Firefox entries:", unique_urls)

# Save unique rows + header in file
write_rows_to_file(
    rows=[fire_header] + unique_fire_rows,
    filename=OUTPUT_FILENAME
)
