import pandas as pd
from pandas import DataFrame
from itertools import combinations


class Subdivision:
    def __init__(self, *args, save_path=None, **kwargs):
        # 文件夹路径
        self.folder_path = save_path
        # 字段名字
        self.field_name = args
        # 区分字段
        self.same_index = kwargs.get('same_index')
        # 表数据
        self.sheet_data = kwargs.get('sheet_data')
        # 项目名字+用户记录数
        self.dataframe_list = []
        self.new_element_list = []
        self.tuple_list = []
        self.cloud_list = [self.sheet_data]
        self.index_combination()
        self.SheetObject = {}
        self.decompose()

    # 字段组合
    def index_combination(self):
        for a in range(len(self.field_name), 0, -1):
            for b in combinations(self.field_name, a):
                self.tuple_list.append(b)
                self.new_element_list.append("-".join(b))

    # 算法中心
    def decompose(self):
        for subscript, tuple_elemnet in enumerate(self.tuple_list):
            elementSame = self.cloud_list[0][self.cloud_list[0].duplicated(subset=tuple_elemnet, keep=False)]
            if len(elementSame):
                self.cloud_list[0] = self.cloud_list[0].drop(index=elementSame.index)
                element_same = elementSame.sort_values(tuple_elemnet[0])
                index_list = list(tuple_elemnet)
                index_list.append(self.same_index)
                index_dataframe = element_same[index_list]
                element_same.drop(columns=index_list, inplace=True)
                new_index = pd.MultiIndex.from_arrays(index_dataframe.values.T, names=index_list)
                element_same.set_index(keys=new_index, inplace=True)
                self.dataframe_list.append([F"{self.new_element_list[subscript]}-same", element_same.shape[0]])
                if self.folder_path:
                    element_same.to_excel(self.folder_path + FR"\{self.new_element_list[subscript]}-same.xlsx")
                else:
                    self.SheetObject.update({F"{self.new_element_list[subscript]}-same":element_same})
            else:
                continue

        if self.folder_path:
            self.cloud_list[0].to_excel(self.folder_path + R"\Not the same.xlsx", index=False)
        else:
            self.SheetObject.update({"Not the same": self.cloud_list[0]})
        self.dataframe_list.append(["Not the same", self.cloud_list[0].shape[0]])
        data_frame = DataFrame(data=self.dataframe_list, columns=["Classification", "quantity"])
        data_frame.loc[data_frame.shape[0]] = ["Total", data_frame.quantity.sum()]
        if self.folder_path:
            data_frame.to_excel(self.folder_path + R"\statistics.xlsx")
        else:
            self.SheetObject.update({"statistics": data_frame})