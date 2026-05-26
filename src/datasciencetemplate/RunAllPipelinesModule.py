from datetime import date

from datasciencetemplate.IngestationPkg.RunIngestAllDataPipelineModule import RunIngestAllDataPipeline
from datasciencetemplate.ProcessingPkg.RunCalculationPipelineModule import RunCalculationPipeline


def RunAllPipelines(
    parameter1: str,
    valuationDate1: date,
    parameter2: str,
    valuationDate2: date,
):
    # first massage all data into a big dataframe
    dfAllData = RunIngestAllDataPipeline()

    # do the calculation steps for each group of data (useful for attributions)
    dfResultOne = RunCalculationPipeline(
        dfBigBlockOfData=dfAllData,
        parameter=parameter1,
        valuationDate=valuationDate1,
    )

    dfResultTwo = RunCalculationPipeline(
        dfBigBlockOfData=dfAllData,
        parameter=parameter2,
        valuationDate=valuationDate1,
    )

    dfResultThree = RunCalculationPipeline(
        dfBigBlockOfData=dfAllData,
        parameter=parameter2,
        valuationDate=valuationDate2,
    )

    allResults = [
        dfResultOne,
        dfResultTwo,
        dfResultThree,
    ]

    return allResults
