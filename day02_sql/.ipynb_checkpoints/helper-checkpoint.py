"""
05_sql 수업용 helper.
- Titanic CSV 를 SQLite 테이블로 만들어 주고, Chinook 샘플 DB 를 열어 줍니다.
- 모든 예제는 `q(conn, "SELECT ...")` 한 줄로 실행하고 결과를 DataFrame 으로 봅니다.
"""
import sqlite3
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def titanic_conn() -> sqlite3.Connection:
    """메모리 SQLite 에 titanic 테이블(891행)을 만들어 연결을 돌려줌."""
    conn = sqlite3.connect(":memory:")
    df = pd.read_csv(DATA_DIR / "titanic.csv")
    df.to_sql("titanic", conn, index=False)
    return conn


def chinook_conn() -> sqlite3.Connection:
    """data/chinook.sqlite (음악 판매 DB, 11개 테이블) 읽기 전용 연결."""
    uri = f"file:{DATA_DIR / 'chinook.sqlite'}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def q(conn, sql) -> pd.DataFrame:
    """SQL 을 실행하고 결과를 DataFrame 으로 반환. (수업의 모든 예제가 이 함수를 씀)"""
    return pd.read_sql(sql, conn)


def show_tables(conn) -> list:
    """DB 안의 테이블 이름 목록."""
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name")
    return [r[0] for r in rows]


def show_columns(conn, table) -> pd.DataFrame:
    """테이블의 열 이름과 타입."""
    df = pd.read_sql(f"PRAGMA table_info({table})", conn)
    return df[["name", "type"]]


def titanic_csv_path() -> str:
    """DuckDB 에서 CSV 를 직접 쿼리할 때 쓰는 문자열 경로."""
    return str(DATA_DIR / "titanic.csv")


def load_titanic() -> pd.DataFrame:
    """DuckDB 가 pandas DataFrame 을 직접 쿼리하는 예제용."""
    return pd.read_csv(DATA_DIR / "titanic.csv")


def output_path(filename) -> Path:
    """parquet 저장 실습용 경로. 05_sql/output/ 폴더를 만들고 그 안의 경로를 돌려줌."""
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    return out_dir / filename
