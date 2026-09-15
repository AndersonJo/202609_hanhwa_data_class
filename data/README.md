# 수업용 데이터 (5개)

강의 중에 데이터를 새로 내려받는 일이 없도록, 수업에서 쓰는 데이터 5개를 이 폴더에 넣어 두었습니다.
각 디렉터리의 `helper.py` 가 이 폴더의 파일을 읽습니다. (재다운로드: `python data/download.py`)

| 파일 | 출처 | 크기 | 쓰는 곳 |
|---|---|---|---|
| `titanic.csv` | Kaggle **Titanic** (train.csv 와 동일) | 891행 × 12열 | 01~06 전부 |
| `seoul_bike.csv` | Kaggle / UCI **Seoul Bike Sharing Demand** (서울 따릉이) | 8,760행 × 14열 | 03_pandas (시계열), 04_visualization |
| `chinook.sqlite` | **Chinook** 샘플 DB (음악 판매, SQLite 표준 예제) | 11개 테이블 | 05_sql (JOIN, 윈도우) |
| `telco_churn.csv` | Kaggle **Telco Customer Churn** (통신사 고객 이탈) | 7,043행 × 21열 | 06_preprocessing |
| `ames.csv` | Kaggle **House Prices** 의 원본 — De Cock(2011) **Ames Housing** | 2,930행 × 82열 | 07_kaggle_analysis |

## titanic.csv
| 열 | 뜻 |
|---|---|
| PassengerId | 승객 번호 |
| Survived | 생존 여부 (1 = 생존, 0 = 사망) |
| Pclass | 객실 등급 (1, 2, 3) |
| Name, Sex, Age | 이름, 성별, 나이 (Age 결측 177개) |
| SibSp, Parch | 동승한 형제·배우자 수, 부모·자녀 수 |
| Ticket, Fare | 티켓 번호, 요금 |
| Cabin | 객실 번호 (결측 687개) |
| Embarked | 탑승 항구 (S = Southampton, C = Cherbourg, Q = Queenstown, 결측 2개) |

## seoul_bike.csv
원본의 `Temperature(°C)` 같은 헤더를 영문 소문자로 정리하고(UTF-8), 날짜를 `YYYY-MM-DD` 로 바꿔 두었습니다.

| 열 | 뜻 |
|---|---|
| date, hour | 날짜(2017-12-01 ~ 2018-11-30), 시각(0~23) |
| rented | 그 시간에 대여된 자전거 수 |
| temp, humidity, wind, visibility, dew_point, solar, rainfall, snowfall | 기온(°C), 습도(%), 풍속(m/s), 가시거리(10m), 이슬점(°C), 일사량(MJ/m²), 강수량(mm), 적설(cm) |
| season | Winter / Spring / Summer / Autumn |
| holiday | Holiday / No Holiday |
| functioning | 운영일 여부 (Yes / No) |

## chinook.sqlite
음악 판매 회사 DB. 주요 테이블: `Artist` – `Album` – `Track` – `Genre`, `Customer` – `Invoice` – `InvoiceLine`, `Employee`.

## telco_churn.csv
| 열 | 뜻 |
|---|---|
| customerID | 고객 ID |
| gender, SeniorCitizen, Partner, Dependents | 인구통계 |
| tenure | 가입 개월 수 |
| PhoneService ~ StreamingMovies | 사용 중인 서비스 (Yes / No / …) |
| Contract | 계약 기간 (Month-to-month / One year / Two year) |
| PaperlessBilling, PaymentMethod | 청구 방식 |
| MonthlyCharges, TotalCharges | 월 요금, 누적 요금 (TotalCharges 에 공백 11개 → 정제 수업 소재) |
| Churn | 이탈 여부 (Yes 26.5%) |

## ames.csv
아이오와주 에임스에서 2006~2010년에 실제로 거래된 주택 2,930건. 열 82개를 원본 그대로 두었습니다
(탭 구분 텍스트를 csv 로만 바꿨습니다). 열 이름의 공백은 `07_kaggle_analysis/helper.py` 가 읽을 때
`Gr Liv Area` → `gr_liv_area` 로 정리합니다.

| 열 | 뜻 |
|---|---|
| SalePrice | **타깃** — 거래 가격 (달러). 평균 180,796 / 중앙값 160,000 / 최대 755,000, 오른쪽으로 크게 치우침 |
| Overall Qual, Overall Cond | 전체 자재·마감 등급, 전체 상태 등급 (1~10) |
| Gr Liv Area | 지상 거주 면적 (제곱피트) — 가격과 가장 밀접한 면적 열 |
| Total Bsmt SF, 1st Flr SF, 2nd Flr SF | 지하실 / 1층 / 2층 면적 |
| Lot Area, Lot Frontage | 대지 면적, 도로에 접한 길이 (Lot Frontage 결측 16.7% — 진짜 결측) |
| Year Built, Year Remod/Add, Yr Sold, Mo Sold | 건축·리모델링 연도, 거래 연·월 |
| Neighborhood | 동네 (28개). 중앙값이 MeadowV 88,250 ~ StoneBr 319,000 으로 3.6배 차이 |
| Exter Qual, Kitchen Qual, Bsmt Qual, Heating QC | 품질 등급 — `Ex > Gd > TA > Fa > Po` **순서형** (문자지만 순서가 있음) |
| Central Air | 중앙 냉방 유무 (Y / N) |
| Garage Cars, Garage Area | 차고 수용 대수, 차고 면적 (둘이 사실상 같은 것을 재고 있음 → 다중공선성 소재) |
| Sale Condition | 거래 성격. `Normal` 2,413 / `Partial` 245(미완공 판매) / `Abnorml` 190 등 — **정상 거래가 아닌 건이 섞여 있음** |
| Pool QC, Misc Feature, Alley, Fence, Fireplace Qu | 결측률 48~99.6%. 단, 이건 "모름"이 아니라 **"그 시설이 없음"** (Pool QC 가 빈 2,917채는 Pool Area 가 전부 0) |

> 결측·이상치·거래 성격이 모두 "이유가 있는" 데이터라, 07_kaggle_analysis 에서 통계적 판단 연습에 씁니다.
