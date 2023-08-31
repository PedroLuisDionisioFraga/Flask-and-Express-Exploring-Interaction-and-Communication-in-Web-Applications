from flask import Flask, request, render_template, redirect, session, url_for

employees = [
  {"name": "Pedro", "age": 20, "salary": 15000},
  {"name": "Maria", "age": 19, "salary": 14000},
  {"name": "João", "age": 14, "salary": 5000},
]

app = Flask(__name__)
# Definindo o caminho da minha pastas de templates(páginas)
app.template_folder = "./Pages"
app.static_folder = "./Scripts"
app.secret_key = 'super secret key'

@app.route("/")
def initialPage():
  return render_template("./index.html")

@app.route("/get-employees")
def get_employees():
  return {"employees": employees}

# Rota dinâmica que vai receber um valor em <age>
'''
  Basicamente eu estou passando em uma url um parâmetro,
nesse caso a idade do empregado, e ele vai me retornar
um json dos empregados acima dessa idade
'''
@app.route("/get-employees-age/<age>")
def get_employees_name(age):
  out_employees = []
  for employee in employees:
    if(employee["age"] > int(age)):
      out_employees.append(employee)

  return {"Employees": out_employees}

# Usando 2 informações
@app.route("/get-employees-info/<name>/<age>")
def get_employees_info(name, age):
  out_employees = []
  for employee in employees:
    # Verificando se a chave existe
    if employee["name"] == name and employee["age"] == int(age):
      out_employees.append(employee)

  return {"Employees": out_employees}

# Agora usando métodos http
# Em "methods" eu coloco apenas os métodos
# que vou usar, que serão os únicos permitidos
'''
  Note que eu n consigo entrar nessa página,
pois ao entrar numa página eu uso o método
'GET' pra acessar seu conteúdo e nessa rota
eu indiquei apenas usarei o método 'POST'
'''
@app.route("/get-all-infos", methods=['POST'])
def get_all_info():
  infos = request.json
  print(infos)

  return {"Employees": employees}

@app.route("/teste", methods=['POST', 'GET'])
def teste():
  if request.method == 'POST':
    infos = request.json
    print(f"infos: {infos}")
    print(f"Send a salary and value: {infos['info']} and {infos['value']}")
    return redirect(url_for('page2', info=infos['info'], value=infos['value']))
  return "Teste GET"

@app.route("/page2/<info>/<value>", methods=['GET'])
def page2(info, value):
  print(f"info: {info}, value: {value}")
  session.clear()
  return render_template("page2.html", info=info, value=value)

app.run(debug=True)
