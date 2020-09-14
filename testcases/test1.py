import unittest
from ddt import ddt, data, unpack, file_data


@ddt     #  修饰测试类
class LearnDdt(unittest.TestCase):


    @data([3, 2], [4, 3], [5, 3])                            # 使用data装饰器，传入列表参数，使用unpack解压缩
    @unpack
    def test_list_extracted_into_arguments(self, first_value, second_value):
        print(first_value, second_value)
        self.assertTrue(first_value > second_value)

    @unpack
    @data({'first': 1, 'second': 3, 'third': 2},              # 使用data将参数按字典格式传入并指定值，解压缩后将值传给参数
            {'first': 4, 'second': 6, 'third': 5})
    def test_dicts_extracted_into_kwargs(self, first, second, third):
        print(first, second, third)
        self.assertTrue(first < third < second)

    @data((3, 2), (4, 3), (5, 3))                              # 使用data加入动态元组组合参数，解压缩将元组的值赋值给参数
    @unpack
    def test_tuples_extracted_into_arguments(self, first_value, second_value):
        print(first_value, second_value)
        self.assertTrue(first_value > second_value)

    @file_data("test_data_dict_dict.json")                      # 使用@file_data 传入文件参数 - json文件
    def test_file_data_json_dict_dict(self, start, end, value):
        print(start, end, value)
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)

    @file_data('test_data_dict.json')                            # 使用@file_data 传入文参数，读取的是字典键的值
    def test_file_data_json_dict(self, value):
        print(value)

    @file_data('test_data_list.json')                              # 使用@file_data 传入文参数，读取的是列表的元素值
    def test_file_data_json_list(self, value):
        print(value)


if __name__ == "__main__":
       unittest.main()