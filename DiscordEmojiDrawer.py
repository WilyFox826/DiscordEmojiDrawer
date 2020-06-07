import PySimpleGUI as sg

#Adding an emoji to draw
clown = ':clown:'
wolf = ':wolf:'
fox = ':fox:'
poop = ':poop:'
fish = ':fish:'
#Current emoji
emoji = clown

#Creating window layout
sg.theme('DarkAmber')
layout = [
    #0                #1               #2               #3               #4               #5               #6               #7               #8               #9               #10              #11              #12              #13              #14              #15              #16              #17              #18   
    [sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox('')],
    #19               #20              #21              #22              #23              #24              #25              #26              #27              #28              #29              #30              #31              #32              #33              #34              #35              #36              #37
    [sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox('')],
    #38               #39              #40              #41              #42              #43              #44              #45              #46              #47              #48               #49              #50              #51              #52             #53              #54              #55              #56
    [sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox('')],
    #57               #58              #59              #60              #61              #62              #63              #64              #65              #66              #67              #68              #69              #70              #71              #72              #73              #74              #75
    [sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox('')],
    #76               #77              #78              #79              #80              #81              #82              #83              #84              #85              #86              #87              #88              #89              #90              #91              #92              #93              #94
    [sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox(''), sg.Checkbox('')],
    [sg.OptionMenu(values=('Clown', 'Wolf', 'Fox', 'Poop', 'Fish'), size=(87, 20))],
    [sg.Button('Draw', size=(39, 1), button_color=('#474747', '#f5f5f5')), sg.Cancel('Выйти', size=(39, 1), button_color=('#474747', '#f5f5f5'))],
    [sg.Output(size=(90, 20), background_color='#474747', text_color='#f5f5f5')],
    [sg.Text('Created by WilyFox', font=('SansSerif'), text_color=('#f5f5f5'))]

]

#Creating window
window = sg.Window('Discord Emoji Drawer', layout)

#Listening for events in window
while True:
    event, values = window.read()
    if event in (None, 'Выйти'):
        break

    #Changin emoji to draw
    if values[95] == 'Clown':
        emoji = clown
    elif values[95] == 'Wolf':
        emoji = wolf
    elif values[95] == 'Fox':
        emoji = fox
    elif values[95] == 'Poop':
        emoji = poop
    elif values[95] == 'Fish':
        emoji = fish


    if event == 'Draw':
        #Clear array
        a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0

        #Cycle for creating the picture
        for i in range (95):
            if values[i] == True:
                a[i] = emoji
            elif values[i] == False:
                a[i] = '      '

        #Drawing the picture
        print(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18])
        print(a[19]+a[20]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]+a[30]+a[31]+a[32]+a[33]+a[34]+a[35]+a[36]+a[37])
        print(a[38]+a[39]+a[40]+a[41]+a[42]+a[43]+a[44]+a[45]+a[46]+a[47]+a[48]+a[49]+a[50]+a[51]+a[52]+a[53]+a[54]+a[55]+a[56])
        print(a[57]+a[58]+a[59]+a[60]+a[61]+a[62]+a[63]+a[64]+a[65]+a[66]+a[67]+a[68]+a[69]+a[70]+a[71]+a[72]+a[73]+a[74]+a[75])
        print(a[76]+a[77]+a[78]+a[79]+a[80]+a[81]+a[82]+a[83]+a[84]+a[85]+a[86]+a[87]+a[88]+a[89]+a[90]+a[91]+a[92]+a[93]+a[94])
