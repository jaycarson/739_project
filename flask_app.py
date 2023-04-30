from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField
from SMV import SMV
from Simulation import Simulation


SECRET_KEY = 'development'


app = Flask(__name__)
app.config.from_object(__name__)


class CharacterClass(object):
    def __init__(self, owner):
        self.owner = owner
        self.dark_vision = 0
        self.name = 'None'


class NoClass(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)


class Bard(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)
        self.name = 'Bard'


class Barbarian(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)
        self.name = 'Barbarian'


class Cleric(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)
        self.name = 'Cleric'


class Druid(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)
        self.name = 'Druid'


class Fighter(CharacterClass):
    def __init__(self, owner):
        CharacterClass.__init__(owner)
        self.name = 'Fighter'


class CharacterRace(object):
    def __init__(self, owner):
        self.owner = owner
        self.stats = {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0}
        self.dark_vision = 0
        self.name = 'None'


class NoRace(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)


class Dwarf(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)
        self.name = 'Dwarf'


class Elf(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)
        self.name = 'Elf'


class Gnome(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)
        self.name = 'Gnome'


class Human(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)
        self.name = 'Human'


class HalfOrc(CharacterRace):
    def __init__(self, owner):
        CharacterRace.__init__(owner)
        self.name = 'Half Orc'


class CharacterForm(FlastForm):
    def __init__(self):
        self.name = ''
        self.character_class = ''
        self.points = 27
        self.points_current = 0
        self.points_max = 27
        self.proficiency = 0
        self.dark_vision = 0

        self.stats = {'str': 8, 'dex': 8, 'con': 8, 'int': 8, 'wis': 8, 'cha': 8}
        self.stats_final = {'str': 8, 'dex': 8, 'con': 8, 'int': 8, 'wis': 8, 'cha': 8}
        self.costs = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}

        self.stats_final = {}

        self.character_class = NoClass()
        self.character_race = NoRace()
   
        races = ['Dwarf', 'Elf', 'Gnome', 'Human', 'Half Orc']
        self.field_races = SelectField(label='Race', choices=races)

        classes = ['Bard', 'Barbarian', 'Cleric', 'Druid', 'Fighter']
        self.field_classes = SelectField(label='Class', choices=classes)

    def __call__(self):
        for stat in self.stats:
            self.stats_final[stat] = self.stats[stat] + self.character_race[stat]
        self.dark_vision = max(self.character_race.dark_vision, self.character_class.dark_vision)

    def adjust_stat(self, stat, amount):
        value = self.stats[stat]
        value_new = value + amount

        if value_new > 16 or value_new < 8:
            return

        cost_diff = self.costs[value_new] - self.costs[value]

        if self.points_current + cost_diff <= self.points_max:
            self.stats[stat] = value_new

    def change_class(self, name):
        classes = {
            'Bard', Bard,
            'Barbarian': Barbarian, 
            'Cleric': Cleric, 
            'Druid': Druid, 
            'Fighter': Fighter,
        }
        if name in classes:
            self.character_class = classes[name]()
        else:
            self.character_class = NoClass()

    def change_race(self, name):
        races = {
            'Dwarf': Dwarf,
            'Elf': Elf,
            'Gnome': Gnome,
            'Human': Human, 
            'Half Orc': HalfOrc
        }
        if name in races:
            self.character_race = races[name]()
        else:
            self.character_race = NoRace()


@app.route('/',methods=['post','get'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        print(form.sex.data)
    else:
        print(form.errors)
    return render_template('home.html')


@app.route('/create',methods=['post','get'])
def fertility():
    form = CharacterForm()
    form.change_race(request.form.get('character_race') or 'None'
    form.change_class(request.form.get('character_class') or 'None'

    sample_size = sim.results['sample size']

    return render_template(
        'create.html',
        form = form,
        char_race = form.character_race.name,
        char_class = form.character_class.name,
        stat_str = form.stats_final['str']
        stat_dex = form.stats_final['dex']
        stat_con = form.stats_final['con']
        stat_int = form.stats_final['int']
        stat_wis = form.stats_final['wis']
        stat_cha = form.stats_final['cha']
    )


@app.route('/update',methods=['post','get'])
def smv():
    race = 'Human'
    dnd_class = 'Fighter'
    strength = 
    height_m = request.form.get('height_m') or 60
    weight_m = request.form.get('weight_m') or 100
    age_m = request.form.get('age_m') or 18
    income_m = request.form.get('income_m') or 10000
    bf_m = request.form.get('bf_m') or 0
    bf_c_m = request.form.get('bf_m_c') or 0
    
    height_f = request.form.get('height_f') or 60
    weight_f = request.form.get('weight_f') or 100
    age_f = request.form.get('age_f') or 19
    income_f = request.form.get('income_f') or 10000
    bf_f = request.form.get('bf_f') or 0
    bf_c_f = request.form.get('bf_c_f') or 0

    attrs = {}

    attrs_m = {
        'sex': 'male',
        'height': int(height_m),
        'weight': int(weight_m),
        'bodyfat': int(bf_m),
        'bodyfat_c': int(bf_c_m),
        'income': int(income_m),
        'age': int(age_m),
        'state': 'Minnesota',
    }
    attrs_f = {
        'sex': 'female',
        'height': int(height_f),
        'weight': int(weight_f),
        'bodyfat': 0,
        #'bodyfat': int(bf_f),
        'bodyfat_c': 0,
        #'bodyfat_c': int(bf_c_f),
        'income': int(income_f),
        'age': int(age_f),
        'state': 'Minnesota',
    }

    app_m = SMV(debug=True, attrs=attrs_m)
    app_m.age_female = int(age_f)
    calc_smv_m = app_m()
    
    app_m_actual = SMV(debug=True, attrs=attrs_m)
    app_m_actual.age_female = int(age_f)
    app_m_actual.male_actual = True
    calc_smv_m_actual = app_m_actual()

    app_f = SMV(debug=True, attrs=attrs_f)
    calc_smv_f = app_f()

    form = SimpleForm()

    app_f.age = int(age_f) + 5
    app_f.weight = int(weight_f) + 10
    smv_f_5 = app_f()
    percent_f_5 = app_f.percent
    
    app_f.age = int(age_f) + 10
    app_f.weight = int(weight_f) + 20
    smv_f_10 = app_f()
    percent_f_10 = app_f.percent
    
    app_f.age = int(age_f)
    app_f.weight = int(weight_f)
    smv_f_0 = app_f()
    percent_f_0 = app_f.percent

    difference = calc_smv_m - calc_smv_f

    commentary_m = ""
    commentary_f = ""

    if calc_smv_m >= calc_smv_f:
        commentary_m += '\nYour SMV is greater than or equal to her SMV. First, you are not entitled to her. '

    commentary_m += app_m.results_weight + "\n"
    commentary_f += app_f.results_weight + "\n"

    commentary_m += app_m.results_income
    
    return render_template(
        'smv.html',
        form=form,
        smv_m=str(calc_smv_m),
        percent_m=str(round(app_m.percent, 1)),
        smv_m_actual=str(calc_smv_m_actual),
        percent_m_actual=str(round(app_m_actual.percent, 1)),
        smv_f= str(smv_f_0),
        smv_f_5= str(smv_f_5),
        smv_f_10= str(smv_f_10),
        percent_f=str(round(percent_f_0, 1)),
        percent_f_5=str(round(percent_f_5, 1)),
        percent_f_10=str(round(percent_f_10, 1)),
        commentary_m=commentary_m.split('\n'),
        commentary_f=commentary_f.split('\n'),
    )


if __name__ == '__main__':
    app.run(debug=True)
