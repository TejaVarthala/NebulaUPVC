from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dynamic_content = "Welcome to our UPVC Interior Doors & Windows!"
    images = [
        {'url': 'p1.jpg', 'description': 'Sliding Windows'},
        {'url': 'p2.jpg', 'description': 'Sliding Doors'},
        {'url': 'p3.jpg', 'description': 'Sliding Doors Full'},
        {'url': 'p4.jpg', 'description': 'Windows Type-6'},
        {'url': 'p5.jpg', 'description': 'Windows Type-4'},
        {'url': 'p6.jpg', 'description': 'Balcony Doors'},
        # Add more images as needed
    ]
    return render_template('index.html', dynamic_content=dynamic_content, images=images)

if __name__ == '__main__':
    app.run(debug=True)
