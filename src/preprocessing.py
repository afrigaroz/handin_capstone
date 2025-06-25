def clean_shots(df):
    df['shot.bodyPart'] = df['shot.bodyPart'].fillna('unknown')
    return df
