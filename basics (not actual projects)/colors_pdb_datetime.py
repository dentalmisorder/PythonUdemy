from datetime import datetime
import colorama 
import pdb #python debuger

colorama.init(autoreset=True)

#============DATETIME=================

today = datetime.today() #same
print(today)

curr_time = datetime.now() #as this
print(curr_time)

print(today.ctime()) #but this format is better and we can get rid of microseconds tho xd

#======================================

#===========COLORAMA===================

def draw_box_fields(func):
    def wrap_up(text):

        print('====================================')
        print(f'{colorama.Fore.YELLOW} {text}')
        print('====================================')

    return wrap_up

@draw_box_fields
def hewwo(text):
    pass

hewwo('hewwo guys! uwu c:')

#======================================

#========PYTHON DEBUGER================

#if u have an error somewhere u can call pdb.set_trace() 
#before an error and play with variables to check what is wrong
# NOTE: type q to quit pdb

y = 5
z = 0

pdb.set_trace()

x = y / z

#=======================================

colorama.deinit()