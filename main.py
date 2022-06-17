#!/usr/bin/env python

import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.latex import parse_latex
from sympy.printing import latex

app = Flask(__name__)
CORS(app)

# symbolically representing x, y, z for operations
x, y, z = sympy.symbols('x y z')

# Convert expression into json object encoded in LaTeX
def expression_to_json(obj):
    return jsonify({"result": str(latex(obj))})

def get_expression(request):
    content = request.json
    expr = content["expr"]
    return expr

@app.route('/')
def index():
    return 200

@app.route('/simplify', methods=['POST'])
def simplify_handler():
    expr = get_expression(request)
    result = sympy.simplify(parse_latex(expr))
    print(f'Parsing {expr}\nResult {result}')
    return expression_to_json(result)

@app.route('/derivative', methods=['POST'])
def derivative_handler():
    return expression_to_json(sympy.diff(parse_latex(get_expression(request)), x))

app.run()
