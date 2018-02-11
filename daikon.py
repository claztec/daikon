import json

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard')
def keyboard():
    # result = {'type':'buttons','buttons':['선택1', '선택2', '선택3']}
    result = {'type':'text'}
    result_str = json.dumps(result, ensure_ascii=False)
    response = make_response(result_str)
    return response

@app.route('/message', methods=['GET', 'POST'])
def message():
    user_key = ''
    type_str = ''
    content = ''
    if request.method == 'POST':
        print('post called')
        parameters = request.json
        user_key = parameters['user_key']
        type_str = parameters['type']
        content = parameters['content']
    else:
        print('else called')

    print(user_key)
    print(type_str)
    print(content)
    result = {}
    if (content == '취소하기') :
        result = {'message':{'text':'알았으'}}
    else:
        result = {'message': {'text': '안녕하세요.',
                              'photo': {
                                  'url': 'http://mud-kage.kakao.com/dn/cEluGu/btqhi9nfZpU/E3h8hxvWYVDpwKKg2f1rC0/img_a375x375.jpg',
                                  'width': 375, 'height': 375},
                              'message_button': {'label': '예약하기', 'url': 'kakaotalk://hairshop/shops/2943/product'}},
                  'keyboard': {'type': 'buttons',
                               'buttons': ['처음으로', '다시하기', '취소하기']}}

    result_str = json.dumps(result, ensure_ascii=False)
    print(result_str)
    response = make_response(result_str)
    return response


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')
