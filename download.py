import requests
from pathlib import Path

URL = "https://www.treasury.gov/ofac/downloads/sdn.csv"

def download_sdn():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    file_path = data_dir / "ofac_sdn.csv"
    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"✅ SDN list downloaded to {file_path}")

if __name__ == "__main__":
    download_sdn()

