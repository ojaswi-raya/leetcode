import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate duration for each entry
    employees['total_time'] = employees['out_time'] - employees['in_time']
    
    # Group by event_day and emp_id, then sum the total_time
    result = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    
    # Rename event_day column to day
    result.rename(columns={'event_day': 'day'}, inplace=True)
    
    return result