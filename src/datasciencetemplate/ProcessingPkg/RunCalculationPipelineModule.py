from datetime import date

import polars

from datasciencetemplate.ProcessingPkg.CreateCategoryColumnModule import CreateCategoryColumn
from datasciencetemplate.ProcessingPkg.CreateCategoryContainsLetterFColumnModule import CreateCategoryContainsLetterFColumn
from datasciencetemplate.ProcessingPkg.CreateValuationDateColumnModule import CreateValuationDateColumn
from datasciencetemplate.ProcessingPkg.CreateYearFractionColumnModule import CreateYearFractionColumn
from datasciencetemplate.ProcessingPkg.OutputResultToExcelModule import OutputResultToExcel


def RunCalculationPipeline(
    parameter: str,
    valuationDate: date,
    dfBigBlockOfData: polars.DataFrame,
) -> polars.DataFrame:

    newDf = (
        dfBigBlockOfData.pipe(
            CreateValuationDateColumn,
            valuationDate=valuationDate,
        )
        .pipe(
            CreateYearFractionColumn,
        )
        .pipe(
            CreateCategoryColumn,
            category=parameter,
        )
        .pipe(
            CreateCategoryContainsLetterFColumn,
        )  # TODO add a aggeragation function here
        .pipe(
            OutputResultToExcel,
            parameter=parameter,
            valuationDate=valuationDate,
        )
    )

    return newDf
