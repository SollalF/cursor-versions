import re


def find_download_links(text):
    # Regular expression pattern to match the download links
    pattern = (
        r"https://downloader\.cursor\.sh/versions/\d+\.\d+\.\d+/[a-zA-Z]+/[a-zA-Z]+/\w+"
    )

    # Find all matches in the text
    links = re.findall(pattern, text)

    return links


# Example usage
text = """
Here are some download links:
https://downloader.cursor.sh/versions/0.34.4/linux/appImage/x86
https://downloader.cursor.sh/versions/0.35.0/windows/exe/x64
"""

download_links = find_download_links(text)
print(download_links)
