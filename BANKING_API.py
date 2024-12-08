from flask import Flask, request, jsonify
from database import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all() 


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    # Create new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'Account created successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({'message': 'Invalid username or password'}), 400
    
    return jsonify({'message': 'Login successful!'}), 200


@app.route('/balance', methods=['GET'])
def balance():
    username = request.args.get('username')  
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify({'balance': user.balance}), 200


@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    username = data.get('username')
    amount = data.get('amount')
    
    if amount <= 0:
        return jsonify({'message': 'Deposit amount must be positive'}), 400
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user.balance += amount
    db.session.commit()
    
    return jsonify({'message': f'Deposited {amount} successfully!', 'new_balance': user.balance}), 200


@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    username = data.get('username')
    amount = data.get('amount')
    
    if amount <= 0:
        return jsonify({'message': 'Withdrawal amount must be positive'}), 400
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if user.balance < amount:
        return jsonify({'message': 'Insufficient balance'}), 400
    
    user.balance -= amount
    db.session.commit()
    
    return jsonify({'message': f'Withdrawn {amount} successfully!', 'new_balance': user.balance}), 200

# Delete a user account
@app.route('/delete', methods=['DELETE'])
def delete_account():
    data = request.get_json()
    username = data.get('username')
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'Account deleted successfully!'}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
