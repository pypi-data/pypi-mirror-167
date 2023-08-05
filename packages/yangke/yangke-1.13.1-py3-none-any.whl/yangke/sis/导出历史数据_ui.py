import os

from yangke.common.qt import YkWindow, run_app
from PyQt5.QtWidgets import QFileDialog
from yangke.sis.导出SIS历史数据 import load_history_file, find_condition


class MainFrame(YkWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.enable_input_panel()
        self.enable_table()

    def choose_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择历史数据文件", os.getcwd(), "*.xlsx;;*.*")
        if os.path.exists(file):
            self.statusBar().showMessage("正在加载历史数据文件，请耐心等待！")
            self.df = load_history_file(file)
            self.statusBar().showMessage("就绪")

    def get_condition(self):
        """
        根据输入面板内容获取符合条件的工况

        :return:
        """
        values = self.get_value_of_panel(need_dict=True, need_unit=False)
        unit_condition = [("凝汽器热负荷", float(values.get("凝汽器热负荷")), "1%"),
                          ("环境温度", float(values.get("环境温度")), "±2"),
                          ("环境湿度", float(values.get("环境湿度")), "±10"),
                          ]
        cold_condition = {"循泵方式": values.get("循泵方式"), "机力塔数量": int(values.get("机力塔数量"))}

        self.res = find_condition(self.df, unit_condition=unit_condition, cold_condition=cold_condition,
                                  auto_loose=True)
        self.table_widget.display_dataframe(self.res)
        self.statusBar().showMessage(f"指定工况下的平均背压为{self.res.mean(numeric_only=True)['当前背压']}")


run_app(MainFrame)
