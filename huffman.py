from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re

Tk().withdraw()
filename = askopenfilename()
#print(filename)

states = []
finalstates = []
startstate = ""
alphabet = []
totaltrans = 0
transitions = []

try:
    with open(filename,"r",encoding='utf8') as f:
        for line in f:
            line = line.strip('\n')
            if not (line.startswith('#') or line[:2] == '//'):
                if '//' in line:
                    line = line[:line.index('//')]
                if 'finalStates{' in line:
                    finalstates = re.split(' *, *', line[line.index('{')+1:line.index('}')])
                elif 'startState{' in line:
                    startstate = line[line.index('{')+1:line.index('}')]
                elif 'states{' in line:
                    states = re.split(' *, *', line[line.index('{')+1:line.index('}')])
                elif 'alphabet{' in line:
                    alphabet = re.split(' *, *', line[line.index('{')+1:line.index('}')])
                elif 'totalTrans=' in line:
                    totaltrans = line[line.index('=')+1:]
                else:
                    transitions.append(re.split(' *, *', line))
                    
except IOError:
    print("File could not be opened.")

