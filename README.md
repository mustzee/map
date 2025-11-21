# 데이터 분석 학습 프로젝트 📊

파이썬 데이터 배열부터 Pandas, 데이터베이스까지 단계별로 학습하는 자동채점 프로젝트입니다.

## 🎯 학습 목표

1. **Step 1**: Python 리스트와 배열 기초
2. **Step 2**: NumPy 배열 다루기
3. **Step 3**: Pandas 기초 (Series, DataFrame)
4. **Step 4**: Pandas 데이터 처리 및 분석
5. **Step 5**: SQLite 데이터베이스 기초
6. **Step 6**: Pandas와 DB 연동

## 🚀 시작하기

### 1. 환경 설정

```bash
# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 학습 방법

각 단계별로 다음 순서로 학습하세요:

1. `lessons/stepN/` 폴더의 학습 자료 읽기
2. `exercises/stepN_exercises.py` 파일의 연습문제 풀기
3. 자동 채점으로 확인하기

### 3. 자동 채점 실행

```bash
# 전체 테스트 실행
python grader.py

# 특정 단계만 테스트
python grader.py --step 1

# 상세 결과 보기
python grader.py --verbose
```

또는 pytest로 직접 실행:

```bash
# 전체 테스트
pytest tests/

# 특정 단계 테스트
pytest tests/test_step1.py -v
```

## 📁 프로젝트 구조

```
.
├── README.md                 # 프로젝트 소개
├── requirements.txt          # 필요한 패키지
├── grader.py                 # 자동 채점 스크립트
├── data/                     # 실습용 데이터
├── lessons/                  # 단계별 학습 자료
│   ├── step1_arrays/
│   ├── step2_numpy/
│   ├── step3_pandas_basics/
│   ├── step4_pandas_advanced/
│   ├── step5_database/
│   └── step6_integration/
├── exercises/                # 실습 문제 (여기에 답을 작성)
│   ├── step1_exercises.py
│   ├── step2_exercises.py
│   └── ...
└── tests/                    # 자동 채점 테스트
    ├── test_step1.py
    └── ...
```

## 📚 각 단계 소개

### Step 1: Python 리스트와 배열 기초
- 리스트 생성, 인덱싱, 슬라이싱
- 리스트 메서드 활용
- 리스트 컴프리헨션

### Step 2: NumPy 배열
- NumPy 배열 생성 및 조작
- 배열 연산 및 브로드캐스팅
- 배열 인덱싱 및 슬라이싱

### Step 3: Pandas 기초
- Series와 DataFrame 생성
- 데이터 선택 및 필터링
- 기본 통계 함수

### Step 4: Pandas 데이터 처리
- 데이터 정제 (결측치, 중복 처리)
- 그룹화 및 집계
- 데이터 병합 및 조인

### Step 5: SQLite 데이터베이스
- 데이터베이스 생성 및 연결
- SQL 쿼리 (SELECT, INSERT, UPDATE, DELETE)
- 테이블 관리

### Step 6: Pandas-DB 연동
- DataFrame을 데이터베이스로 저장
- SQL 쿼리 결과를 DataFrame으로 불러오기
- 실전 데이터 파이프라인

## 💯 채점 기준

각 단계는 여러 개의 연습문제로 구성되어 있으며, 각 문제는 다음과 같이 채점됩니다:

- ✅ **통과**: 모든 테스트 케이스 통과
- ❌ **실패**: 하나 이상의 테스트 케이스 실패

전체 점수는 통과한 문제 수 / 전체 문제 수 × 100으로 계산됩니다.

## 🎓 학습 팁

1. 각 단계를 순서대로 학습하세요
2. 막히는 부분이 있으면 학습 자료를 다시 읽어보세요
3. 자주 테스트하면서 진행하세요
4. 에러 메시지를 잘 읽고 디버깅하세요

## 📝 라이선스

MIT License
