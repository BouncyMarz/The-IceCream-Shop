import time
import random
from colorama import Fore, Style


msg = 'hello! welcome to your new job.'
msg2 = 'Here, you will learn how to make and serve ice cream!'
print(msg.title())
time.sleep(1.5)
print(msg2.title())
time.sleep(2.5)
msg3 = 'So Let\'s Get Started!'
print(msg3)
time.sleep(2)
msg4 = 'Oh! Here comes a customer.'
print(msg4.title())
time.sleep(1)

i= 1
t = 1
y = 1
money = 0
while i< 100:
    mon = 'money = ' + str(money)
    i +=1
    text = 'Hi'
    text2 = 'Hey'
    welcome = [text,text2]
    ranwel = random.choice(welcome)

    cha1 = '''                                                      ''' + mon + '''
  /\\____/\\   ''' + ranwel + '''                 
=(,,>ヮ<,,)= 
 /  ◠  ◠  \\ '''
    cha2 = '''                                                      ''' + mon + '''
            ''' + ranwel + '''               
𐀪       ''' 

    cha3 = '''                                                      ''' + mon + '''
 ╱|、     ''' + ranwel + '''                      
(˚ˎ 。7  
 |、˜〵          
 じしˍ,)ノ '''

    cha4 = '''                                                      ''' + mon + '''
 /)/)   ''' + ranwel + '''                        
( . .)
(  づ      '''

    cha5 = '''                                                      ''' + mon + '''
         ''' + ranwel + '''              
𖠋𖠋        '''

    cha6 = '''                                                      ''' + mon + '''
⠀⠀⠀⠀⠀⠀⢀⣠⠤⠔⠒⠒⠒⠒⠒⠢⠤⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀''' + ranwel + '''     
⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠦⠀
⠀⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧
⠀⡇⠀⠀⠀⢀⡶⠛⣿⣷⡄⠀⠀⠀⣰⣿⠛⢿⣷⡄⠀⠀⠘⣿⠀
⠀⡇⠀⠀⠀⢸⣷⣶⣿⣿⡇⠀⠀⠀⢻⣿⣶⣿⣿⣿⠀⠀⠀⢸⠀
⠀⡇⠀⠀⠀⠈⠛⠻⠿⠟⠁⠀⠀⠀⠈⠛⠻⠿⠛⠁⠀⠀⠀⢸⠀
⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠁
⠀⠀⠈⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣚⡁⠀⠀
⠀⠀⠀⠀⠈⠙⠒⢢⡤⠤⠤⠤⠤⠤⠖⠒⠒⠋⠉⠉⠈⢙⢨⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹
⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⣤⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⢠⣿⠀⠀⠀⢸⠀⠀⣿⠀⠀⠀⣸
⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⢸⠘⡆⠀⠀⢸⣀⡰⠋⣆⠀⣠⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠤⠤⠼⠀⠘⠤⠴⠃⠀⠀⠀⠈⠉⠁ 
'''


    cha7 = '''                                                      ''' + mon + '''
       ''' + ranwel +'''            
 ૮__‘__ა                                           
૮  • ﻌ • ა
(  ა  ૮ )  '''

    cha8 = '''                                                      ''' + mon + '''
⠀⠀⠀⠀⠀⠀⣀⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''' + ranwel + '''⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠛⠉⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠄⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡘⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⠀⣾⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⡇⠀⠀⠀⢡⠄⠀⠀⣀⣀⣀⣠⠊⠀⠀⠀⠀⡠⠞⠛⠛⠛⠛⠀⠀⠀⠀⠀
⠀⠀⢃⠀⠀⠀⠀⠗⠚⠉⠉⠀⠈⠁⠀⠀⠀⢀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⠲⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠃⠀⠀⢠⣤⡀⠀⠀⠀⠀⣿⣿⣿⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠈⠛⠉⣴⣆⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣇⢰⡧⣉⡉⠀⠀⢀⡀⠀⣀⣀⣠⣿⡷⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⠘⠃⠈⠻⢦⠞⠋⠙⠺⠋⠉⠉⠉⢡⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⢲⡄⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⣀⣤⣴⣶⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⣾⠀⠀⣶⠀⠀⠀⢸⣦⣴⣿⣿⣿⠛⠉⠉⠉⠉⠁⠀
⠀⠀⢀⣀⡰⠏⠀⠀⠀⠀⠉⠀⠈⠋⠀⠀⠀⠘⣿⣿⣿⠛⠋⠀⠀⠀⠀⠀⠀⠀
⠰⣮⣉⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠻⠥⠤⢤⣶⢄⠀⢀⣠⣄⠀⠀⢠⣶⣤⣄⠈⠑⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠈⠋⠁⠠⠁⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
'''

    cha9 = '''                                                      ''' + mon + '''
⢠⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢻⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⡿⠁⠀⠀⠀⠀⠀''' + ranwel + '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠸⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢛⣿⣿⣿⣿⣿⣿⣼⠀⢰⣼⣿⣿⣿⣿⣿⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⠟⠻⠿⣾⡿⠿⠛⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⡏⢹⣶⡄⠀⠀⠀⠀⢴⣾⠛⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣇⠘⠛⠀⢀⣶⣦⠀⠘⠛⢀⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣈⣽⣷⣶⡖⠒⢿⠟⠲⣤⣶⣿⣉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠻⠞⠉⢻⣍⣳⣴⠛⢦⣒⣋⣿⠉⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀    ⢸⠈⠉⠀⠀⠀⠈⠁⣿⠀⢴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀ ⠀⣠⠀⠀⠀⣿⣴⣿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣯⣀⣀⣀⡿⣅⣀⣀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠉⠉⠁⠀⠀'''
    # In honor of Jose
    cha10 = '''                                                     ''' + mon + '''         
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀''' + ranwel + '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠁⠀⠁⠀⠙⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⣴⣾⣿⣷⣦⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠏⠙⠀⠙⠳⢶⣦⣄⣀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⠿⣿⠂⠀⠀⠀⠀⠀⢻⣎⡹⣿⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣷⣀⢘⠀⠀⠀⠀⠀⣰⣿⡾⣿⣿⢿⡿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⠃⢼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⡆⢹⣿⡇⠐⢋⣻⣶⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠻⢷⣶⣼⣿⣍⠻⢿⣿⣿⣿⣿⣿⣿⣿⣠⣿⣧⣶⣾⣿⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣶⣮⣿⣿⢟⣿⣿⣿⣯⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⣀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣯⠞⣼⣹⣿⣿⣿⡿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠻⢶⣦⣄⡀⢀⣰⣿⣿⣿⣷⢛⣦⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠛⠻⠾⢿⣿⣻⣿⣿⣿⣿⣯⡗⣎⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⡇⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠻⠟⠻⢿⣿⣿⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢭⣿⣿⠃⠀⠀⠀⠀⠀⠀⢹⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣷⣤⣴⡀⢻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢤⣄⣀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⡵⢻⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡇⢻⣿⡿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠛⠻⢾⣦⣤⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠂⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⣿⣿⣟⡿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠻⠛⠛⠀⠀⠀⠀⢀⣠⣤⣶⣿⠿⣟⣿⣿⣭⠿⣿⣾⣿⣿⣿⣿⣿⣿⠰⣿⣿⣿⣟⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣤⣴⣾⣿⣿⣿⣷⠾⠿⠟⠛⢿⣿⣿⣾⣱⡿⣿⣿⣿⣿⣿⣿⠈⣿⣿⣿⣿⣞⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⣿⣿⡋⠉⠁⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⣿⠀⠛⢿⣿⣾⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠈⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⡀⠀⠙⢿⣿⣿⣿⣿⡆⢠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣆⡀⢀⢀⣀⣤⣴⣿⣿⣿⣽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣿⣿⣿⣿⣿⣇⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⢻⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣻⣿⣿⣿⣿⣿⣿⠈⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣤⣴⣴⣾⠿⠛⠋⠉⠁⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⣿⣿⣿⡰⣉⠻⢿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡟⣭⣳⣿⣿⣿⣿⣷⣆⡒⡈⠙⠻⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡟⠻⣷⣟⣷⣄⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣟⢣⣿⣿⣿⣿⣿⣭⣿⡟⣿⣿⣷⣤⣀⣸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⢿⣯⣻⣦⡀⠀⠀⠀⠀⠐⠛⢿⣿⣿⡇⢻⣿⣿⣾⣿⣿⣻⣯⡽⣿⣿⣿⣿⡟⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⣻⣿⣄⠀⠀⠀⢀⣀⣠⣿⣿⣟⠸⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣦⣀⣀⣽⣿⠿⠛⢿⣿⣆⣿⣿⣯⠽⣿⣿⣿⣿⣯⣼⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⠘⠋⠁⠀⠀⠀⣻⣿⣿⣿⣧⣻⣿⣿⣏⢳⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⢿⠉⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣋⣾⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣾⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠻⣿⡿⠿⣿⠟⠉⠈⠻⢿⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⡀⠀⠀⠀⠀⠀⠀⠈⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀
'''

    cha11 = '''                                                     ''' + mon + '''                          
                            ▒▒▒▒▒▒▒▒▒▒░░              
                      ▒▒▒▒▒▒▒▒▒▒▒▒░░         ''' + ranwel + '''           
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                      
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                      
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░    ▒▒▒▒▒▒▒▒  
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒  
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒    
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░  ░░▒▒    
          ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░        ░░▒▒    
            ▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒                ░░    
            ▒▒▒▒▒▒          ▒▒▒▒▒▒                      
            ▒▒▒▒▒▒            ▒▒▒▒                      
            ▒▒▒▒                ▒▒                      
            ▒▒    
