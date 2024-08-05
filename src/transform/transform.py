import pandas as pd

def df_data(dt=20180101, path='~/code/de32-kca/data_kca/'):
    d = pd.read_parquet(path)
    d = pd.read_parquet(path)

    cols = [
        'movieCd', #영화의 대표코드를 출력합니다.
        'movieNm', #영화명(국문)을 출력합니다.
        'load_dt', # 입수일자
        'repNationCd', #한국외국영화 유무
    ]

    df = d[cols]
    df_G = df[(df['load_dt'] == dt) & (d['repNationCd'] == 'G')]
    df_K = df[(df['load_dt'] == dt) & (d['repNationCd'] == 'K')]
    df_M = df_G.merge(df_K, on=['movieCd', 'movieNm', 'load_dt'], how='left')

    df_D = df_M.drop(columns='repNationCd_x').reset_index(drop=True)
    df_N = df_D[df_D['repNationCd_y'].notnull()]
    df_F = df_N.rename(columns={'repNationCd_y': 'nationCd'})

    print(df_F)

df_data()
