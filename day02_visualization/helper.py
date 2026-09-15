"""
04_visualization 수업용 helper.
- 이 디렉터리의 주제가 '그리기' 이므로 helper 에는 그리는 코드가 없습니다. 데이터 로더만 있습니다.
- 수업 중에는 `from helper import load_titanic, load_bike` 처럼 사용합니다.
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_titanic() -> pd.DataFrame:
    """Titanic. 그림이 깨지지 않도록 Age 결측은 중앙값으로 채우고 Title 열을 추가한 버전."""
    df = pd.read_csv(DATA_DIR / "titanic.csv")
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna("S")
    df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.")
    return df


def titanic_corr() -> pd.DataFrame:
    """Titanic 숫자 열(Survived, Pclass, Age, SibSp, Parch, Fare)의 상관행렬."""
    df = load_titanic()
    cols = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
    return df[cols].corr()


def load_bike() -> pd.DataFrame:
    """서울 따릉이 시간별 데이터 (8760행). datetime 열 포함."""
    df = pd.read_csv(DATA_DIR / "seoul_bike.csv")
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["datetime"] = df["date"] + pd.to_timedelta(df["hour"], unit="h")
    df["weekday"] = df["date"].dt.day_name()
    df["is_weekend"] = df["date"].dt.dayofweek >= 5
    return df


def load_bike_daily() -> pd.DataFrame:
    """하루 단위로 합친 따릉이 (365행): date, rented(합계), temp(평균), rainfall(합계)."""
    df = load_bike()
    daily = df.groupby("date").agg(
        rented=("rented", "sum"),
        temp=("temp", "mean"),
        rainfall=("rainfall", "sum"),
    ).reset_index()
    return daily


def load_bike_hourly() -> pd.DataFrame:
    """시간대 × 계절별 평균 대여 수 (긴 형식, 96행): hour, season, rented."""
    df = load_bike()
    hourly = df.groupby(["hour", "season"])["rented"].mean().reset_index()
    return hourly


def output_path(filename) -> Path:
    """savefig 실습용 경로. 04_visualization/output/ 폴더를 만들고 그 안의 경로를 돌려줌."""
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    return out_dir / filename
