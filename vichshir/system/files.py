import os
import requests


def download_file_from_url(url: str, filename: str, dest_folder: str = './'):
    """
    Credits to: Ivan Vinogradov
    From: https://stackoverflow.com/questions/56950987/download-file-from-url-and-save-it-in-a-folder-python
    """

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))