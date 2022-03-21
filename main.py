import pandas as pd
from pprint import pprint


def read_Hyde_EMS(file_name='Hyde_EMS.xlsx'):
    hydes_ems_df = pd.read_excel(file_name)
    hydes_ems_df = hydes_ems_df.sort_values(by=['MACHINE_ID', 'START_DATE'])
    hydes_ems_df.to_excel('test.xlsx', index=False)


if __name__ == '__main__':
    read_Hyde_EMS()
