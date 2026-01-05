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
    parser_sample = subparsers.add_parser('sample', help='test sample CSV ')
    parser_sample.add_argument('filename', nargs='?', default='sample.csv')

    #exe
    args = parser.parse_args() 
    if args.command == 'plot' :
        try :
            if args.chart_type != 'hist' and not args.y :
                parser_plot.error(f"'{args.chart_type}'need y columns")
            print(f"[{args.chart_type.upper()}]... {args.input}")
            df = load_csv(args.input, args.x, args.y)

            draw_terminal_plot(df, args.x,args.y, args.title,args.chart_type)
            stats_col = args.y if args.y else args.x
            show_stats(df, stats_col)

        except Exception as e :
            print(f"Error : {e}")
            sys.exit(1)
    elif args.command == 'sample':
        count = 100
        days = np.arange(1, count + 1)
        temp = 20 + 10 * np.sin(days / 10) + np.random.normal(0, 2, count)
        sales = 50 + (temp * 5) + np.random.normal(0, 10, count)
        humidity = np.random.uniform(30, 90, count)

        # DataFrame
        df = pd.DataFrame({
            'day': days,
            'temp': temp.round(1),     
            'sales': sales.astype(int),  
            'humidity': humidity.round(1)
        })
        
        df.to_csv(args.filename, index=False)

if __name__ == "__main__":
    main() 