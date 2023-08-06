# this file datafile.py has the same filename to datafile.xlsx (but different extension)
# if xlwings addin is installed, press button "run main" in the Microsoft Excel tab 'xlwings'
# this file will be load, and the function main() will be called by xlwings.
#
import office
import pandas


def main():
    book = office.Excel()  # if xlwings addin called, get the active workbook
    sheet = book.active
    # print(sheet.name)
    # sheet['A12'].value = book.filename
    # sheet['A11'].value = sheet.name
    #
    df = sheet['A1:D6'].to_dataframe()
    sheet['A18'].value = df

    book.save()
    book.close()


if __name__ == "__main__":
    # if run in command line, call main()
    main()
