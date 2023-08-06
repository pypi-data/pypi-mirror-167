import os
import json
import xlsxwriter


def flatten_json(y:dict) -> list:
    '''Function expexts a dictionary i.e. JSON and will return
       list of paths.
    '''
    out = []
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out.append(name[:-1])
    flatten(y)
    return out



def get_path(directory:str=None) -> list:
    '''
    This function will take standard JSON as input and will return
    all the path present in that JSON.
    parameters:-
    directory: string
    '''
    if directory is None:
        return "Please provide either file_name or directory"
    else:
        files = os.listdir(directory)
        for file_name in files:
            with open(f"{directory}\{file_name}","rb") as f:
                data = json.load(f)
                row = 0
                column = 0
                workbook = xlsxwriter.Workbook(f'{file_name}.xlsx')
                worksheet = workbook.add_worksheet()
                paths = flatten_json(data)
                for element in paths:
                    worksheet.write(row, column, element)
                    row += 1
                workbook.close()
            f.close()
    print("success")
    return "Success"

        


