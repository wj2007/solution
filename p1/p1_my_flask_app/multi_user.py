"""
C:\Jia\dev_home\daily_practise\solution\p1\p1_my_flask_app>curl -o user_data.txt http://localhost:5000/users  
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   171  100   171    0     0    773      0 --:--:-- --:--:-- --:--:--   773

"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# 一个简单的用户数据库
users = []

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # 检查数据格式是否正确
    if isinstance(data, list):  # 如果是列表，则为批量添加
        for user_data in data:
            user = {'id': len(users) + 1, 'name': user_data['name'], 'email': user_data['email']}
            users.append(user)
        return jsonify(users), 201  # 返回所有用户的列表及状态码

    elif isinstance(data, dict):  # 如果是字典，则为单个用户
        user = {'id': len(users) + 1, 'name': data['name'], 'email': data['email']}
        users.append(user)
        return jsonify(user), 201  # 返回新建用户及状态码
    return jsonify({'error': 'Invalid data format.'}), 400  # 返回错误信息及状态码

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)