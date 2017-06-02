
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
    with open('houtai.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
        
@app.route('/results',methods = ['POST'])
def results() -> 'html' :
    x = request.form['x']
    y1 = ['白粥','鸡蛋','油条','肠粉','面条','米粉','面包']
    y2 = ['西红柿炒鸡蛋','鱼香茄子','咖喱牛肉','宫保鸡丁','蒸水蛋','青菜'] 
    y3 = ['西兰花炒肉片','凉拌青瓜','客家酿豆腐','蒜香小龙虾','小鸡炖蘑菇','糖醋排骨']
    if '早餐' in x:
     y = sample(y1,3),'放弃吧已经是中午了'
    elif '午餐' in x:
     y = sample(y2,3),'这算是早餐了还是两个鸡蛋就算了吧'
    else: y = sample(y3,3),'少吃点吧万一有人叫你去宵夜呢'
    title = '已预约成功'
    
    log_request(request, results)
    return render_template('results.html',
                           the_x=x,
                           the_y=y)

@app.route('/houtai')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('houtai.log') as log:
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



