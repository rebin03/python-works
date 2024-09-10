from abc import ABC, abstractmethod

class Editor(ABC):
    
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def debug(self):
        pass
    
class Vscode(Editor):
    
    def open(self):
        print("Vscode open method")
    
    def execute(self):
        print("Vscode execute method")
    
    def debug(self):
        print("Vscode debug method")
        
vs = Vscode()
vs.open()
vs.execute()
        
