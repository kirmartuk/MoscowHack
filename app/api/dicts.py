from app.api import bp
from app.models import *
import xlrd

@bp.route("/dicts")
def getDict():
	"""all dicts
    ---
    responses:
        '200':
          description: return all dicts
        """
	with open('dict.json', 'r') as file:
		data = file.read()
	return data
# @bp.route("/adddataset")
# def insertData():
# 	loc = ("/home/kirill/hackaton_res/data_set/dataset_new.xls")
# 	wb = xlrd.open_workbook(loc)
# 	sheet = wb.sheet_by_index(0)
#
#
# 	for row in range(0, sheet.nrows):
# 		print("current >> " + str(row))
# 		#print("shelter >> " + str(sheet.cell_value(row, 41)))
# 		animal_shelter = Shelter.get_id_by_address(sheet.cell_value(row, 41))
# 		#print("id >> " + str(animal_shelter))
# 		#print(animal_shelter)
# 		idcard = sheet.cell_value(row, 1)
# 		#int
# 		animal_type = sheet.cell_value(row, 2)
# 		animal_type = AnimalType.get_id_by_type(animal_type)
# 		#str
# 		animal_age = sheet.cell_value(row, 3)
# 		#int
# 		animal_weight = sheet.cell_value(row, 4)
# 		#str
# 		animal_nickname = sheet.cell_value(row, 5)
# 		#int
# 		animal_male = 0
# 		animal_sex = sheet.cell_value(row, 6)
# 		if animal_sex == "мужской":
# 			animal_male = 1
# 		#int
# 		animal_breed = sheet.cell_value(row, 7)
# 		#print(animal_breed)
# 		animal_breed = AnimalBreed.get_id_by_breed(animal_breed)
# 		#print(animal_breed)
# 		#str
# 		animal_color = sheet.cell_value(row,8)
# 		#str
# 		animal_fur = sheet.cell_value(row,9)
# 		#str
# 		animal_ears = sheet.cell_value(row, 10)
# 		#str
# 		animal_tail = sheet.cell_value(row, 11)
# 		#str
# 		animal_size = sheet.cell_value(row, 12)
# 		#str
# 		animal_special_signs = sheet.cell_value(row, 13)
# 		#int
# 		animal_cell = sheet.cell_value(row, 14)
# 		#str
# 		animal_idmark = sheet.cell_value(row, 15)
# 		#str
# 		animal_sterilized = sheet.cell_value(row, 16)
# 		#str
# 		animal_veterinarian = sheet.cell_value(row, 17)
# 		#int
# 		animal_ready_str = sheet.cell_value(row, 18)
# 		animal_ready = False
#
# 		if animal_ready_str == "да":
# 			animal_ready = True
#
#
#
# 		Animal.add_animal(idcard, animal_age, animal_weight, animal_nickname, animal_male, animal_special_signs, "",animal_type, animal_breed, animal_shelter, animal_color, animal_fur, animal_ears, animal_tail, animal_size, animal_cell, animal_idmark, animal_sterilized, animal_veterinarian, animal_ready)
#
# 	return ""
