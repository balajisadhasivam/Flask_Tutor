from flask import *
app = Flask(__name__,template_folder='template')

@app.route('/home/<name>',methods=['GET'])
def home(name):
    print(name)
    return render_template('index.html',user_name=name)
    

if __name__=="__main__":

    app.run()