'''

    chalist = [cha1,cha2,cha3,cha4,cha5,cha6,cha7,cha8,cha9,cha10,cha11]#re-add cha6 & 8
    people = random.choice(chalist)


    Store = people+  '''_________________________________
============================================
____________________________________________
'''

    def choc(text, r, g, b):
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{text}\033[0m")

    def vana(text, r, g, b):
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{text}\033[0m")

    def strab(text, r, g, b):
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{text}\033[0m")

    def waffle(text, r, g, b):
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{text}\033[0m")

    scoop1 = ''' ██████
████████'''

    scoop2= '''
 ██████
████████
 ██████
████████'''
        
    wafflecone = ''' ░░░░░░
  ░░░░
   ░░'''

    filler = ' '

    info= "1 = chocolate, 2 = vanilla, 3 = strawberry"

    info2 = "Press R to return\n"

    kitchen = '''______________________________________________           ''' + mon + '''
 _____          _____          _____
|🟫🟫 |        |⬜⬜ |        |🟥🟥 |
|🟫🟫 |        |⬜⬜ |        |🟥🟥 |
|🟫🟫 |        |⬜⬜ |        |🟥🟥 |
|_____|        |_____|        |_____|
Chocolate      Vanilla       Strawberry   
_______________________________________________\n''' + info + '''
_______________________________________________\n'''

    prompt = ''

    thx = 'Thank you!'

    roast = "GIRLLL YOU STUPID"
    wrong = "Sorry that's not what I ordered."
    error= [wrong]
    randomerror = random.choice(error)
    def incorrect():
        print(Store.replace(ranwel,randomerror))

    prom1 = 'I would like one scoop of chocolate icecream.' 
    prom2 = 'I would like one scoop of vanilla icecream.'
    prom3 = 'I would like one scoop of strawberry icecream.'
    prom4 = 'I would like two scoops of chocolate icecream.'
    prom5 = 'I would like two scoops of vanilla icecream.'
    prom6 = 'I would like two scoops of strawberry icecream.'
    prom7 = 'I would like one scoop of strawberry icecream and one scoop of chocolate icecream.'
    prom8 = 'I would like one scoop of chocolate icecream and one scoop of vanilla icecream.'
    prom9 = 'I would like one scoop of vanilla icecream and one scoop of strawberry icecream.'
    # prom10 = 'I would like three scoop of chocolate icecream.'

    textlist = [prom1,prom2,prom3,prom4,prom5,prom6,prom7,prom8,prom9]
    rantext = random.choice(textlist)
    
    print(Store)
    
    def b():
        time.sleep(1.5)
        print(Store.replace(ranwel,rantext))
        time.sleep(0.5)
        print('\nPress K to enter the Kitchen\n')
    b()

    while t==1:
        kit = input(prompt).lower()
        print('\033[1A' + prompt + '\033[K')
        if kit == 'k' or kit == 'K':
            print(kitchen)
            icecream = input(prompt).lower()
            print('\033[1A' + prompt + '\033[K')
            t+=1 
        else:
            print('\nPress K to enter the kitchen')
    t-=1
    if rantext == prom1 and icecream == '1' or rantext == prom4 and icecream == '1' or rantext == prom8 and icecream == '1':    #chocolate
        choc(scoop1, 138, 98, 69)
        waffle(wafflecone, 191, 145, 105)
        print (kitchen)
        print('\n' + info2)
        mo = int(money)
        money +=1

        while y ==1:
            back = input(prompt).lower()
            print('\033[1A' + prompt + '\033[K')
            if back == 'r' and rantext == prom1 or back == 'R'and rantext == prom1:      #first return
                print(Store.replace(ranwel,thx))
                y+=1
            elif back == '1' and  rantext == prom4:     # double c
                choc(scoop2, 138, 98, 69)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money +=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after c+c 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)
            elif back == '2' and rantext == prom8:  # c+v
                vana(scoop1, 255, 255, 255)    
                choc(scoop1, 138, 98, 69)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money+=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after c+v 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)
            else:
                incorrect()
                money -= 2
                print(y)
                y +=1
                
    elif rantext == prom2 and icecream == '2' or rantext == prom5 and icecream == '2' or rantext == prom9 and icecream == '2':  # vanilla
        vana(scoop1, 255, 255, 255)
        waffle(wafflecone, 191, 145, 105)
        print(kitchen)
        print('\n' + info2)
        mo = int(money)
        money +=1

        while y ==1:
            back = input(prompt).lower()
            print('\033[1A' + prompt + '\033[K')
            if back == 'r' and rantext == prom2 or back == 'R' and rantext == prom2:      #first return
                print(Store.replace(ranwel,thx))
                y+=1
            elif back == '2' and  rantext == prom5:     # double v
                vana(scoop2, 255, 255, 255)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money +=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after double v 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)

            elif back == '3' and rantext == prom9:      # v+s
                strab(scoop1, 237, 140, 180)
                vana(scoop1, 255, 255, 255)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money+=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after v+s 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)
            else:  
                incorrect()
                money -= 2
                y +=1              
    elif rantext == prom3 and icecream == '3' or rantext == prom6 and icecream == '3' or rantext == prom7 and icecream == '3':  # Strawberry
        strab(scoop1, 237, 140, 180)
        waffle(wafflecone, 191, 145, 105)
        print(kitchen)
        print('\n' + info2)
        mo = int(money)
        money +=1

        while y ==1:
            back = input(prompt).lower()
            print('\033[1A' + prompt + '\033[K')
            if back == 'r' and rantext == prom3 or back == 'R' and rantext == prom3:      #first return
                print(Store.replace(ranwel,thx))
                y+=1
            elif back == '3' and  rantext == prom6:     # double s
                strab(scoop2, 237, 140, 180)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money +=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after double v 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)

            elif back == '1' and rantext == prom7:      # s+c
                choc(scoop1, 138, 98, 69)
                strab(scoop1, 237, 140, 180)
                waffle(wafflecone, 191, 145, 105)
                print (kitchen)
                print('\n' + info2)
                money+=1

                while y == 1:
                    back2 = input(prompt).lower()
                    print('\033[1A' + prompt + '\033[K')
                    if back2 == 'r' or back2 == 'R':       # Return after s+c 
                        print(Store.replace(ranwel,thx))
                        y+=1
                    else:
                        print('\n' + info2)
            else:  
                incorrect()
                money -= 2
                y +=1
    else:
        incorrect()
        money -= 1
        y +=1
    y -= 1
    
    people = random.choice(chalist)
    time.sleep(1.5)
