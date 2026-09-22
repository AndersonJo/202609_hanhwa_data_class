"""
06_preprocessing 수업용 helper.
- Titanic (01, 02, 05, 06) 과 Telco 고객 이탈 (03, 04, 07, 08) 데이터 로더.
- 전처리 전/후를 비교하는 작은 그림 함수 (그림 그리기는 이 디렉터리의 주제가 아니므로 helper 에 둠).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


# ---------- Titanic ----------
def load_titanic() -> pd.DataFrame:
    """Titanic 원본 (891행 12열)."""
    return pd.read_csv(DATA_DIR / "titanic.csv")


def load_titanic_numeric() -> pd.DataFrame:
    """숫자 열만: Survived, Pclass, Age(NaN 포함), SibSp, Parch, Fare."""
    df = load_titanic()
    return df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]


# ---------- Telco ----------
def load_telco() -> pd.DataFrame:
    """Telco 고객 이탈 (7043행).
    - TotalCharges 를 숫자로 변환 (공백 11개 → NaN)
    - Churn(Yes/No) 을 churn(1/0) 열로 추가, customerID 제거
    """
    df = pd.read_csv(DATA_DIR / "telco_churn.csv")
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["churn"] = (df["Churn"] == "Yes").astype(int)
    df = df.drop(columns=["customerID"])
    return df


def load_telco_encoded():
    """모델에 바로 넣을 수 있는 숫자 행렬 (X, y).
    - 문자열 열은 get_dummies 로 0/1 열로 변환
    - TotalCharges 결측은 중앙값으로 채움
    """
    df = load_telco()
    y = df["churn"]
    X = df.drop(columns=["Churn", "churn"])
    X["TotalCharges"] = X["TotalCharges"].fillna(X["TotalCharges"].median())
    X = pd.get_dummies(X, drop_first=True, dtype=int)
    return X, y


# ---------- 작은 그림 함수 ----------
def plot_box(series, title="Boxplot"):
    """이상치 확인용 상자 그림 하나."""
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.boxplot(series.dropna(), vert=False)
    ax.set_title(title)
    ax.set_yticks([])
    plt.show()


def plot_hist(series, title="Histogram", bins=30):
    """분포 확인용 히스토그램 하나."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.hist(series.dropna(), bins=bins)
    ax.set_title(title)
    plt.show()


def plot_before_after(before, after, titles=("Before", "After"), bins=30):
    """전처리 전/후 분포를 나란히 비교."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))
    axes[0].hist(pd.Series(before).dropna(), bins=bins)
    axes[0].set_title(titles[0])
    axes[1].hist(pd.Series(after).dropna(), bins=bins)
    axes[1].set_title(titles[1])
    plt.tight_layout()
    plt.show()


def class_balance(y):
    """클래스별 개수와 비율을 표로 출력."""
    counts = pd.Series(y).value_counts()
    ratio = pd.Series(y).value_counts(normalize=True).round(3)
    print(pd.DataFrame({"count": counts, "ratio": ratio}))


def show(df, n=5):
    """shape 와 앞 n행을 같이 출력."""
    print("shape:", df.shape)
    try:
        from IPython.display import display
        display(df.head(n))
    except ImportError:
        print(df.head(n))
