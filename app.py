

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def priority(c):
    if c=='^':
        return 2
    elif c =='/' or c=='*':
        return 1
    elif c =='+' or c=='-':
        return 0
    else:
        return -1

def infix_to_postfix(s):
    postfix = []
    stack = []
    for i in range(len(s)):
        c = s[i]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and (priority(s[i]) < priority(stack[-1]) or priority(s[i]) == priority(stack[-1])):
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    infix_expr = data.get('infix')

    postfix_expr = infix_to_postfix(infix_expr)
    return jsonify({'postfix': postfix_expr})

if __name__ =='__main__':
    app.run(debug=True)