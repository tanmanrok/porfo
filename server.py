"""Testing Idea"""
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def write_to_csv(data):
    """Write Data Email List"""
    with open('database.csv', mode='a', newline='', encoding='UTF-8') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    
@app.route('/')
def my_home():
    """Main Page"""
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    """All Pages"""
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit"""
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/#thanks')
    else:
        return 'Something went Wrong'
