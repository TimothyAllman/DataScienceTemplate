from datetime import date

from datasciencetemplate.RunAllPipelinesModule import RunAllPipelines

INPUT_PARAM_1 = "frost"
INPUT_PARAM_2 = "category_5"
VALUATION_DATE_1 = date(2025, 3, 2)
VALUATION_DATE_2 = date(2026, 3, 2)

# now run the pipeline
RunAllPipelines(
    parameter1=INPUT_PARAM_1,
    valuationDate1=VALUATION_DATE_1,
    parameter2=INPUT_PARAM_2,
    valuationDate2=VALUATION_DATE_2,
)
