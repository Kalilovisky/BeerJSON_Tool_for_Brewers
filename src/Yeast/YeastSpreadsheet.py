import xlrd
import json
import os

from src.Yeast.YeastStrain import YeastStrain

class YeastSpreadsheet:
    def __init__(self, filename):
        self.filename = filename
        self.yeast_strains = []

    def read_spreadsheet(self):
        workbook = xlrd.open_workbook(self.filename)
        sheet = workbook.sheet_by_index(0)

        for i in range(1, sheet.nrows):
            name = sheet.cell_value(i, 0)
            beer_type = sheet.cell_value(i, 1)
            form = sheet.cell_value(i, 2)
            laboratory = sheet.cell_value(i, 3)
            product_id = sheet.cell_value(i, 4)
            min_temp = sheet.cell_value(i, 5)
            max_temp = sheet.cell_value(i, 6)
            attenuation = sheet.cell_value(i, 7)
            flocculation = sheet.cell_value(i, 8)
            

            yeast_strain = YeastStrain(name, beer_type, form, laboratory, product_id, min_temp, max_temp, attenuation, flocculation)
            self.yeast_strains.append(yeast_strain)
        
        return self.yeast_strains

    def to_json(self, yeast_list):
        yeast_strain_list = [yeast_strain.to_json() for yeast_strain in yeast_list]
        return {"yeast_strains": yeast_strain_list}
        
    def save_to_json(self, filename, yeast_list):       
        data = self.to_json(yeast_list)
        with open(filename, "w") as f:
            json.dump(data, f)