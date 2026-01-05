import plotext as plt
import pandas as pd
import numpy as np 

def draw_terminal_plot(df:pd.DataFrame, x_col:str, y_col:str,title:str,kind:bool ):
    """
    kind : 'scatter', 'line','bar','hist'
    """
    plt.clear_figure()
    plt.theme("dark")

    x_data = df[x_col].tolist()
    y_data = df[y_col].tolist() if y_col in df.columns else []

    if kind == "scatter":
        plt.scatter(x_data, y_data, marker="small",color="yellow")
    elif kind == "line" :
        plt.plot(x_data, y_data, marker="dot",color="cyan")
    elif kind == "bar" :
        plt.bar(x_data,y_data, marker="sd",color="green") 
    elif kind == "hist" :
        plt.hist(x_data,bins=10, marker="fgh", color="magenta")
    
    plt.title(f"{title} [{kind.upper()}]")
    plt.xlabel(x_col)
    if kind != "hist" :
        plt.ylabel(y_col)
    plt.grid(True,True)
    plt.show()

def show_stats(df:pd.DataFrame, col:str) :
    if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
        print(f"    최대값 : {df[col].max():.4f}")
        print(f"    최소값 : {df[col].min():.4f}")
        print(f"    평균값 : {df[col].mean():.4f}")