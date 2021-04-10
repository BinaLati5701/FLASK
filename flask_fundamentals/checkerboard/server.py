from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", row = 8, column = 8 )

@app.route('/<x>/<y>')
def x_and_y(x, y):
    return render_template("index.html", row = int(x), column=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def colors(x, y, color1, color2): 
    return render_template("color.html", row = int(x), column=int(y), color1 = color1, color2 = color2)

if __name__== "__main__":
    app.run(debug=True)