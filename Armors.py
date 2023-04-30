class Armor(object):
    def __init__(self):
        self.name = 'None'
        self.ac = 10
        self.max_dex = 10
        self.min_str = 0
        self.disadvantage = False


class Padded(Armor):
    def __init__(self):
        self.name = 'Padded'
        self.ac = 11
        self.disadvantage = True
        

class Leather(Armor):
    def __init__(self):
        self.name = 'Leather'
        self.ac = 11
        

class StuddedLeather(Armor):
    def __init__(self):
        self.name = 'Studded Leather'
        self.ac = 12
        

class Hide(Armor):
    def __init__(self):
        self.name = 'Hide'
        self.ac = 12
        self.max_dex = 2
        

class ChainShirt(Armor):
    def __init__(self):
        self.name = 'Chain Shirt'
        self.ac = 13
        self.max_dex = 2
        

class ScaleMail(Armor):
    def __init__(self):
        self.name = 'Scale Mail'
        self.ac = 14
        self.max_dex = 2
        self.disadvantage = True
        

class Breastplate(Armor):
    def __init__(self):
        self.name = 'Breast Plate'
        self.ac = 14
        self.max_dex = 2
        

class HalfPlate(Armor):
    def __init__(self):
        self.name = 'Half Plate'
        self.ac = 15
        self.max_dex = 2
        self.disadvantage = True
        

class RingMail(Armor):
    def __init__(self):
        self.name = 'Half Plate'
        self.ac = 14
        self.max_dex = 0
        self.disadvantage = True
        

class ChainMail(Armor):
    def __init__(self):
        self.name = 'Chain Mail'
        self.ac = 16
        self.max_dex = 0
        self.disadvantage = True
        self.min_str = 13
        

class Splint(Armor):
    def __init__(self):
        self.name = 'Splint'
        self.ac = 17
        self.max_dex = 0
        self.disadvantage = True
        self.min_str = 15
        

class Plate(Armor):
    def __init__(self):
        self.name = 'Plate'
        self.ac = 18
        self.max_dex = 0
        self.disadvantage = True
        self.min_str = 15
        

class Shield(Armor):
    def __init__(self):
        self.name = 'Shield'
        self.ac = 2 


class Armors(object):
    def __init__(self):
        self.armors = {
            'Padded': Padded(),
            'Leather': Leather(),
            'Studded Leather': StuddedLeather(),
            'Hide': Hide(),
            'Chain Shirt': ChainShirt(),
            'Scale Mail': ScaleMail(),
            'Breastplate': Breastplate(),
            'Half Plate': HalfPlate(),
            'Ring Mail': RingMail(),
            'Chain Mail': ChainMail(),
            'Split': Splint(),
            'Plate': Plate(),
            'Shield': Shield(),
        }

    def get(self, name):
        if name in self.armors:
            return self.armors[name]
        else:
            return None


    def is_armor(self, name):
        return name in self.armors.keys()
