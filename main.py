import pandas as pd
from pprint import pprint

#
# def read_Hyde_EMS(file_name='Hyde_EMS.xlsx'):
#     hydes_ems_df = pd.read_excel(file_name)
#     hydes_ems_df = hydes_ems_df.sort_values(by=['MACHINE_ID', 'START_DATE'])
#     hydes_ems_df.to_excel('test.xlsx', index=False)
#
#
# if __name__ == '__main__':
#     read_Hyde_EMS()


hydes_ems_df = pd.read_excel('Hyde_EMS.xlsx')
hydes_ems_df = hydes_ems_df.sort_values(by=['MACHINE_ID', 'START_DATE']).reset_index(drop=True)

hyde_wblc_mtba_df = pd.read_excel('Hyde_WBLC_MTBA.xlsx')
for i in range(len(hyde_wblc_mtba_df)):
    temp_df = hydes_ems_df[hydes_ems_df['MACHINE_CODE'].str.contains(str(hyde_wblc_mtba_df.loc[i, ('MACHINE_ID')]))]
    print(temp_df)
