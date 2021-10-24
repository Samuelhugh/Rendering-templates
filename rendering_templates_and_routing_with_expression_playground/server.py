from flask import Flask, render_template # Import Flask from flask to allow us to create our app, and render template.
app = Flask(__name__) # Create a new Instance of the Flask called "app".
@app.route('/play')
def play():
    return render_template('index.html', num=3)
@app.route('/play/<int:num>')
def addbox(num):
    return render_template('index.html', num=num)
@app.route('/play/<int:num>/<color>')
def addcolor(num, color):
    return render_template('index.html', num=num, color=color)
if __name__ == '__main__': # Ensure this file is being run directly and not from a different module
    app.run(debug=True) # If true run in Debug mode.