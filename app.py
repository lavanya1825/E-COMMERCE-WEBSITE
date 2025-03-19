from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {
        'id': 1,
        'name': 'Coca-Cola',
        'description': 'Coca-Cola is a globally popular, carbonated, sweetened soft drink, best known as "Coke," invented by John Stith Pemberton in 1886, and is a cultural icon and a symbol of American tastes.',
        'price': 100,
        'image': 'https://www.bigbasket.com/media/uploads/p/xxl/60000655_9-coca-cola-soft-drink-original-taste.jpg'
    },
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
