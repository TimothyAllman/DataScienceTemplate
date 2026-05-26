import polars


def RunIngestAllDataPipeline() -> polars.DataFrame:

    # get data source 1
    dfCsvData = polars.DataFrame(
        {
            "id": [1, 2],
            "name": ["Alice", "Bob"],
        }
    )

    # get data source 2
    dfExcelData = polars.DataFrame(
        {
            "id": [2, 3],
            "age": [25, 30],
        }
    )

    # Standard inner join
    result = dfCsvData.join(
        dfExcelData,
        on="id",
        how="inner",
    )

    return result
