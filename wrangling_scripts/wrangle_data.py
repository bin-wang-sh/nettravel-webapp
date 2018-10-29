import pandas as pd
import plotly.graph_objs as go
from datetime import datetime

# TODO: Scroll down to line 157 and set up a fifth visualization for the data dashboard
def clean_data(dataset):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        new_df(dataframe): data after 2007 year.

    """
    df = pd.read_csv(dataset)

    # convert date to datetime64
    df['date']=pd.to_datetime(df['date'])

    # calculate profit and marketing share
    total_df=df.groupby('date')['profit','income'].sum()
    total_df.reset_index(inplace=True)
    total_df.columns=['date','total_profit','total_income']
    new_df=pd.merge(df, total_df, on='date',how='left')
    new_df['profit_ratio']=new_df['profit']/new_df['total_profit']
    new_df['income_ratio']=new_df['income']/new_df['total_income']

    # convert code to string
    new_df['code']=new_df['code'].apply(lambda x:"{:0>6d}".format(x)).astype(str)
    new_df['year'] = new_df['date'].dt.year

    # output clean csv file
    return new_df.loc[new_df['year'] > 2007,:]

def get_stack(df,col):
    """ Get stack dataset on data ,code and target column
    Args:
        df(dataframe): clean dataset for inputself.
        col(string): target column nameself.
    Return:
        new_df: stack dataset on target column.

    """
    top5_list=['600519', '000858', '002304', '000568', '600600']
    df_tmp=df.loc[df.code.isin(top5_list)].sort_values(by=['year',col], ascending=False)
    df_ratio=df_tmp.loc[:,['year','code',col]]
    df_stack=df_ratio.pivot(index='year', columns='code', values=col)
    return df_stack
def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots arable land from 1990 to 2015 in top 10 economies
  # as a line chart
    graph_one = []
    df = clean_data('data/wine.csv')
    df_fig=get_stack(df,'profit_ratio')
    codelist = df_fig.columns.values.tolist()[:5]
    
    for code in codelist:
        x_val = df_fig.index.values.tolist()
        y_val = df_fig[code].tolist()
        graph_one.append(
        go.Bar(
             x=x_val, #year
             y=y_val,  #profit ratio
             name=code)
             )
    layout_one = dict(title = 'Change in profit share per code 2008 to 2017',
                    xaxis = dict(title = 'Year'),
                    yaxis = dict(title = 'Profit ratio'),
                    barmode='stack'
                    )

# second chart plots marketing share 2007 to 2017 as a bar chart

    graph_two = []
    df = clean_data('data/wine.csv')
    df_fig=get_stack(df,'income_ratio')
    codelist = df_fig.columns.values.tolist()[:5]
    
    for code in codelist:
        x_val = df_fig.index.values.tolist()
        y_val = df_fig[code].tolist()
        graph_two.append(
            go.Bar(
             x=x_val, #year
             y=y_val,  #income ratio
             name=code)
             )
    layout_two = dict(title = 'Change in Marketing share per code 2008 to 2017',
                    xaxis = dict(title = 'Year'),
                    yaxis = dict(title = 'income ratio'),
                    barmode='stack'
                    )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    return figures
