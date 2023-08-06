from os import listdir
from os.path import isdir


symbol_right= '─'
symbol_mix = '├'
symbol_end = '└'


class PrettyTree():

    def __init__(self, filepath):
        self.sticks = 0
        self.text = ''
        self.filepath = filepath

    def draw(self) -> str:
        try:
            output = ''
            response = self.checkinside(self.filepath).split('\n')
            for i in response[:-1]:
                if i[2] == symbol_right: add_s = symbol_mix
                else: add_s = ''
                output+=f'{add_s}{i[2:]}\n'

            roundness = output.split('\n')[:-1]
            for x in range(len(roundness)):
                try:
                    if roundness[x][0] != roundness[x+1][0] and roundness[x][0] == symbol_mix:
                        roundness[x] = roundness[x].replace(symbol_mix, symbol_end)
                except IndexError:
                    if roundness[x][0] == symbol_mix:
                        roundness[x] = roundness[x].replace(symbol_mix, symbol_end)
            output = ''
            for _ in roundness:
                output+=f'{_}\n'
            return output
        except FileNotFoundError as e:
            print(e)

    def checkinside(self, request, sticks: int = 0) -> str:
        for x in listdir(request):
            if isdir(fr'{request}\{x}'): sym = '📁'
            else: sym = '' # Maybe later will be added some more icons

            self.text+=f'{symbol_mix}{symbol_right*sticks} {sym}'+fr'{request}\{x}'[fr'{request}\{x}'.rfind('\\')+1:]+'\n'

            if sticks == 0: self.sticks = 0
            if isdir(fr'{request}\{x}'):
                self.sticks+=2
                self.checkinside(fr'{request}\{x}', self.sticks)
        return self.text
