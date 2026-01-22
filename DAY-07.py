from flask import Flask,request,jsonify

app=Flask(__name__)

users=[{id1,name Raja},
       {id 2, name Rama} ]

@app.route(,methods=[Get])
def home()
    return  Welcome

@app.route(users,methods=[Get])
def get_users()
    return  jsonify(users)

@app.route(usersintuser_id,methods=[Get])
def get_user(user_id)

    for user in users
        if user[id]==user_id
            return jsonify(user)
    return jsonify({messageuser not found}),404

@app.route(users,methods=[POST])
def add_user()
    data=request.json
    newuser={
        idlen(users)+1,namedata.get(name)
    }
    users.append(newuser)
    return jsonify(newuser),201

@app.route(usersintuser_id,methods=[PUT])
def update_user(user_id)
    data=request.json
    for user in users
        if user[id] == user_id
            user[name]=data.get(name)
            return jsonify(user)
    return jsonify({message user not found}), 404


@app.route(usersintuser_id,methods=[PATCH])
def update_user(user_id)
    data=request.json
    for user in users
        if user[id] == user_id
            user[name]=data.get(name)
            return jsonify(user)
    return jsonify({message user not found}), 404


if __name__==__main__
    app.run(debu