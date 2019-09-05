from gpiozero import LED, Button, LEDBoard, ButtonBoard
from guizero import App, Waffle, Text,Box, PushButton, Combo, Window, CheckBox

mode = 'unset'
mode_old = 'unset'
GPIO_pins = [2,3,4,14,15,17,18,27,22,23,24,10,9,11,25,8,7,5,6,12,13,19,16,26,20,21]

def pressed():
    global p_in
    global buttons
    print('pressed')
    #print(p_in.value)
    i = 0
    for p in p_in.value:

        if p == 1:
            print(i)
            if buttons[i].bg == 'white':
                buttons[i].bg = 'green'
            elif buttons[i].bg == 'grey':
                buttons[i].bg = 'grey'
            else:
                buttons[i].bg = 'white'
        i+=1
            
  
def released():
    print('released')
    global p_in
    global buttons
    #print(p_in.value)
    i = 0
    for p in p_in.value:
        if p == 0:
           buttons[i].bg = 'green'
        i+=1
    
def inoroutchoice(selected_value):
    print('choice')
    global mode
    global mode_old
    global p_out
    global p_in
    if selected_value == "Input":
        mode = 'input'
        if mode_old == 'output':
            p_out.close()
        elif mode_old == 'input':
            p_in.close()
        mode_old = 'input'
        #p_out.close()
        if pullup.value == 0:
            p_in = ButtonBoard(2,3,4,14,15,17,18,27,22,23,24,10,9,11,25,8,7,5,6,12,13,19,16,26,20,21)
        else:
            p_in = ButtonBoard(4,14,15,17,18,27,22,23,24,10,9,11,25,8,7,5,6,12,13,19,16,26,20,21,pull_up=False)
            buttons[1].disable()
            buttons[1].bg = 'light grey'
            buttons[0].disable()
            buttons[0].bg = 'light grey'
        #p_in = ButtonBoard(b2=2,b3=3,b20=20)
        p_in.when_pressed = pressed
        #p_in.when_released = released
        i=0
        floaters = []
        for p in p_in.value:
            #print(p)
            if p == 1:
                floaters.append(i)
                print(i)
                if buttons[i].bg == 'grey':
                    buttons[i].bg = 'green'
                else:
                    buttons[i].bg = 'grey'
            i+=1
        if len(floaters) > 0:
            app.warn("Possible floaters!", "Found " + str(len(floaters)) + " pins that may be floating high")
    elif selected_value == 'Output':
        mode = 'output'
        if mode_old == 'input':
            p_in.close()
        elif mode_old == 'output':
            p_out.close()
        mode_old = 'output'
        
        #p_in.close()
        p_out = LEDBoard(2,3,4,14,15,17,18,27,22,23,24,10,9,25,11,8,7,5,6,12,13,19,16,26,20,21)
        p_out.off()
        for b in buttons:

            if b.bg == 'grey':
                b.bg = 'green'

def clicked(pin_index):
    global mode

    global p_out
    global p_in
    print('clicked')
    if mode == 'output':
        print(pin_index)
        p_out.toggle(pin_index)
        if buttons[pin_index].bg == 'white':
            buttons[pin_index].bg = 'green'
        else:
            buttons[pin_index].bg = 'white'
    if mode == 'input':
        print(pin_index)
        #warn = Window(app)
        app.warn("hey!","Clicking on a button doesn't do anything in Input mode. Switch to output mode to change the state of a pin")

        
app = App(layout='grid',height=920, width = 300)
label = Text(app, "Select a mode of operation:", grid=[0,0,2,1])
inorout = Combo(app,options=["Unset", "Input","Output"],grid=[0,1,2,1],command=inoroutchoice)
pullup = CheckBox(app,grid=[2,1,2,1],text="pull-down")
#waffle = Waffle(app, command=pin_clicked, height=20, width=2, grid=[1,0,1,20],align='top')
b1 = PushButton(app, grid=[0,2],align='top',text="3v3",width=6,height=1)
b1.bg = 'yellow'
b2 = PushButton(app, grid=[1,2],align='top',text="5v",width=6,height=1)
b2.bg = 'red'


b3 = PushButton(app, grid=[0,3],align='top',text="GPIO2",width=6,height=1, command = clicked, args=[0])
b3.bg = 'green'
b4 = PushButton(app, grid=[1,3],align='top',text="5v",width=6,height=1)
b4.bg = 'red'



b5 = PushButton(app, grid=[0,4],align='top',text="GPIO3",width=6,height=1, command = clicked, args=[1])
b5.bg = 'green'
b6 = PushButton(app, grid=[1,4],align='top',text="GND",width=6,height=1)
b6.bg = 'black'
b6.text_color='white'


b7 = PushButton(app, grid=[0,5],align='top',text="GPIO4",width=6,height=1, command = clicked, args=[2])
b7.bg = 'green'
b8 = PushButton(app, grid=[1,5],align='top',text="GPIO14",width=6,height=1, command = clicked, args=[3])
b8.bg = 'green'

