# Termi Plot
---

### Directory Structure
``` plaintext
termi-plot/
│
├── data/                 # 테스트용 CSV 파일들을 넣을 곳
│   └── .keep             # 빈 폴더 유지용 (선택)
│
├── src/                  # 소스 코드 모음 (핵심 로직)
│   ├── __init__.py       # 파이썬 패키지로 인식되게 함 (비워둬도 됨)
│   ├── loader.py         # [데이터] 파일을 읽고 전처리하는 역할
│   ├── plotter.py        # [시각화] plotext로 그래프 그리는 역할
│   └── cli.py            # [인터페이스] Typer 명령어 및 진입점
│
├── .gitignore            # 깃에 올리지 않을 파일 목록
├── requirements.txt      # 필요한 라이브러리 목록
├── README.md             # 프로젝트 설명서
└── main.py               # 실행을 위한 진입 파일 (Entry Point)
```