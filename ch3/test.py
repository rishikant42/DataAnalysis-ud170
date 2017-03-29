import numpy as np
import pandas as pd

enrollments_df = pd.DataFrame({
    'account_key': [448, 448, 448, 448, 448],
    'status': ['canceled', 'canceled', 'canceled', 'canceled', 'canceled'],
    'join_date': ['2014-11-10', '2014-11-05',  '2015-01-27', '2014-1-10', '2015-03-10'],
    'days_to_cancel': [65, 5, 0, 0, np.nan],
    'is_udacity': [True, True, True, True, True]
    })

print enrollments_df
