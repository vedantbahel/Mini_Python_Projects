from guietta import _, Gui, Quit

gui = Gui (
    ["Enter the type of vehicle (c for car, b for bus, s for scooter): ",    '__c__'],
    ["Enter time in hour (please enter in 24 hours format): ", '__enteringHour__'],
    ["Enter time in minutes: ",                            '__enteringMinutes__'],
    ["Leaving time in hours (please enter in 24 hours format): ",  '__leavingHour__'],
    ["Leaving time in minutes: ",                               '__leavingMinutes__'],
    
    ["-----------------------Parking slip------------------------",                _],
    [                       ['Generate'],               Quit                        ],
    ["Total no. of hours in parking: ",                             '__totalHours__'],
    ["Total charge: ",                                                   '__total__']
)

def calculate_charge(gui):
    hour = int(gui.leavingHour) - int(gui.enteringHour)
    if(int(gui.leavingMinutes) < int(gui.enteringMinutes)):
            hour -=1
    gui.totalHours = hour

    if(gui.c == 'c'):
        if (hour < 4):
            gui.total = 10
        else:
            gui.total = 20
    
    elif(gui.c == 'b'):
        if (hour < 4):
            gui.total = 20
        else:
            gui.total = 30

    elif(gui.c == 's'):
        if (hour < 4):
            gui.total = 5
        else:
            gui.total = 10

gui.Generate = calculate_charge

gui.run()
