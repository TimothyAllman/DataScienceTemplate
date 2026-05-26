from datetime import date

import polars

from datasciencetemplate.MetaDataPkg.OuputExcelMetaDataModule import OutputExcelMetaData


def CreateValuationDateColumn(
    df: polars.DataFrame,
    valuationDate: date,
) -> polars.DataFrame:

    print(f"Creating {OutputExcelMetaData.VALUATION_DATE_COLUMN_NAME} column")

    newDf = df.with_columns(
        polars.lit(valuationDate).alias(OutputExcelMetaData.VALUATION_DATE_COLUMN_NAME),
    )

    return newDf
