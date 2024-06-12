from datetime import datetime, timedelta

import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt


def avg_salary(data_set: DataFrame) -> Series:
    """Fonction qui permet de determiner le salaire moyen
    en fonction du nombre d'années d'expérience

    Args:
        data_set (DataFrame): L'ensemble de données fourni pour la question
    """

    # Remove any faulty dates from the column
    data_set["DEBUT_CONTRAT"] = pd.to_datetime(
        data_set["DEBUT_CONTRAT"],
        errors="coerce",
    )
    data_set.dropna(inplace=True, subset=["DEBUT_CONTRAT"])

    # Gets the delta years between start date and tody
    data_set["delta_contract_days"] = datetime.today() - data_set["DEBUT_CONTRAT"]
    data_set["delta_contract_years"] = data_set["delta_contract_days"] / timedelta(
        days=362
    )

    # Bins and groups data by the delta years column
    result_set: Series = data_set.groupby(
        pd.cut(
            data_set["delta_contract_years"],
            5,
        ),
        observed=True,
    )["TAUX_HORAIRE_BRUT"].mean()

    # Plot results
    result_set.plot.bar(
        rot=False,
        title="salaire moyen en fonction d'années d'expérience",
    )
    plt.ylabel("salaire moyen [Eur/heure]")
    plt.xlabel("années d'expérience [années]")
    plt.show()
    print(result_set)
    return result_set
