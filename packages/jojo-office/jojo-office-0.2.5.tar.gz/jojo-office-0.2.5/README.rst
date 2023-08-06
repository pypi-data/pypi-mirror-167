office module 0.2.0 documentation

Author: JoStudio, Date: 2022/9/1

office Module
======================

Process .docx, .xlsx, .pptx, .pdf files for office automation






office.excel submodule
-----------------------------------------------

Excel : process the data in .xlsx file



Example:

::

    import office



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












office.ppt submodule
-----------------------------------------------

PPT : auto creation of the .pptx file



Example:

::

    import office



    # create file output.pptx using template1.pptx

    ppt = office.open_file("output.pptx", template="template1.pptx")



    # create ppt content by fill the data from Excel file datafile.xlsx, and save.

    ppt.fill('datafile.xlsx').save()



    # save pptx to pdf with watermark (works on Windows with Microsoft PowerPoint)

    ppt.save('final.pdf', watermark="CONFIDENTIAL")



    # save pptx slides into a long image, with watermark (works on Windows with Microsoft PowerPoint)

    ppt.save('long.jpg', watermark="CONFIDENTIAL")



    # play ppt (works on Windows with Microsoft PowerPoint)

    ppt.play()











office.word submodule
-----------------------------------------------

Word : auto creation of the .docx file



Example:

::

    import office



    # create file output.docx using template1.docx

    doc = office.open_file("output.docx", template="template1.docx")



    # create document content by fill the data from Excel file datafile.xlsx, and save.

    doc.fill('datafile.xlsx').save()



    # save to pdf with watermark (works on Windows with Microsoft PowerPoint)

    doc.save('final.pdf', watermark="CONFIDENTIAL")








