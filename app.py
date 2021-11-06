import collaborative_filter as cf
from flask import Flask, request, render_template 
  
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    scores = []
    scores.append(request.form['movie0'])
    scores.append(request.form['movie1'])
    scores.append(request.form['movie2'])
    scores.append(request.form['movie3'])
    scores.append(request.form['movie4'])
    scores.append(request.form['movie5'])
    scores.append(request.form['movie6'])
    scores.append(request.form['movie7'])
    scores.append(request.form['movie8'])
    scores.append(request.form['movie9'])
    
    results = cf.create_matrix(scores)
    #results = ["1", "2", "4", "5"]
    return render_template('index.html', content="<p>" + "</p><p>".join(results) + "</p>")

if __name__ == '__main__':
    app.run(debug=True)	