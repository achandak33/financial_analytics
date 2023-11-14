from flask import Flask, render_template, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    daily_returns = pd.read_csv('Data/daily_stock_returns.csv')
    daily_returns['date'] = daily_returns['date'].astype(str)
    daily_portfolio = pd.read_csv('Data/daily_portfolio_returns.csv')
    daily_portfolio['date'] = daily_portfolio['date'].astype(str)
    cum_returns = pd.read_csv('Data/cumulative_returns.csv')
    cum_returns['date'] = cum_returns['date'].astype(str)
    rs1 = pd.read_csv('Data/rolling_stock1.csv')
    rs1['Date'] = rs1['Date'].astype(str)
    rs2 = pd.read_csv('Data/rolling_stock2.csv')
    rs2['Date'] = rs2['Date'].astype(str)
    rs3 = pd.read_csv('Data/rolling_stock3.csv')
    rs3['Date'] = rs3['Date'].astype(str)
    rs4 = pd.read_csv('Data/rolling_stock4.csv')
    rs4['Date'] = rs4['Date'].astype(str)
    rs5 = pd.read_csv('Data/rolling_stock5.csv')
    rs5['Date'] = rs5['Date'].astype(str)
    rsp = pd.read_csv('Data/rolling_rsp.csv')
    rsp['Date'] = rsp['Date'].astype(str)
    reg = pd.read_csv('Data/regression.csv',index_col=0)


    data={}
    data['rds'] = daily_returns.to_dict('index')
    data['pr'] = daily_portfolio.to_dict('index')
    data['cr'] = cum_returns.to_dict('index')
    data['rs1'] = rs1.to_dict('index')
    data['rs2'] = rs2.to_dict('index')
    data['rs3'] = rs3.to_dict('index')
    data['rs4'] = rs4.to_dict('index')
    data['rs5'] = rs5.to_dict('index')
    data['rsp'] = rsp.to_dict('index')
    data['reg'] = reg.to_dict('index')

    return render_template('dashboard.html',**data )




