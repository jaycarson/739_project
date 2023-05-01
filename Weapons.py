class Weapon(object):
    def __init__(self):
        self.name = 'None'
        self.damage = '1d4'
        self.damage_versatile = '1d6'
        self.versatile = False
        self.light = False
        self.finesse = False
        self.range = 0
        self.max_range = 0
        self.two_handed = False
        self.heavy = False
        self.reach = False

    def update(self):
        return


class Club(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Club'
        self.damage = '1d4'
        self.light = True


class Dagger(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Dagger'
        self.damage = '1d4'
        self.light = True
        self.finesse = True
        self.range = 20
        self.max_range = 60


class Greatclub(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Greatclub'
        self.damage = '1d8'
        self.two_handed = True


class Handaxe(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Handaxe'
        self.damage = '1d6'
        self.light = True
        self.range = 20
        self.max_range = 60


class Javelin(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Javelin'
        self.damage = '1d6'
        self.range = 30
        self.max_range = 120


class LightHammer(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'LightHammer'
        self.damage = '1d4'
        self.range = 20
        self.max_range = 60
        self.light = True


class Mace(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Mace'
        self.damage = '1d6'


class Quarterstaff(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Quarterstaff'
        self.damage = '1d6'
        self.damage_versatile = '1d8'
        self.versatile = True


class Sickle(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Sickle'
        self.damage = '1d4'
        self.light = True


class Spear(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Spear'
        self.damage = '1d6'
        self.damage_versatile = '1d8'
        self.versatile = True
        self.range = 20
        self.max_range = 60


class LightCrossbow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Light Crossbow'
        self.damage = '1d8'
        self.range = 80
        self.max_range = 320
        self.two_handed = True


class Dart(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Dart'
        self.damage = '1d4'
        self.range = 20
        self.max_range = 60
        self.two_handed = False
        self.finesse = False


class Shortbow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Shortbow'
        self.damage = '1d6'
        self.range = 80
        self.max_range = 320
        self.two_handed = True


class Sling(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Sling'
        self.damage = '1d4'
        self.range = 30
        self.max_range = 120


class Battleaxe(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Battleaxe'
        self.damage = '1d8'
        self.damage_versatile = '1d10'
        self.versatile = True


class Flail(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Flail'
        self.damage = '1d8'


class Glaive(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Flail'
        self.damage = '1d10'
        self.heavy = True
        self.two_handed = True
        self.reach = True


class Greataxe(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Greataxe'
        self.damage = '1d12'
        self.heavy = True
        self.two_handed = True


class Greatsword(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Greatsword'
        self.damage = '2d6'
        self.heavy = True
        self.two_handed = True


class Halberd(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Halberd'
        self.damage = '1d10'
        self.heavy = True
        self.two_handed = True


class Lance(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Lance'
        self.damage = '1d12'
        self.reach = True


class Longsword(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Longsword'
        self.damage = '1d8'
        self.damage_versatile = '1d10'
        self.versatile = True


class Maul(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Maul'
        self.damage = '2d6'
        self.heavy = True
        self.two_handed = True


class Morningstar(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Morningstar'
        self.damage = '1d8'


class Pike(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Pike'
        self.damage = '1d10'
        self.heavy = True
        self.reach = True
        self.two_handed = True


class Rapier(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Rapier'
        self.damage = '1d8'
        self.finesse = True


class Scimitar(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Scimitar'
        self.damage = '1d6'
        self.finesse = True
        self.light = True


class Shortsword(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Shortsword'
        self.damage = '1d6'
        self.finesse = True
        self.light = True


class Trident(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Trident'
        self.damage = '1d6'
        self.damage_versatile = '1d8'
        self.versatile = True
        self.range = 20
        self.max_range = 60


class WarPick(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'War Pick'
        self.damage = '1d8'


class Warhammer(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Warhammer'
        self.damage = '1d8'
        self.damage_versatile = '1d10'
        self.versatile = True


class Whip(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Whip'
        self.damage = '1d4'
        self.finesse = True
        self.reach = True


class Blowgun(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Blowgun'
        self.damage = '1d1'
        self.finesse = True
        self.range = 25
        self.max_range = 100


class HandCrossbow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Hand Crossbow'
        self.damage = '1d6'
        self.range = 30
        self.max_range = 120
        self.light = True


class HeavyCrossbow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Hand Crossbow'
        self.damage = '1d10'
        self.range = 100
        self.max_range = 400
        self.heavy = True
        self.two_handed = True


class Longbow(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Long Bow'
        self.damage = '1d8'
        self.range = 150
        self.max_range = 600
        self.heavy = True
        self.two_handed = True


class Net(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.name = 'Net'
        self.damage = '0d0'
        self.range = 5
        self.max_range = 15


class Weapons(object):
    def __init__(self):
        self.simple_melee = {
            'Club': Club(),
            'Dagger': Dagger(),
            'Greatclub': Greatclub(),
            'Handaxe': Handaxe(),
            'Javelin': Javelin(),
            'Light Hammer': LightHammer(),
            'Mace': Mace(),
            'Quarterstaff': Quarterstaff(),
            'Sickle': Sickle(),
            'Spear': Spear(),
        }

        self.simple_range = {
            'Light Crossbow': LightCrossbow(),
            'Dart': Dart(),
            'Shortbow': Shortbow(),
            'Sling': Sling(),
        }

        self.martial_melee = {
            'Battleaxe': Battleaxe(),
            'Flail': Flail(),
            'Glaive': Glaive(),
            'Greataxe': Greataxe(),
            'Greatsword': Greatsword(),
            'Halberd': Halberd(),
            'Lance': Lance(),
            'Longsword': Longsword(),
            'Maul': Maul(),
            'Morningstar': Morningstar(),
            'Pike': Pike(),
            'Rapier': Rapier(),
            'Scimitar': Scimitar(),
            'Shortsword': Shortsword(),
            'Trident': Trident(),
            'War Pick': WarPick(),
            'Warhammer': Warhammer(),
            'Whip': Whip(),
        }

        self.martial_range = {
            'Blowgun': Blowgun(),
            'Hand Crossbow': HandCrossbow(),
            'Heavy Crossbow': HeavyCrossbow(),
            'Longbow': Longbow(),
            'Net': Net(),
        }

    def is_weapon(self, name):
        if name in self.martial_melee.keys():
            return True
        elif name in self.martial_range.keys():
            return True
        elif name in self.simple_melee.keys():
            return True
        elif name in self.simple_range.keys():
            return True
        else:
            return False

    def get(self, weapon):
        if weapon in self.martial_melee.keys():
            return self.martial_melee[weapon]
        elif weapon in self.martial_range.keys():
            return self.martial_range[weapon]
        elif weapon in self.simple_melee.keys():
            return self.simple_melee[weapon]
        elif weapon in self.simple_range.keys():
            return self.simple_range[weapon]
    
    def get_simples(self):
        weapons = []
        for weapon in self.simple_melee:
            weapons.append(self.simple_melee[weapon])
        for weapon in self.simple_range:
            weapons.append(self.simple_range[weapon])
        return weapons

    def get_martials(self):
        weapons = []
        for weapon in self.martial_melee:
            weapons.append(self.martial_melee[weapon])
        for weapon in self.marial_range:
            weapons.append(self.martial_range[weapon])
        return weapons
