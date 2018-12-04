import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)))))
from setting import *

def get_word_json(select):
    scope = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("%sconfiguration/messfar-3cb0e128881a.json" %(FileRoute), scope)
    gc = gspread.authorize(credentials)
    sh = gc.open("Ahfargo_say_data")
    worksheet = sh.worksheet(select)
    say_count = worksheet.range('B1')
    say_count = re.search('\d+',say_count[0].value).group()
    say_count = str(int(say_count)+1)
    cell_list = worksheet.range('A2:A%s' %(say_count))
    return [item.value for item in cell_list]
def get_default_json():
    ret = list()
    scope = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("%sconfiguration/messfar-3cb0e128881a.json" %(FileRoute), scope)
    gc = gspread.authorize(credentials)
    sh = gc.open("Ahfargo_say_data")
    worksheet = sh.worksheet("default")
    cell_list = worksheet.range('A1:A1000')
    cell_list = [item.value for item in cell_list if item.value != '']
    for index, item in enumerate(cell_list):
        row_list = worksheet.range('B%s:Z%s' %(index+1,index+1))
        row_list = [item.value for item in row_list if item.value != '']
        ret.append({"word": item, "schema": row_list})
    print(ret)
    return ret
select = ["bus_num", "route_plan", "fun_place", "nearby_bus", "nearby_bike"]
json_data = dict()
for item in select:
    print(get_word_json(item))
    json_data[item] = get_word_json(item)
json_data['default'] = get_default_json()
with open('%sres/get_word.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)
