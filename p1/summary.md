总结

 - Flask 的内置开发服务器不支持 HTTPS, 默认配置不包括SSL/TLS 支持，适合开发和测试
 - 对于生产环境，推荐使用 WSGI 服务器(如 Gunicorn)配合 Nginx, Nginx可以有效地处理 HTTPS 连接，并且是当前最佳实践
 - 确保为你的应用配置有效的 SSL/TLS 证书，以确保通信安全.


执行
- python -m venv p1_venv
- \solution\p1\p1_venv\Scripts> .\activate
- python.exe -m pip install --upgrade pip
- pip install flask
- .\p1_venv\Scripts\python.exe .\p1_my_flask_app\multi_user.py


Curl命令
- -X <COMMAND>：指定使用的 HTTP 方法（如 GET、POST、PUT、DELETE 等）    
- -H <header>：添加自定义请求头,JSON 格式，示例：-H "Content-Type: application/json"
- -d <data>：在 POST 请求中发送数据
- -o <file>：将输出保存到指定文件