b9 = PushButton(app, grid=[0,6],align='top',text="GND",width=6,height=1)
b9.bg = 'black'
b9.text_color='white'
b10 = PushButton(app, grid=[1,6],align='top',text="GPIO15",width=6,height=1, command = clicked, args=[4])
b10.bg = 'green'


b11 = PushButton(app, grid=[0,7],align='top',text="GPIO17",width=6,height=1, command = clicked, args=[5])
b11.bg = 'green'
b12 = PushButton(app, grid=[1,7],align='top',text="GPIO18",width=6,height=1, command = clicked, args=[6])
b12.bg = 'green'

b13 = PushButton(app, grid=[0,8],align='top',text="GPIO27",width=6,height=1, command = clicked, args=[7])
b13.bg = 'green'
b14 = PushButton(app, grid=[1,8],align='top',text="GND",width=6,height=1)
b14.bg = 'black'
b14.text_color='white'


b15 = PushButton(app, grid=[0,9],align='top',text="GPIO22",width=6,height=1, command = clicked, args=[8])
b15.bg = 'green'
b16 = PushButton(app, grid=[1,9],align='top',text="GPIO23",width=6,height=1, command = clicked, args=[9])
b16.bg = 'green'

b17 = PushButton(app, grid=[0,10],align='top',text="3v3",width=6,height=1)
b17.bg = 'yellow'
b18 = PushButton(app, grid=[1,10],align='top',text="GPIO24",width=6,height=1, command = clicked, args=[10])
b18.bg = 'green'

b19 = PushButton(app, grid=[0,11],align='top',text="GPIO10",width=6,height=1, command = clicked, args=[11])
b19.bg = 'green'
b20 = PushButton(app, grid=[1,11],align='top',text="GND",width=6,height=1)
b20.bg = 'black'
b20.text_color='white'

b21 = PushButton(app, grid=[0,12],align='top',text="GPIO9",width=6,height=1, command = clicked, args=[12])
b21.bg = 'green'
b22 = PushButton(app, grid=[1,12],align='top',text="GPIO25",width=6,height=1, command = clicked, args=[13])
b22.bg = 'green'

b23 = PushButton(app, grid=[0,13],align='top',text="GPIO11",width=6,height=1, command = clicked, args=[14])
b23.bg = 'green'
b24 = PushButton(app, grid=[1,13],align='top',text="GPIO8",width=6,height=1, command = clicked, args=[15])
b24.bg = 'green'

b25 = PushButton(app, grid=[0,14],align='top',text="GND",width=6,height=1)
b25.bg = 'black'
b25.text_color='white'
b26 = PushButton(app, grid=[1,14],align='top',text="GPIO7",width=6,height=1, command = clicked, args=[16])
b26.bg = 'green'

b27 = PushButton(app, grid=[0,15],align='top',text="RES",width=6,height=1)
b27.bg = 'blue'
b28 = PushButton(app, grid=[1,15],align='top',text="RES",width=6,height=1)
b28.bg = 'blue'

b29 = PushButton(app, grid=[0,16],align='top',text="GPIO5",width=6,height=1, command = clicked, args=[17])
b29.bg = 'green'
b30 = PushButton(app, grid=[1,16],align='top',text="GND",width=6,height=1)
b30.bg = 'black'
b30.text_color='white'

b31 = PushButton(app, grid=[0,17],align='top',text="GPIO6",width=6,height=1, command = clicked, args=[18])
b31.bg = 'green'
b32 = PushButton(app, grid=[1,17],align='top',text="GPIO12",width=6,height=1, command = clicked, args=[19])
b32.bg = 'green'

b33 = PushButton(app, grid=[0,18],align='top',text="GPIO13",width=6,height=1, command = clicked, args=[20])
b33.bg = 'green'
b34 = PushButton(app, grid=[1,18],align='top',text="GND",width=6,height=1)
b34.bg = 'black'
b34.text_color='white'

b35 = PushButton(app, grid=[0,19],align='top',text="GPIO19",width=6,height=1, command = clicked, args=[21])
b35.bg = 'green'
b36 = PushButton(app, grid=[1,19],align='top',text="GPIO16",width=6,height=1, command = clicked, args=[22])
b36.bg = 'green'

b37 = PushButton(app, grid=[0,20],align='top',text="GPIO26",width=6,height=1, command = clicked, args=[23])
b37.bg = 'green'
b38 = PushButton(app, grid=[1,20],align='top',text="GPIO20",width=6,height=1, command = clicked, args=[24])
b38.bg = 'green'

b39 = PushButton(app, grid=[0,21],align='top',text="GND",width=6,height=1)
b39.bg = 'black'
b39.text_color='white'
b40 = PushButton(app, grid=[1,21],align='top',text="GPIO21",width=6,height=1, command = clicked, args=[25])
b40.bg = 'green'
#buttons = [b2,b3,b4,b14,b15,b17,b18,b27,b22,b23,b24,b10,b9,b11,b25,b8,b7,b5,b6,b12,b13,b19,b16,b26,b20,b21]
buttons = [b3,b5,b7,b8,b10,b11,b12,b13,b15,b16,b18,b19,b21,b22,b23,b24,b26,b29,b31,b32,b33,b35,b36,b37,b38,b40]

app.display()



