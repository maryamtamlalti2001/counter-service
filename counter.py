from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
import os


app=Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
csrf = CSRFProtect(app)



#define the file's path to store the data 

COUNTER_FILE="./data/counter.txt"

#it will be mounted aas a volume 

def read_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE,"r") as f:
            return int(f.read().strip())
    else:
        return 0
    
def update_counter(counter):
    with open(COUNTER_FILE,'w') as f:
        f.write(str(counter))

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    #this functioin handles the get and post requests 
    counter= read_counter()
    if request.method == "POST":
        counter+=1
        update_counter(counter)
        return  f"POST requests counter updated. Current count: {counter}"
    elif request.method == "GET":
        return f"Current POST requests count: {counter}"
    
    @app.route('/health',methods=["GET"])
    def health_check():
        try:
    # Basic health check: Ensure the counter file is accessible.
            read_counter()
            return jsonify({"status": "healthy"}), 200
        except Exception as e:
            return jsonify({"status": "unhealthy", "reason": str(e)}), 500



if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080, debug=False)
        

    
    
    



   

