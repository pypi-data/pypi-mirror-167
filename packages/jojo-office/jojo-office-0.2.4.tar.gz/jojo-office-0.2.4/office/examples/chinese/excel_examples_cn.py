import office


def example_open_read_write_cells():
    # 打开 datafile.xlsx 文件，返回 workbook 对象
    workbook = office.open_file("datafile.xlsx")

    # 如果 workbook 中有名为 '商品销售' 的工作表
    if '商品销售' in workbook:
        sheet = workbook['商品销售']  # 取得工作表对象
        cell = sheet['B2']  # 取得 B2 单元格对象
        print(cell.value)  # 打印 B1 单元格的值
        cell.value = '新城'  # 修改 B2 单元格的值

        range1 = sheet['B2:C4']  # 取得 B2:C4 区域
        print(range1.value)  # 打印 区域的值

    workbook.save()
    workbook.close()


def example_direct_read_write():
    # 打开 datafile.xlsx 文件，返回 workbook 对象
    wb = office.open_file("datafile.xlsx")

    # 通过workbook对象直接获取 商品销售!B2 单元格对象
    # 如果 商品销售 工作表不存在，则自动创建工作表
    print(wb['商品销售!B2'].value)

    # 通过workbook对象直接写入 商品销售!B2 单元格的值
    # 如果 商品销售 工作表不存在，则自动创建工作表
    wb['商品销售2!B2'].value = "上海"

    print(wb['商品销售!B2'].value)  # 显示该单元格已写入 "上海"

    # 通过workbook对象直接获取 商品销售!B2:C4 区域对象
    range1 = wb['商品销售!B2:C4']
    # 区域对象的 values 属性返回一个列表， 包含区域内所有单元格的值
    print(range1.values)

    # 通过workbook对象获取 商品销售!B2:C4 区域对象, values 写入各单元格的值
    wb['商品销售!B21:C22'].values = [['北京', 18], ['上海', 20]]

    print(wb['商品销售!B21:C22'].values)  # 显示该区域已写入

    wb.save()
    wb.close()


def example_find():
    wb = office.open_file("datafile.xlsx")

    # 查找 商品销售 工作表中 单元格值为 "中山" 的单元格
    # cell = wb.find("商品销售", "中山")
    # print(cell)

    # 查找商品销售表中 "中山" 与 "金额"的交叉单元格，即：中山的金额
    cell = wb.find("商品销售", "中山", "金额")
    if cell:
        print(cell.value)


def find_file(month, sheet_name, area, item):
    """ 查找文件 """
    wb = office.open_file(str(month) + '.xlsx')
    cell = wb.find(sheet_name, area, item)
    if cell:
        return cell.value


def example_expand():
    wb = office.open_file("datafile.xlsx")

    # 取得一个单元格  商品销售!A1
    cell = wb["商品销售"]['A1']

    # 扩展单元格, 返回一个区域, 返回结果是 A1:D6
    print(cell.expand())

    # 扩展单元格(水平方向不扩展), 返回一个区域, 返回结果是 A1:A6
    print(cell.expand(right=None))

    # 扩展单元格(垂直方向不扩展), 返回一个区域, 返回结果是 A1:D1
    print(cell.expand(down=None))


def example_range_to_dataframe():
    wb = office.open_file("datafile.xlsx")

    # 取得一个区域  商品销售!A1:D6
    range1 = wb["商品销售", 'A1:D6']
    print(range1)

    # 取得该区域的数据，返回list
    list1 = range1.to_list()
    print(list1)

    # 取得该区域的数据，返回 DataFrame
    df = range1.to_dataframe()
    print(df)

    # 写入DataFrame数据
    range1.values = df

    # 写入list数据
    range1.values = list1

    # wb.save()
    # wb.close()


if __name__ == "__main__":
    # example_open_read_write_cells()
    # example_direct_read_write()
    # example_find()
    # print(find_file(202201, '商品销售', "中山", "金额"))
    # example_expand()
    example_range_to_dataframe()
