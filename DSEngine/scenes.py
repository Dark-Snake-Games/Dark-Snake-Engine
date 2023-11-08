
SCN = "main"

def resetwindow():
    global window
    window.layers = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], "GUI": []}
    
def fakescene(keys):
    pass

class scene:
    def __init__(self, scene, init, stop = resetwindow) -> None:
        self.init, self.scene, self.stop = init, scene, stop
scenes={"main":scene(fakescene,fakescene)}
def changescene(scn: str):
    global SCN,scenes
    scenes[SCN].stop()
    SCN = scn
    scenes[SCN].init()

def runscene(keys):
    print(SCN,scenes)
    scenes[SCN].scene(keys)

def setscenes(dict):
    global scenes
    scenes=dict

def addscene(name,scene:scene):
    global scenes
    scenes[name]=scene
    
def setmainwindow(win):
    global window
    window=win