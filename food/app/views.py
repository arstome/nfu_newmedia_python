
# coding: utf-8

# In[1]:
from flask import render_template,flash,redirect, Flask, request, escape
from app import app
from random import sample


@app.route('/')
def index() -> 'html':
    return render_template('index.html', the_title = "选择困难症患者饭点助选器")
       
def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
        
@app.route('/results',methods = ['POST'])
def results() -> 'html' :
    x = request.form['x']
    y1 = ['白粥','鸡蛋','c','d','e','f']
    y2 = ['米线','','e','r','t','y'] 
    y3 = ['白饭','2','3','4','5','6']
    if 'bf' in x:
     y = sample(y1,3),'放弃吧已经是中午了'
    elif 'lc' in x:
     y = sample(y2,3),'这算是早餐了还是两个鸡蛋就算了吧'
    else: y = sample(y3,3),'少吃点吧万一有人叫你去宵夜呢'
    title = '已预约成功'
    log_request(request, results)
    return render_template('results.html',
                           the_x=x,
                           the_y=y)

@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('houtai.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


# In[ ]:



