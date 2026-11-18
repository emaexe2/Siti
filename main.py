from flask import Flask
import random
app = Flask(__name__)

oggetti = ['Spada di diamante', 'Piccone di ferro', 'Arco', 'Freccia', 'Scudo', 'Ascia di pietra', 'Pala di legno', 'Canna da pesca', 'Bussola', 'Orologio', 'Secchio', 'Acciarino', 'Cesoie', 'Tridente', 'Elitre']
blocchi = ['Terra', 'Pietra', 'Erba', 'Sabbia', 'Ghiaia', 'Legno di quercia', 'Ossidiana', 'TNT', 'Diamante grezzo', 'Netherrack', 'Glowstone', 'Lana bianca', 'Vetro', 'Bedrock']
mob = ['Creeper', 'Zombie', 'Scheletro', 'Ragno', 'Enderman', 'Maiale', 'Mucca', 'Pecora', 'Gallina', 'Villager', 'Blaze', 'Ghast', 'Slime', 'Lupo']
cibo = ['Mela', 'Mela d\'oro', 'Pane', 'Carota', 'Patata al forno', 'Bistecca', 'Torta', 'Biscotto', 'Anguria', 'Zuppa di funghi']

@app.route('/')
def base():
    return 'Benvenuto nel generatore di oggetti di Minecraft!'

@app.route('/oggetto')
def oggetto_random():
    return random.choice(oggetti)

@app.route('/blocco')
def blocco_random():
    return random.choice(blocchi)

@app.route('/mob')
def mob_random():
    return random.choice(mob)

@app.route('/cibo')
def cibo_random():
    return random.choice(cibo)

@app.route('/inventario')
def inventario():
    return random.choice(oggetti) + ', ' + random.choice(blocchi) + ', ' + random.choice(cibo)

@app.route('/battaglia')
def battaglia():
    return 'Combatti contro un ' + random.choice(mob) + ' con: ' + random.choice(oggetti)

@app.route('/creeper')
def creeper():
    return 'BOOM!'

@app.route('/creeper/big')
def creeper_big():
    return 'BOOOOOOOOOOOOOOOOOOOOOOOOOM!!!'

@app.route('/miniera')
def miniera():
    return 'scava scava scava...'

@app.route('/miniera/profonda')
def miniera_profonda():
    return 'hai trovato: ' + random.choice(blocchi)

@app.route('/miniera/profonda/segreto')
def segreto():
    return 'hai trovato un DIAMANTE! sei fortunatissimo!'

app.run(debug=True)
