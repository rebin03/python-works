class Editor:
    
    def __init__(self, name, vendor):
        self.name = name
        self.vendor = vendor
        
    def open(self):
        print(f"{self.name} open")
        
    def execute(self):
        print(f"{self.name} execute")
        
        
class Vscode(Editor):
    
    def __init__(self, name, vendor):
        super().__init__(name, vendor)
        

class Pycharm(Editor):
    
    def __init__(self, name, vendor):
        super().__init__(name, vendor)
        
        
vsc = Vscode("Visual Studio Code", "Microsoft")
pych = Pycharm("Pycharm", "JetBrains")

vsc.open()
vsc.execute()

pych.open()
pych.execute()