from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        water_sent = request.form['water_sent']
        water_used = request.form['water_used']
        customer_num = request.form['customer_num']
        total_loss = float(water_sent) - float(water_used)
        return render_template('result.html', total_loss=total_loss, customer_num=customer_num)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
