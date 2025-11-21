# 샘플 데이터

이 폴더에는 연습용 샘플 데이터 파일이 포함되어 있습니다.

## 파일 목록

### sample_students.csv
학생 정보 데이터
- `id`: 학생 ID
- `name`: 이름
- `age`: 나이
- `major`: 전공
- `gpa`: 학점 (Grade Point Average)

### sample_sales.csv
판매 데이터
- `date`: 날짜
- `product`: 제품명
- `category`: 카테고리
- `price`: 가격
- `quantity`: 수량

## 사용 예시

```python
import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('data/sample_students.csv')
print(df.head())

# 데이터 분석
print(df.groupby('major')['gpa'].mean())
```

## 주의사항

- 이 파일들은 학습용 샘플 데이터입니다
- 실제 프로젝트에서는 더 큰 데이터셋을 사용하게 됩니다
- `.gitignore`에 의해 다른 CSV 파일들은 버전 관리에서 제외됩니다
