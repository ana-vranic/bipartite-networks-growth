import pandas as pd
from datetime import datetime

def df_reindex(scale):
    scale = scale.sort_values(by='year_month')
    scale = scale.set_index('year_month')
    idx = pd.date_range(*(pd.to_datetime([scale.index[0], scale.index[-1]]) + pd.offsets.MonthEnd()), freq='M')
    idx = [x.strftime('%Y-%m') for x in idx ]
    scale = scale.reindex(idx, fill_value=0).reset_index()
    return scale

name = "data_to2012year"
df = []
filename = "%s_newusers"%name
with open(filename, 'r') as F:
    lines = F.readlines()

    for line in lines:

        key, size = line.split('\t')
        size = size.strip()
        key = key.strip('[]').split(',')
        y = key[0].strip()
        m = key[1].strip()
        d1 = datetime.strptime(y+'-'+m, "%Y-%m")
        d1 = d1.strftime("%Y-%m")

        df.append((d1,int(size)))

df_new_users = pd.DataFrame(df, columns = ['year_month', 'new_users'])
df3 = df_reindex(df_new_users)


df = []
with open('%s_newgroups'%name, 'r') as F:
    lines = F.readlines()

    for line in lines:

        key, size = line.split('\t')
        size = size.strip()
        key = key.strip('[]').split(',')
        y = key[0].strip()
        m = key[1].strip()
        d1 = datetime.strptime(y+'-'+m, "%Y-%m")
        d1 = d1.strftime("%Y-%m")

        df.append((d1,int(size)))

df_new_groups = pd.DataFrame(df, columns = ['year_month', 'new_groups'])
df1 = df_reindex(df_new_groups)

df = []
with open('%s_activeusers'%name, 'r') as F:
    lines = F.readlines()

    for line in lines:

        key, size = line.split('\t')
        size = size.strip()
        key = key.strip('[]').split(',')
        y = key[0].strip()
        m = key[1].strip()
        d1 = datetime.strptime(y+'-'+m, "%Y-%m")
        d1 = d1.strftime("%Y-%m")

        df.append((d1,int(size)))

df_active_users = pd.DataFrame(df, columns = ['year_month', 'active_users'])
df2 = df_reindex(df_active_users)

dataf = pd.merge(df1, df2, how='outer')
df = pd.merge(dataf, df3, how='outer' )


df['old_users'] = df['active_users'] - df['new_users']

df['total_users'] = df['new_users']

for i in range(1,len(df)):
    df.loc[i, 'total_users'] =  df.loc[i, 'new_users'] + df.loc[i-1, 'total_users']


df['total_groups'] = df['new_groups']

for i in range(1,len(df)):
    df.loc[i, 'total_groups'] =  df.loc[i, 'new_groups'] + df.loc[i-1, 'total_groups']

df.to_csv('%s_ts.csv'%name, index=None)
