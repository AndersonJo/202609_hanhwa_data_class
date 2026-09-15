"""
03_pandas 수업용 helper.
- Titanic (01~06, 09) 과 서울 따릉이 (07~08) 데이터를 DataFrame 으로 읽어 줍니다.
- 수업 중에는 `from helper import load_titanic` 처럼 사용합니다.
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_titanic() -> pd.DataFrame:
    """Titanic 원본 그대로 (891행 12열). 정제는 수업에서 직접 합니다."""
    return pd.read_csv(DATA_DIR / "titanic.csv")


def load_titanic_clean() -> pd.DataFrame:
    """04_cleaning 에서 배운 정제를 미리 적용한 버전.
    - Age 결측 → 중앙값, Embarked 결측 → 최빈값
    - Name 에서 호칭(Title) 열 추가
    """
    df = load_titanic()
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.")
    return df


def port_lookup() -> pd.DataFrame:
    """Embarked 코드 ↔ 항구 이름 대응표 (merge 실습용)."""
    return pd.DataFrame({
        "Embarked": ["S", "C", "Q"],
        "Port": ["Southampton", "Cherbourg", "Queenstown"],
    })


def split_titanic():
    """Titanic 을 두 표로 나눔 (merge 실습용).
    - people : PassengerId, Name, Sex, Age
    - trips  : PassengerId, Pclass, Fare, Embarked, Survived
    """
    df = load_titanic()
    people = df[["PassengerId", "Name", "Sex", "Age"]]
    trips = df[["PassengerId", "Pclass", "Fare", "Embarked", "Survived"]]
    return people, trips


def load_bike_raw() -> pd.DataFrame:
    """서울 따릉이 원본 (8760행). date 열이 아직 문자열 상태 → 07 에서 직접 변환."""
    return pd.read_csv(DATA_DIR / "seoul_bike.csv")


def load_bike() -> pd.DataFrame:
    """서울 따릉이. date 를 datetime 으로 바꾸고 date+hour 를 합친 datetime 열을 추가."""
    df = load_bike_raw()
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["datetime"] = df["date"] + pd.to_timedelta(df["hour"], unit="h")
    return df


def output_path(filename) -> Path:
    """저장 실습용 경로. 03_pandas/output/ 폴더를 만들고 그 안의 경로를 돌려줌."""
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    return out_dir / filename


def show(df, n=5):
    """shape 와 앞 n행을 같이 출력."""
    print("shape:", df.shape)
    try:
        from IPython.display import display
        display(df.head(n))
    except ImportError:
        print(df.head(n))
