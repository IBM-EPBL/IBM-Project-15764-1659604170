from flask import Flask,render_template,request
app = Flask(__name__,template_folder="templates")
@app.route('/')
@app.route('/register',methods=['GET','POST'])
def register():
      if request.method == "POST":
          username = request.form.get('username')
          email = request.form.get('email')
          phone = request.form.get('phone')

          return display_info(username,email,phone)
      return render_template('registerdisplay.html')
      
def display_info(name,mail,phone):
      return f'''
          <center>
           <h2> Details: </h2>
           <p> username : {name} </p>
           <p> email : {mail} </p>
           <p> phone : {phone} </p>
          </center>
      
      '''  
if __name__==('__main__'):
    app.run(debug=True,port=5000) 
