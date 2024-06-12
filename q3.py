from pandas import DataFrame


def correlation_matrix(data_set: DataFrame) -> None:
    """Fonction pour determiner une corrélation entre l'âge et le salaire

    Args:
        data_set (DataFrame): L'ensemble de données fourni pour la question
    """
    df: DataFrame = data_set[["AGE", "TAUX_HORAIRE_BRUT"]]
    corr_df: DataFrame = df.corr(method="pearson")

    corr_salaire_age = round(corr_df["AGE"]["TAUX_HORAIRE_BRUT"], 2)
    print(f"corrélation entre l'âge et le salaire: {100*corr_salaire_age}%")
    return corr_salaire_age
