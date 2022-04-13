from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
#survey
@app.route('/')
def index():
    return render_template("index.html")
#survey result
@app.route('/result', methods=['POST'])
def survey_result():
	print("Got Post Info")
	print(request.form)
	session['form_name'] = request.form['name']
	session['form_location'] = request.form['location']
	session['form_language']= request.form['language']
	session['form_comment'] = request.form['comments']
	return redirect ("/show")

@app.route("/show")
def show_result():
	print(request.form)
	return render_template("result.html", form_name=session['form_name'], form_location=session['form_location'], form_language=session['form_language'],form_comment=session['form_comment'])

if __name__ == "__main__":
    app.run(debug=True)