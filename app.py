from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Flash 메시지 등에 사용되는 보안 키

# 사용자 데이터 파일 경로
USER_DB = 'user_db.json'

# 사용자 데이터 파일이 존재하지 않으면 빈 JSON 생성
if not os.path.exists(USER_DB):
    with open(USER_DB, 'w') as f:
        json.dump({}, f)


# 비밀번호를 SHA-256으로 해시
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# 메인 페이지: 로그인/회원가입 폼 렌더링
@app.route('/')
def home():
    return render_template('login.html')


# 회원가입 처리
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # 사용자 데이터 로드
    with open(USER_DB, 'r') as f:
        users = json.load(f)

    # 중복 사용자 확인
    if username in users:
        flash('이미 존재하는 사용자입니다.', 'error')
        return redirect(url_for('home'))

    # 사용자 추가 및 저장
    users[username] = hash_password(password)
    with open(USER_DB, 'w') as f:
        json.dump(users, f)

    flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
    return redirect(url_for('home'))


# 로그인 처리
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 사용자 데이터 로드
    with open(USER_DB, 'r') as f:
        users = json.load(f)

    # 인증 확인
    if username in users and users[username] == hash_password(password):
        flash(f'{username}님, 로그인 성공!', 'success')
    else:
        flash('아이디 또는 비밀번호가 잘못되었습니다.', 'error')

    return redirect(url_for('home'))


# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
