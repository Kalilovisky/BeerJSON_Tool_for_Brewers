import os
import glob

from src.Yeast.YeastSpreadsheet import YeastSpreadsheet

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    my_files = glob.glob('src/Yeast/*.xls')
    yeast_list = []

    for file in my_files:
        yeast_spreadsheet = YeastSpreadsheet(file)
        yeast_list += yeast_spreadsheet.read_spreadsheet()

    yeast_spreadsheet.save_to_json("yeast.json", yeast_list)

if __name__ == "__main__":
    main()
