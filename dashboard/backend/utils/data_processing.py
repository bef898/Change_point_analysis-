def filter_data_by_date(df, start_date, end_date):
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]
