from pathlib import Path

def read_requirements():
    return Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()



