from datetime import date

import polars


def OutputResultToExcel(
    df: polars.DataFrame,
    valuationDate: date,
    parameter: str,
) -> polars.DataFrame:

    SUFFIX_LABEL = f"{valuationDate}{parameter}"

    df.write_excel(
        f"outputData/{SUFFIX_LABEL}output.xlsx",
    )

    return df
