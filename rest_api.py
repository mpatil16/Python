from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

cors = CORS(app, resources={r"/employee/*": {"origins": "*"}})

data = [
    {
        "id": 1001,
        "empName": "Balyan,Ankit",
        "skill": "Java",
        "designation": "Analyst",
        "department": "Sogeti",
        "location": "Newyork"
    },
    {
        "id": 1002,
        "empName": "Solanki,Satish",
        "skill": "Python",
        "designation": "Consultant",
        "department": "Sogeti",
        "location": "Mumbai"
    },
    {
        "id": 1003,
        "empName": "Kant,Ripu",
        "skill": "AngularJS",
        "designation": "Consultant",
        "department": "AppsOne","location":"Newyork"
    },
    {
        "id": 1004,
        "empName": "Chouhan, Arpit",
        "skill": "Flask",
        "designation": "Consultant",
        "department": "AppsTwo",
        "location": "Pune"
    },
    {
        "id": 1005,
        "empName": "Bhansali,Sanjay",
        "skill": "Java",
        "designation": "Consultant",
        "department": "Sogeti",
        "location": "Singapore"
     },
    ]


@app.route('/employees', methods=['GET'])
#@cross_origin(origin='localhost',headers=['Content- Type', 'Authorization'])
@cross_origin()
def get_all():
    data.sort(key=lambda x: x.get('id'))
    print(json.dumps(data, indent=4))
    if not data:
        return json.dumps([])
    return json.dumps(data)


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    for name in data:
        if str(name['id']) == str(id):
            print("inside if\n")
            return json.dumps([name])
    return json.dumps([])


@app.route('/employees', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        #print("loading....\n")
        empdata = request.get_json(force=True)
        #print(json.dumps(empdata, indent=4))
        #print(type(empdata))
        datato_save = {}
        datato_save['id'] = int(empdata['id'])
        datato_save['empName'] = empdata['empName']
        datato_save['skill'] = empdata['skill']
        datato_save['designation'] = empdata['designation']
        datato_save['department'] = empdata['department']
        datato_save['location'] = empdata['location']
        data.append(datato_save)
        return json.dumps({"status": "True"})
    else:
        return json.dumps({"status": "False"})


@app.route('/employees/<int:id>', methods=['GET', 'PUT'])
def update_employee(id):
    print("inside update =",request.method)
    if request.method == 'PUT':
        d = request.get_json(force=True)
        for name in data:
            print(name, d)
            if str(name['id']) == str(d['id']):
                print("INSIDE IF")
                name['empName'] = d['empName']
                name['skill'] = d['skill']
                name['designation'] = d['designation']
                name['department'] = d['department']
                name['location'] = d['location']
                return json.dumps({"status": "True"})
    return json.dumps({"status": "False"})


@app.route('/employees/<int:emp_id>', methods=['GET', 'DELETE'])
def delete_employee(emp_id):
    if request.method == 'DELETE':
        for e in range(len(data)):
            if str(data[e]['id']) == str(emp_id):
                data.pop(e)
                return json.dumps({"status": "True"})
        return json.dumps({"status": "False"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
