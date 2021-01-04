import pandas as pd
import os

sheet_name = "Sheet1"


class EmptySheetName(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def prepare_data(filename):
    dataframe = pd.read_csv("resources/csv/" + filename)
    dataframe.columns = ["x", "y", "z"]
    dataframe = dataframe.sort_values(by=["z"])
    return dataframe


def get_series_values(dataframe):
    return dataframe.groupby("z").last().index


def create_excel_writer(filename):
    try:
        return pd.ExcelWriter("resources/xlsx/" + filename[:-4] + ".xlsx", engine="xlsxwriter")
    except PermissionError as e:
        print("Destination file opened. Close destination file and try again.")
        raise


def export_data_to_excel(dataframe, writer):
    dataframe.to_excel(writer, index=False, header=False, sheet_name=sheet_name)


def get_chart_series_length(dataframe, x):
    return len(dataframe[dataframe["z"] == x].index.to_list())


def generate_chart(dataframe, workbook):
    series_values = get_series_values(dataframe)
    first_index = 0
    chart = workbook.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
    for x in series_values:
        last_index = get_chart_series_length(dataframe, x) + first_index
        chart.add_series({
            "categories": [sheet_name, first_index, 0, last_index, 0],
            "values": [sheet_name, first_index, 1, last_index, 1],
            "line": {"none": True},
            "marker": {"type": "circle", "size": 4}
        })
        chart.set_y_axis({"major_gridlines": {"visible": False}})
        chart.set_legend({"position": "none"})
        first_index = last_index
    return chart


def prepare_sheet(dataframe, writer):
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    chart = generate_chart(dataframe, workbook)
    worksheet.insert_chart("D1", chart)


def generate_xlsx():
    for filename in os.listdir("resources/csv"):
        if filename.endswith(".csv"):
            dataframe = prepare_data(filename)
            writer = create_excel_writer(filename)
            try:
                if sheet_name == "":
                    raise EmptySheetName("Sheet name cannot be empty")
                export_data_to_excel(dataframe, writer)
                prepare_sheet(dataframe, writer)
                print(filename)
                writer.save()
            except EmptySheetName as e:
                print(e)


def main():
    generate_xlsx()


if __name__ == "__main__":
    main()
