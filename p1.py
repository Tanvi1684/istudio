from flask import Flask,render_template,request,url_for
import mysql.connector

app=Flask(__name__,template_folder='templates')

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="istudio"
)
cursor=db.cursor()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/feature')
def feature():
    return render_template('feature.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        sql="INSERT INTO `contact`(`name`, `email`, `subject`, `message`) VALUES (%s,%s,%s,%s)"
        value=(name,email,subject,message)
        cursor.execute(sql,value)
        db.commit()
        return "Succesed"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


