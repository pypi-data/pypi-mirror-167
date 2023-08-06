import office

try:
    import pandas as pd
except ImportError:
    pd = None


def example_fill_excel_data():
    # create file output.pptx using template1.pptx
    ppt = office.open_file("output.pptx", template="template1.pptx")

    # fill into the ppt with the data from Excel file datafile.xlsx, and save.
    ppt.fill('datafile.xlsx').save()


def example_fill_table():
    # create file output.pptx using template2.pptx
    # fill into the ppt with the data from Excel file datafile.xlsx, and save.
    office.open_file("output.pptx", "template2.pptx").fill('datafile.xlsx').save()


def example_fill_chart():
    # create file output.pptx using template3.pptx
    # fill into the ppt with the data from Excel file datafile.xlsx, and save.
    office.open_file("output.pptx", "template3.pptx").fill('datafile.xlsx').save()


def example_insert_photo():
    # create file output.pptx using template4.pptx
    # fill into the ppt with the data from Excel file datafile.xlsx, and save.
    office.open_file("output.pptx", "template4.pptx").fill('datafile.xlsx').save()


def example_report():
    # create file output.pptx using template5.pptx
    # fill into the ppt with the data from Excel file datafile.xlsx, and save.
    office.open_file("report.pptx", "template5.pptx").fill('datafile.xlsx').save()


def example_long_image():
    # open report.pptx, save it as a long image(save file is a .jpg file means save long imag)
    # add watermark when save
    office.open_file("report.pptx").save("long.jpg", watermark="CONFIDENTIAL")


def example_save_pdf():
    # save as .pdf file, add watermark
    office.open_file("report.pptx").save('report.pdf', watermark="商业秘密，注意保管")


def example_play_ppt():
    # play powerpoint file with timing parameters
    office.open_file("report.pptx").play([1, 3, 3, 1])


def example_play_ppt_with_voice():
    # play powerpoint file with timing parameters, play voice files
    office.open_file("report.pptx").play([
        1,
        [3, "1.wav"],
        3,
        [1, "2.wav"]
    ])


def example_play_ppt_with_file():
    # play powerpoint file with definitions in file  play.txt
    office.open_file("report.pptx").play("play.txt")


def example_fill_dictionay():
    data = {
        "Name": "Peter",
        "Age": 18,
        "Photo": "peter.jpg",
        'Study': {
            'Lesson': ['Literature', 'Math', 'English'],
            'Score': [95.3, 68, 75],
            'Evaluate': ['Good', 'Bad', 'Medium']
        }
    }

    # create file output.pptx using template5.pptx
    # fill into the ppt with the data from dictionary, and save.
    office.open_file("report.pptx", "template6.pptx").fill(data).save()


def example_fill_dataframe():
    data = {
            'Lesson': ['Literature', 'Math', 'English'],
            'Score': [95.3, 68, 75],
            'Evaluate': ['Good', 'Bad', 'Medium']
    }

    df = pd.DataFrame(data)

    # create file output.pptx using template8.pptx
    # fill into the ppt with the data from dictionary, and save.
    office.open_file("report.pptx", "template7.pptx").fill(df).save()


def example_multi_fill():
    person = {"Name": "Peter", "Age": 18, "Photo": "peter.jpg"}

    # create file output.pptx using template8.pptx
    # fill data from file datafile.xlsx, then fill data from person dict
    office.open_file("report.pptx", "template8.pptx").fill('datafile.xlsx').fill(person).save()


def example_duplicate_slide():
    # create file output.pptx using template9.pptx,  fill data from file datafile.xlsx
    office.open_file("report.pptx", "template9.pptx").fill("datafile.xlsx").save()


if __name__ == "__main__":
    example_fill_excel_data()
    # example_fill_table()
    # example_fill_chart()
    # example_insert_photo()
    # example_report()
    # example_long_image()
    # example_save_pdf()
    # example_play_ppt()
    # example_play_ppt_with_voice()
    # example_play_ppt_with_file()
    # example_fill_dictionay()
    # example_fill_dataframe()
    # example_multi_fill()
    # example_duplicate_slide()



