import pandas as pd
import os
from typing import Optional

def load_csv(file_path: str, x_col: str, y_col: Optional[str] = None):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Filed found data{file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Filed load csv: {e}")

    # 1. 불러올 컬럼 리스트 정리 (중복 제거 로직)
    cols_to_use = [x_col]
    if y_col and y_col != x_col: # y가 존재하고, x랑 다를 때만 추가
        cols_to_use.append(y_col)

    # 2. 컬럼 존재 여부 확인
    for col in cols_to_use:
        if col not in df.columns:
            raise ValueError(
                f"faild found colums: {col}\n"
                f"exist columns: {list(df.columns)}"
            )

    # 3. 데이터 선택 (copy로 깊은 복사)
    clean_df = df[cols_to_use].copy()
    
    # 4. 숫자 변환 (errors='coerce'로 문자열을 NaN으로 변환)
    for col in cols_to_use:
        clean_df[col] = pd.to_numeric(clean_df[col], errors='coerce')
    
    # 5. 결측치 제거
    clean_df = clean_df.dropna()

    return clean_df