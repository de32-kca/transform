import pandas as pd

def df_data(dt=20180101, path='~/code/de32-kca/data_kca/'):
    d = pd.read_parquet(path)
    d = pd.read_parquet(path)

    cols = [
        'movieCd',  # 영화의 대표코드를 출력합니다.
        'movieNm',  # 영화명(국문)을 출력합니다.
        'openDt',   # 영화의 개봉일을 출력합니다.
        'salesAmt', # 해당일의 매출액을 출력합니다.
        'audiCnt',  # 해당일의 관객수를 출력합니다.
        'scrnCnt',  # 해당일자에 상영한 스크린수를 출력합니다.
        'showCnt',  # 해당일자에 상영된 횟수를 출력합니다.
        'load_dt',  # 입수일자
    ]

    df = d[cols + ['repNationCd']]
    df_G = df[(df['load_dt'] == dt) & (d['repNationCd'] == 'G')]
    df_K = df[(df['load_dt'] == dt) & (d['repNationCd'] == 'K')]
    df_M = df_G.merge(df_K, on=cols, how='left')

    df_D = df_M.drop(columns='repNationCd_x').reset_index(drop=True)
    df_N = df_D[df_D['repNationCd_y'].notnull()]
    df_F = df_N.rename(columns={'repNationCd_y': 'nationCd'})

    print(df_F)

df_data()
