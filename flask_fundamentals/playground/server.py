from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')          
def hello_world():
    return render_template("index.html", play = 3)  

@app.route('/<play>') 
def play_box(play):    
    print(play)
    return render_template("index.html", play=int(play))

@app.route('/<play>/<color>') 
def box_color(play, color):    
    print(play)
    return render_template("index.html", play=int(play), color = color)

if __name__=="__main__":   
    app.run(debug=True)