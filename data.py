from pathlib import Path
import pandas as pl
import tarfile as tt
import urllib.request

# Use housing for the first implementation, replace titanic later

def load_house_data():
    # tarball_path = Path("datasets/housting.gz")
    tarball_path = Path("datasets/titanic.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/titanic.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tt.open(tarball_path) as housing_tg:
            housing_tg.extractall(path="datasets")
    return pl.read_csv("datasets/titanic/test.csv")

titanic = load_house_data()
        