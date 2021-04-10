from flask import Flask  
app = Flask(__name__) 

@app.route('/')          
def hello_world():
    return 'Hello World!'  
    
@app.route('/dojo')
def dojo():
    return "Dojo!"

# returns "Hi Flask!", "Hi Michael!", "Hi John!"
@app.route('/say/<name>') 
def hi(name):    
    print(name)
    return f"Hi, {name}!" 

# returns "hello" 35 times, "bye" 80 times, "dog" 99 times
@app.route('/repeat/<int:number>/<word>') 
def show_user_profile(number, word):
    print(number)
    print(word)
    return ((word) * (number))

@app.route('/<message>')
def message(message):
    print(message)
    return f"Sorry! No response. Try again."

@app.route('/<error>/<message>')
def error_message(error, message):
    print(error, message)
    return f"Sorry! No response. Try again."

@app.route('/<error>/<message>/<warning>')
def warning(error, message, warning):
    print(error, message, warning)
    return f"Sorry! No response. Try again."



if __name__=="__main__":   
    app.run(debug=True)    

