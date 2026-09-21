"""
01_python 수업용 helper.
- 수업에서 쓰는 실제 파일(data/titanic.csv)을 읽어 주는 작은 함수들.
- 강의 중에는 `from helper import load_titanic_rows` 처럼 한 줄로 가져다 씁니다.
"""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def titanic_path() -> Path:
    """data/titanic.csv 의 절대 경로."""
    return DATA_DIR / "titanic.csv"


def load_titanic_rows(n=None) -> list:
    """CSV 각 행을 dict 로 읽어 리스트로 반환. n 을 주면 앞에서 n개만."""
    with open(titanic_path(), encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if n is not None:
        rows = rows[:n]
    return rows


def load_titanic_ages() -> list:
    """Age 가 비어 있지 않은 승객의 나이(float) 리스트. (714개)"""
    ages = []
    for row in load_titanic_rows():
        if row["Age"] != "":
            ages.append(float(row["Age"]))
    return ages


def load_titanic_column(name) -> list:
    """원하는 열 하나를 문자열 리스트로 반환. 예: load_titanic_column("Sex")"""
    return [row[name] for row in load_titanic_rows()]


def output_path(filename) -> Path:
    """쓰기 실습용 경로. 01_python/output/ 폴더를 만들고 그 안의 경로를 돌려줌."""
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    return out_dir / filename


def show(obj, n=5):
    """리스트/딕셔너리의 앞 n개만 보기 좋게 출력."""
    if isinstance(obj, dict):
        items = list(obj.items())[:n]
        for key, value in items:
            print(f"{key!r}: {value!r}")
        print(f"... total {len(obj)} keys")
    else:
        for item in list(obj)[:n]:
            print(item)
        print(f"... total {len(obj)} items")
