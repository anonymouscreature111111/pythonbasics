from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    
    def make_sound(self):
        pass



class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar")

    def make_sound(self):
        print("Guitar goes: Strum strum!")


class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano")

    def make_sound(self):
        print("Piano goes: Plink plonk!")


class Drum(Instrument):
    def __init__(self):
        super().__init__("Drum")

    def make_sound(self):
        print("Drum goes: Boom boom!")



instruments = [Guitar(), Piano(), Drum()]

print("=== Music Instrument Sound Show ===")
for inst in instruments:
    print(f"{inst.name} is playing...")
    inst.make_sound()
