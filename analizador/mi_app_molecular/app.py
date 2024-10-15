from flask import Flask, render_template, request, jsonify
from chempy import Substance, Reaction
from chempy.chemistry import Substance
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/tabla-periodica')
def tabla_periodica():
    return render_template('tabla_periodica.html')

@app.route('/construir-molecula', methods=['POST'])
def construir_molecula():
    data = request.json
    formula = data.get('formula')
    try:
        molecula = Substance.from_formula(formula)
        return jsonify({
            'success': True,
            'formula': molecula.formula,
            'molar_mass': molecula.molar_mass(),
            'composition': molecula.composition
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/calcular-balance', methods=['POST'])
def calcular_balance():
    data = request.json
    reactivos = data.get('reactivos', [])
    productos = data.get('productos', [])
    try:
        reaccion = Reaction(reactivos, productos)
        balance = reaccion.balance()
        return jsonify({
            'success': True,
            'balance': balance
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/calcular-energia', methods=['POST'])
def calcular_energia():
    data = request.json
    formula = data.get('formula')
    try:
        molecula = Substance.from_formula(formula)
        # Este es un cálculo de energía simplificado. En una aplicación real,
        # se usarían métodos más sofisticados.
        energia = sum([atom.mass for atom in molecula.atoms]) * 100
        return jsonify({
            'success': True,
            'energia': energia
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)