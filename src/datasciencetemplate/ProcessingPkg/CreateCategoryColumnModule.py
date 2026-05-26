import polars

from datasciencetemplate.MetaDataPkg.OuputExcelMetaDataModule import OutputExcelMetaData


def CreateCategoryColumn(
    df: polars.DataFrame,
    category: str,
) -> polars.DataFrame:

    print(f"Creating {OutputExcelMetaData.CATEGORY_COLUMN_NAME} column")

    newDf = df.with_columns(
        polars.lit(category).alias(OutputExcelMetaData.CATEGORY_COLUMN_NAME),
    )

    return newDf
