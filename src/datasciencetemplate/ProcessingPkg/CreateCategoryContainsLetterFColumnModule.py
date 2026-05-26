import polars

from datasciencetemplate.MetaDataPkg.OuputExcelMetaDataModule import OutputExcelMetaData


def CreateCategoryContainsLetterFColumn(
    df: polars.DataFrame,
) -> polars.DataFrame:

    print(f"Creating {OutputExcelMetaData.CATEGORY_CONTAINS_AN_F_COLUMN_NAME} column")
    
    # Define the two search conditions (case-insensitive)
    contains_f = polars.col(OutputExcelMetaData.CATEGORY_COLUMN_NAME).str.contains("(?i)f")
    contains_o = polars.col(OutputExcelMetaData.CATEGORY_COLUMN_NAME).str.contains("(?i)o")

    newDf = df.with_columns(
        polars.when(contains_f)
        .then(
            polars.lit("Has F"),  # If it has 'F'
        )
        .when(contains_o)
        .then(
            polars.lit("Has O"),  # Else if it has 'O'
        )
        .otherwise(
            polars.lit("no letter o and no letter f"),  # Else it has neither
        )
        .alias(OutputExcelMetaData.CATEGORY_CONTAINS_AN_F_COLUMN_NAME),
    )

    return newDf
