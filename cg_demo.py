import requests

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    key_list = ['Id', 'Name', 'Skill', 'Designation', 'Department', 'Location', 'Delete']
    try:
        # emp_list = requests.get('http://cd-awscp-bb-env.us-east-1.elasticbeanstalk.com/employee')
        emp_list = requests.get('http://localhost:5001/employee/getAll')
        #print json.dumps(emp_list.json(), indent=4)
    except Exception as e:
        return render_template('index.html', emp_list=emp_list.json(), key_list=key_list)


@app.route('/emp_delete/<emp_id>')
def emp_delete(emp_id):
    #print "Inside Delete"
    url = 'http://localhost:5001/employee/deleteEmployee/'+emp_id
    emp_id = requests.delete(url)
    return redirect(url_for('index'))


@app.route('/update/<emp_id>', methods=['GET', 'POST'])
def update(emp_id):
    if request.method == "GET":
        #print "INSIDE GET of Update"
        url = 'http://localhost:5001/employee/getEmployee/'+emp_id
        req = requests.get(url)
        return render_template('update.html', emp=req.json())
    elif request.method == "POST":
        #print "Inside update post method"
        url = 'http://localhost:5001/employee/updateEmployee'
        data = {}
        data['id'] = request.form['id']
        data['empName'] = request.form['name']
        data['skill'] = request.form['skill']
        data['designation'] = request.form['designation']
        data['department'] = request.form['department']
        data['location'] = request.form['location']
        req = requests.put(url, json=data)
        #print "STATUS CODE: "+str(req.status_code)
        return redirect(url_for('index'))


@app.route('/create_employee/', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        # url = 'http://cd-awscp-bb-env.us-east-1.elasticbeanstalk.com/employee'
        url = 'http://localhost:5001/employee/createEmployee'
        data = {}
        data['id'] = request.form['id']
        data['empName'] = request.form['name']
        data['skill'] = request.form['skill']
        data['designation'] = request.form['designation']
        data['department'] = request.form['department']
        data['location'] = request.form['location']
        # data = json.dumps(data)
        #print data
        req = requests.post(url, json=data)
        # print json.dumps(data)
        #print req.status_code
        return redirect(url_for('index'))
    return render_template('create_employee.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')



