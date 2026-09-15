"""
수업용 데이터 5개를 내려받아 data/ 에 저장하는 재현용 스크립트.
학생은 실행할 필요 없음 (파일이 이미 리포에 포함되어 있음).

    python data/download.py
"""
import io
import zipfile
import urllib.request
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent

TITANIC_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
BIKE_URL = "https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip"
CHINOOK_URL = "https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_Sqlite.sqlite"
TELCO_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
# Ames Housing: De Cock (2011) 원본. Kaggle "House Prices" 대회 데이터의 출처.
# Dean De Cock, "Ames, Iowa: Alternative to the Boston Housing Data as an
# End of Semester Regression Project", Journal of Statistics Education 19(3), 2011.
AMES_URL = "https://raw.githubusercontent.com/rasbt/machine-learning-book/main/ch09/AmesHousing.txt"


def fetch(url):
    print("downloading:", url)
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def save_titanic():
    (DATA_DIR / "titanic.csv").write_bytes(fetch(TITANIC_URL))


def save_seoul_bike():
    # 원본은 cp1252 인코딩 + "Temperature(°C)" 같은 헤더 → 영문 소문자 헤더, ISO 날짜로 1회 정리
    raw = fetch(BIKE_URL)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        name = [n for n in z.namelist() if n.lower().endswith(".csv")][0]
        df = pd.read_csv(io.BytesIO(z.read(name)), encoding="cp1252")
    df.columns = [
        "date", "rented", "hour", "temp", "humidity", "wind", "visibility",
        "dew_point", "solar", "rainfall", "snowfall", "season", "holiday", "functioning",
    ]
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
    df.to_csv(DATA_DIR / "seoul_bike.csv", index=False, encoding="utf-8")


def save_chinook():
    (DATA_DIR / "chinook.sqlite").write_bytes(fetch(CHINOOK_URL))


def save_telco():
    (DATA_DIR / "telco_churn.csv").write_bytes(fetch(TELCO_URL))


def save_ames():
    # 원본은 탭 구분 텍스트 → csv 로만 바꾸고 열 82개는 그대로 둔다 (열 정리는 helper.py 담당)
    df = pd.read_csv(AMES_URL, sep="\t")
    df.to_csv(DATA_DIR / "ames.csv", index=False)


if __name__ == "__main__":
    save_titanic()
    save_seoul_bike()
    save_chinook()
    save_telco()
    save_ames()
    for p in sorted(DATA_DIR.iterdir()):
        print(f"{p.name:20s} {p.stat().st_size:>10,} bytes")
