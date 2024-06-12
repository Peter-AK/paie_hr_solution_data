from pandas import DataFrame


def avg_age_by_dept(data_set: DataFrame) -> DataFrame:
    """Fonction pour determiner l'âge moyen des
    employés dans chaque département

    Args:
        data_set (DataFrame): L'ensemble de données fourni pour la question
    """
    df: DataFrame = data_set.groupby("EMPLOI")["AGE"].mean()
    print(df)
    return df
