import argparse
import sys
import pandas as pd
import numpy as np
from src.loader import load_csv
from src.plotter import draw_terminal_plot, show_stats

def main() :
    parser = argparse.ArgumentParser(
        description="Termi-Plot : make plot in terminor"    
    )
    subparsers = parser.add_subparsers(dest='command', required=True,help="Chose to execute command")

    # 'plot'
    parser_plot = subparsers.add_parser('plot', help="Draw variable chart")

    parser_plot.add_argument(
        'chart_type',
        choices=['bar','line','scatter','hist'],
        help = 'sort of chart (bar, line, scatter, hist)'
    )
    parser_plot.add_argument('-i','--input',required=True,help="input file path")

    parser_plot.add_argument('-x','--x', required=True, help='column of x')
    parser_plot.add_argument('-y','--y', required=False, help='column of y')
    parser_plot.add_argument('-t','--title', default="Data Analysis",help="title")

    # sample
    parser_sample = subparsers.add_parser('sample', help='테스트용 샘플 CSV 생성')
    parser_sample.add_argument('filename', nargs='?', default='sample.csv')

    #exe
    args = parser.parse_args() 
    if args.command == 'plot' :
        try :
            if args.chart_type != 'hist' and not args.y :
                parser_plot.error(f"'{args.chart_type}' 차트는 --y 옵션이 필수입니다.")
            print(f"[{args.chart_type.upper()}] 차트 그리는 중... {args.input}")
            df = load_csv(args.input, args.x, args.y)

            draw_terminal_plot(df, args.x,args.y, args.title,args.chart_type)
            stats_col = args.y if args.y else args.x
            show_stats(df, stats_col)

        except Exception as e :
            print(f"Error : {e}")
            sys.exit(1)
    elif args.command == 'sample':
        # 데이터 개수 설정
        count = 100
        
        # 1. 시계열 데이터 (Day)
        days = np.arange(1, count + 1)
        
        # 2. 기온 (Sine 파형 + 노이즈) -> Line 차트용
        temp = 20 + 10 * np.sin(days / 10) + np.random.normal(0, 2, count)
        
        # 3. 아이스크림 판매량 (기온과 정비례) -> Scatter 차트용
        sales = 50 + (temp * 5) + np.random.normal(0, 10, count)
        
        # 4. 습도 (랜덤값) -> Histogram용
        humidity = np.random.uniform(30, 90, count)

        # DataFrame 생성
        df = pd.DataFrame({
            'day': days,
            'temp': temp.round(1),       # 소수점 1자리
            'sales': sales.astype(int),  # 정수형
            'humidity': humidity.round(1)
        })
        
        df.to_csv(args.filename, index=False)
        
        print(f"✅ 멀티 컬럼 샘플 파일 생성 완료: {args.filename}")
        print(f"   컬럼 목록: {list(df.columns)}")
        print(f"👉 테스트 예시: ./plot scatter -i {args.filename} -x temp -y sales")

if __name__ == "__main__":
    main() 