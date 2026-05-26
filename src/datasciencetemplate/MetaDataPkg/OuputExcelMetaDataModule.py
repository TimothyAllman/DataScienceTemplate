from enum import StrEnum


class OutputExcelMetaData(StrEnum):
    VALUATION_DATE_COLUMN_NAME = "Valuation Date"
    YEAR_FRAC_COLUMN_NAME = "Year Fraction"
    CATEGORY_COLUMN_NAME = "Category"
    CATEGORY_CONTAINS_AN_F_COLUMN_NAME = "does the category column contain an F"
