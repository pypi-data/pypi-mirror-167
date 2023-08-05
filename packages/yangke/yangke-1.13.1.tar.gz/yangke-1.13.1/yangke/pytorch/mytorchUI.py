import os

import pandas as pd

from yangke.common.config import logger
from yangke.common.qt import YkWindow, run_app, YkItem
from PyQt5.QtWidgets import QFileDialog
from yangke.common.fileOperate import read_csv_ex
from yangke.base import auto_save_para


class MainWindow(YkWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # 完成了通用变量的加载
        self.df = self.proj.get("dataframe")  # 取到本应用的特有变量
        self.file = self.proj.get("datafile")
        self.display_project(self.proj)  # 展示本应用的数据至画面

    def init_inner_ui(self):
        if self.proj.get("table_enabled"):
            self.enable_table()
        self.set_value_of_panel({"数据文件": self.file})
        if self.file is not None:
            self.read_data()

    def display_project(self, proj=None):
        """
        展示数据至画面

        :param proj:
        :return:
        """
        if self.file is not None:
            self.enable_input_panel()
            self.set_value_of_panel({"数据文件": self.file})
            if os.path.exists(self.file):
                self.df = read_csv_ex(self.file)
            self.enable_table()
            if self.df is None:
                return
            self.table_widget.display_dataframe(self.df)
            title = list(self.df.columns)
            items = [
                YkItem(label="选择神经网络输入参数：", size=[200, 50, 50]),
                YkItem(label="input 1", value=title, size=[50, 150, 100]),
                YkItem(label="", value='<button on-click="remove_input_item()">删除输入参数</button>',
                       unit='<button on-click="insert_input_item()">添加输入参数</button>', size=[50, 100, 100]),

                YkItem(label="选择神经网络输出参数：", size=[200, 50, 50]),
                YkItem(label="output 1", value=title, size=[50, 150, 100]),
                YkItem(label="", value='<button on-click="remove_input_item()">删除输出参数</button>',
                       unit='<button on-click="insert_output_item()">添加输出参数</button>', size=[50, 100, 100]),
            ]
            self.input_panel.append_item(items)
            self.proj.update({"dataframe": self.df})


    def choose_file(self):
        files, _ = QFileDialog.getOpenFileName(self, '选择数据文件', os.getcwd(), "All Files(*)")
        self.set_value_of_panel({"数据文件": files})
        self.file = files
        self.proj.update({"datafile": files})
        print("选择文件")

    def read_data(self):
        files = self.get_value_of_panel(need_unit=False, need_dict=True)['数据文件']
        if isinstance(files, list):
            for file in files:
                if os.path.exists(file):
                    self.df = read_csv_ex(file)
        else:
            if os.path.exists(files):
                self.df = read_csv_ex(files)
        self.enable_table()
        if self.df is None:
            return
        self.table_widget.display_dataframe(self.df)
        title = list(self.df.columns)
        items = [
            YkItem(label="选择神经网络输入参数：", size=[200, 50, 50]),
            YkItem(label="input 1", value=title, size=[50, 150, 100]),
            YkItem(label="", value='<button on-click="remove_input_item()">删除输入参数</button>',
                   unit='<button on-click="insert_input_item()">添加输入参数</button>', size=[50, 100, 100]),

            YkItem(label="选择神经网络输出参数：", size=[200, 50, 50]),
            YkItem(label="output 1", value=title, size=[50, 150, 100]),
            YkItem(label="", value='<button on-click="remove_input_item()">删除输出参数</button>',
                   unit='<button on-click="insert_output_item()">添加输出参数</button>', size=[50, 100, 100]),
        ]
        self.input_panel.append_item(items)
        self.proj.update({"dataframe": self.df})

    def insert_input_item(self):
        values = self.get_value_of_panel(need_dict=True, need_unit=False)
        input_values = [e for e in values if e.startswith("input")]
        title = list(self.df.columns)
        item = YkItem(label=f"input {len(input_values) + 1}", value=title, size=[50, 150, 100])
        self.input_panel.insert_item(len(input_values) + 2, item)

    def remove_input_item(self):
        values = self.get_value_of_panel(need_dict=True, need_unit=False)
        input_values = [e for e in values if e.startswith("input")]
        self.input_panel.remove_item(values.index(input_values[-1]))

    def insert_output_item(self):
        values: dict = self.get_value_of_panel(need_dict=True, need_unit=False)
        output_values = [k for k, v in values.items() if k is not None and k.startswith("output")]
        title = list(self.df.columns)
        item = YkItem(label=f"output {len(output_values) + 1}", value=title, size=[50, 150, 100])
        idx = list(values.keys()).index(output_values[-1]) + 1
        self.input_panel.insert_item(idx, item)

    def remove_output_item(self):
        values = self.get_value_of_panel(need_dict=True, need_unit=False)
        input_values = [e for e in values if e.startswith("output")]
        self.input_panel.remove_item(values.index(input_values[-1]))


run_app(MainWindow)
