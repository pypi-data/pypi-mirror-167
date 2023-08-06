import office


def example_basic():
    # open file datafile.xlsx, return workbook object
    workbook = office.open_file("datafile.xlsx")

    # list worksheets
    sheet_names = workbook.sheetnames
    print(sheet_names)

    # get a sheet
    sheet = workbook['Sales']
    print(sheet.name)

    # get a cell
    cell = sheet['B2']
    print(cell.value)

    # write a cell
    cell.value = 'New City'

    # save
    workbook.save("newfile.xlsx")

    # close
    workbook.close()


def example_workbook_worksheet():
    # create a newfile.xlsx, copied from the template file
    # if the newfile.xlsx not exists, create it.
    # if the newfile.xlsx already exists, overwrite it.
    workbook = office.open_file("newfile.xlsx", template="datafile.xlsx")

    # create a new sheet
    workbook.sheets.add("NewSheet")

    # if there is a sheet named "Sales"
    if 'NewSheet' in workbook:
        sheet = workbook['NewSheet']  # get the sheet
        sheet.name = 'NewName'  # change sheet name
        workbook.active = sheet  # set active sheet

    workbook.sheets.add("NewSheet2")  # create a sheet
    workbook.sheets.delete('NewSheet2')  # delete sheet

    workbook.save()
    workbook.close()


def example_read_write_cell():
    # open file datafile.xlsx, return workbook object
    workbook = office.open_file("datafile.xlsx")

    # if there is a worksheet named 'Sales'
    if 'Sales' in workbook:
        sheet = workbook['Sales']  # get the worksheet object

        print('max_row', sheet.max_row)
        print('max_column', sheet.max_column)

        cell = sheet['B3']  # get the 'B2' cell object
        print(cell.value)  # print the value of the cell

        cell = sheet.cell(3, 2)  # get cell at row 2, column 3 (B3)
        print(cell.value)  # print the value of the cell

        cell.value = 'New City'  # Change the value of the cell

    workbook.save()
    workbook.close()


def example_read_write_range():
    # open file datafile.xlsx, return workbook object
    workbook = office.open_file("datafile.xlsx")

    # if there is a worksheet named 'Sales'
    if 'Sales' in workbook:
        sheet = workbook['Sales']  # get the worksheet object
        # read a range value
        range1 = sheet['B2:C4']
        # value of the range is a list, include values of the cells
        print(range1.value)

        # change the values in the range
        sheet['B11:C12'].value = [['Chicago', 18], ['Shanghai', 20]]


def example_read_write_via_workbook():
    # open file datafile.xlsx, return workbook object
    wb = office.open_file("datafile.xlsx")

    # get a sheet by name
    sheet = wb['Sales']  # if sheet not exists, raise exception

    cell = sheet['B3']  # get a cell object
    print(cell.value)  # print the cell value
    print(sheet.cell(3, 2).value)  # get a cell by (row_int, column_int)

    # write the value of the cell
    cell.value = 'Paris'

    # get a cell through workbook, if worksheet 'Sales' not exists, create it.
    print(wb['Sales!B3'].value)
    print(wb['Sales', 'B3'].value)  # by sheet_name, cell address
    print(wb['Sales', 3, 2].value)  # by sheet_name, row_int, column_int

    # write a cell value, if worksheet 'Sales' not exists, create it.
    wb['Sales!B3'].value = "Shanghai"

    print(wb['Sales!B3'].value)

    # read a range value
    range1 = wb['Sales!B2:C4']
    # value of the range is a list, include values of the cells
    print(range1.value)

    # change the values in the range
    wb['Sales!B11:C12'].value = [['Chicago', 18], ['Shanghai', 20]]

    print(wb['Sales!B11:C12'].value)

    wb.save()
    wb.close()


def example_find():
    # open file, get a workbook object
    wb = office.open_file("datafile.xlsx")

    # get a sheet
    sheet = wb["Sales"]

    # find cell value "Sydney", return cell object. return None if not found.
    cell = sheet.find("Sydney")
    if cell is not None:  # if found
        # print info of cell
        print(cell.value, cell.address, cell.row, cell.column)

    # find two value: "Sydney", "Sales Amount"
    # return the cross cell.   return None if not found
    cell = sheet.find("Sydney", "Sales Amount")
    if cell is not None:  # if found
        # print info of cell
        print(cell.value, cell.address, cell.row, cell.column)

    # using workbook object to find
    cell = wb.find("Sales", "Sydney", "Sales Amount")
    if cell is not None:  # if found
        print("Sydney", "Sales Amount", cell.value)


def example_expand():
    # open file, get a workbook object
    wb = office.open_file("datafile.xlsx")

    # get a cell : Sales!A1
    cell = wb["Sales!A1"]

    # expand the cell to a range, result range will be A1:D6
    range1 = cell.expand()
    print(range1)

    # expand the cell to a range, do not expand to the right
    print(cell.expand(right=None))  # A1:A6

    # expand the cell to a range, do not expand downward
    print(cell.expand(down=None))  # A1:D1

    # expand rightward with specified columns count, downward with specified rows count
    print(cell.expand(right=5, down=4))  # A1:F5


def example_range_to_dataframe():
    # open file, get a workbook object
    wb = office.open_file("datafile.xlsx")

    # get a range  Sales!A1:D6
    range1 = wb["Sales", 'A1:D6']
    print(range1)

    # get a list data from the range
    list1 = range1.to_list()
    print(list1)

    # get a DataFrame object from the range
    df = range1.to_dataframe()
    print(df)

    # Write DataFrame to the range
    range1.values = df

    # Write list data to the range
    range1.values = list1

    # wb.save()
    # wb.close()


if __name__ == "__main__":
    # example_basic()
    # example_workbook_worksheet()
    # example_read_write_cell()
    # example_read_write_range()
    # example_read_write_via_workbook()
    # example_expand()
    # example_find()
    # example_expand()
    # example_range_to_dataframe()
    pass
