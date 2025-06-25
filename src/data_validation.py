def validate_shots_schema(df):
    expected_cols = ['videoTimestamp', 'location.x', 'location.y', 'shot.isGoal', 'shot.bodyPart']
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
