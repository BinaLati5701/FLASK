from flask import Flask, render_template 
practice = Flask(__name__) 

@practice.route('/')          
def hello_world():
    return render_template("index.html")  

@practice.route('/<name>/<times>') 
def hello_person(name, times):    
    print(name)
    return render_template("name.html", some_name=name, num_times=int(times))

if __name__=="__main__":   
    practice.run(debug=True)