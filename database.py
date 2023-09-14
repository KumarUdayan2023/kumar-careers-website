from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DATABASE_CONNECTION_STRING']



engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl":{
      "ssl_python database.pyca": "/etc/ssl/cert.pem"
    }
  })
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs



  
  # result_all = result.fetchall()
  # print("type(result_all()): ", type(result_all))
  # print()

  # first_dict_row = result_all[1]._asdict()
  # print(first_dict_row)

# for row in result_all:
#   row_dict = row._asdict()
#   print("type of row_dict: ",type(row_dict))
#   print(row_dict)


  
  
