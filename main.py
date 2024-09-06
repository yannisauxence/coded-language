# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
from datetime import datetime
import teradatasql
from datetime import datetime
pd.options.display.max_columns = None

u_name = 
pw = 
server_name = 

now = (datetime.now().strftime('%Y_%m_%d %H_%M_%S'))

#     return df
def create_DF_from_SQL(query, username=u_name, password=pw, server=server_name):
    with teradatasql.connect(host=server_name, user=username, password=password) as connect:
        df = pd.read_sql(query, connect)
    return df


def export_into_XLSX(dataframe, Sheetname, Output):
    with pd.ExcelWriter(Output) as writer:
        dataframe.to_excel(writer, sheet_name=Sheetname, index=False)
# class DB:
#
#     def __init__(self, id):
#         self.id = str(id)
#
#     def enter(self):
#         self.brand = input("Enter your car's brand: ")
#         self.location = input("Enter your car's location: ")
#         self.owner = input("Enter your car's owner: ")
#
#     def display(self):
#         print("Your car's id is " + self.id)
#         print("Your car's brand is " + self.brand)
#         print("Your car's location is " + self.location)
#         print("Your car's owner is " + self.owner)
#
#
# i = 0
# list = []
# q = 0
# w = input("Enter your car's ID (Press q to quit): ")
# while w != 'q':
#     obj = DB(w)
#     obj.enter()
#     objlist = [obj.id, obj.brand, obj.location, obj.owner]
#     list.append(objlist)
#     i += 1
#     q = i
#     w = input("Enter your car's ID:(Press q to quit) ")
#
# listb = []
# listc = []
# for i in range(q):
#     listb.append(list[i][1])
#     listc.append(list[i][2])
#     print(list[i])
#
# #for i in range(q):
# xpoints = np.array(listb)
# ypoints = np.array(listc)
# plt.plot(xpoints, ypoints, 'o')
# plt.show()
