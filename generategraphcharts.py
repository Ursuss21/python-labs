import pandas as pd
import os


class EmptySheetName(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class GraphGenerator:
    XLSX_PATH = "resources/xlsx/"
    CSV_PATH = "resources/csv/"
    SUFFIX = ".csv"

    def __init__(self, file, sheet_name="Sheet1", chart_destination_cell="D1"):
        self.sheet_name = sheet_name
        self.file = file

        self.dataframe = None
        self.writer = None

        self.workbook = None
        self.worksheet = None
        self.chart = None
        self.series_values = None

        self.first_index = 0
        self.last_index = 0
        self.chart_destination_cell = chart_destination_cell

    def read_data_from_csv(self):
        self.dataframe = pd.read_csv(self.CSV_PATH + self.file)

    def set_dataframe_column_names(self):
        self.dataframe.columns = ["x", "y", "label"]

    def sort_dataframe_column(self, column_name):
        self.dataframe = self.dataframe.sort_values(by=[column_name])

    def prepare_data(self):
        self.read_data_from_csv()
        self.set_dataframe_column_names()
        self.sort_dataframe_column("label")

    def create_excel_writer(self):
        try:
            self.writer = pd.ExcelWriter(self.XLSX_PATH + self.file[:-4] + ".xlsx",
                                         engine="xlsxwriter")
        except PermissionError:
            print("Destination file opened. Close destination file and try again.")
            raise

    def export_data_to_excel(self):
        self.dataframe.to_excel(self.writer,
                                index=False,
                                header=False,
                                sheet_name=self.sheet_name)

    def create_workbook(self):
        self.workbook = self.writer.book

    def create_worksheet(self):
        self.worksheet = self.writer.sheets[self.sheet_name]

    def prepare_sheet(self):
        self.create_workbook()
        self.create_worksheet()

    def get_series_values(self):
        self.series_values = self.dataframe.groupby("label").last().index

    def create_chart(self):
        self.chart = self.workbook.add_chart({"type": "scatter",
                                              "subtype": "straight_with_markers"})

    def set_first_index(self):
        self.first_index = self.last_index

    def set_last_index(self, series_value):
        self.last_index = len(self.dataframe[self.dataframe["label"] == series_value].index.to_list()) \
                          + self.first_index

    def add_series(self):
        self.chart.add_series({
            "categories": [self.sheet_name, self.first_index, 0, self.last_index, 0],
            "values": [self.sheet_name, self.first_index, 1, self.last_index, 1],
            "line": {"none": True},
            "marker": {"type": "circle", "size": 4}
        })

    def create_series(self):
        for series_value in self.series_values:
            self.set_last_index(series_value)
            self.add_series()
            self.set_first_index()

    def set_chart_gridlines_visibility(self, value):
        self.chart.set_y_axis({"major_gridlines": {"visible": value}})

    def disable_chart_legend(self):
        self.chart.set_legend({"position": "none"})

    def insert_chart_into_sheet(self):
        self.worksheet.insert_chart(self.chart_destination_cell, self.chart)

    def generate_chart(self):
        self.get_series_values()
        self.create_chart()
        self.create_series()
        self.set_chart_gridlines_visibility(False)
        self.disable_chart_legend()
        self.insert_chart_into_sheet()

    def save_chart(self):
        self.writer.save()

    def prepare_excel_sheet_with_chart(self):
        self.create_excel_writer()
        self.prepare_data()
        self.export_data_to_excel()
        self.prepare_sheet()
        self.generate_chart()
        self.save_chart()


def main():
    for filename in os.listdir(GraphGenerator.CSV_PATH):
        if filename.endswith(GraphGenerator.SUFFIX):
            g = GraphGenerator(filename)
            g.prepare_excel_sheet_with_chart()


if __name__ == "__main__":
    main()
