"""
一个简单的API Web应用, 在CMD中运行Curl命令, 或者转Postman执行
curl http://localhost:5000/hello 
    返回'Hello,World'
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"John Doe\", \"email\": \"john.doe@example.com\"}" http://localhost:5000/users
    返回 
    {
        "email": "john.doe@example.com",
        "id": 2,
        "name": "John Doe"
    }
-X <COMMAND>：指定使用的 HTTP 方法（如 GET、POST、PUT、DELETE 等）    
-H <header>：添加自定义请求头,JSON 格式，示例：-H "Content-Type: application/json"
-d <data>：在 POST 请求中发送数据
-o <file>：将输出保存到指定文件
"""



from flask import Flask, request, jsonify

app = Flask(__name__)

# 一个简单的用户数据库
users = []

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# 每次发送都会创建只有一个新的user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {'id': len(users) + 1, 'name': data['name'], 'email': data['email']}
    users.append(user)
    return jsonify(user)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)