from datetime import date

import polars

from datasciencetemplate.MetaDataPkg.OuputExcelMetaDataModule import OutputExcelMetaData

CUTOFF_DATE = date(2021, 1, 2)


def CreateYearFractionColumn(
    df: polars.DataFrame,
) -> polars.DataFrame:

    print(f"Creating {OutputExcelMetaData.YEAR_FRAC_COLUMN_NAME} column")

    newDf = df.with_columns(
        (
            polars.col(
                OutputExcelMetaData.VALUATION_DATE_COLUMN_NAME,
            )
            - CUTOFF_DATE
        ).alias(OutputExcelMetaData.YEAR_FRAC_COLUMN_NAME),
    )

    return newDf
