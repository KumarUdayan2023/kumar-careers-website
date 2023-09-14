from flask import Flask,render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)




    
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs,
                         company_name="Kumar")
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug= True)


# JOBS = [
#          {'id ': 1,
#          'type': "Data Analust",
#           'location': 'Surrey, BC',
#           'Salary':"$2000"},
  
#          {'id ': 2,
#          'type': "Data Scientist",
#           'location': 'Richmond, BC',
#           'Salary':"$3000"}, 
             
#          {'id ': 3,
#          'type': "Frontend Engineer",
#           'location': 'Vancouver, BC', 
#          'Salary': "$3400"},
          
#          {'id ': 4,
#          'type': "Backend Engineer",
#           'location': 'Portmoody, BC',
#           'Salary':"$3000"} 
          
#          ]



