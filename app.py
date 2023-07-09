from flask import Flask, request, jsonify,render_template
import openai
openai.api_key = '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'
app = Flask(__name__)

def gpt(text):
    messages=[{"role":"system","content":"you are a kind helpful assistant."}]
    message = text
    if message:
        messages.append(
            {"role": "user", "content": "please find out grammatical mistakes in this sentence:"+message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    content={"you said":text,"reply":reply}
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    return reply

@app.route('/',methods=['POST','GET'])
def Home():
    return render_template('home.html')
@app.route('/api/chat', methods=['POST','GET'])
def chat():
    user_message = request.json['message']
    print(user_message)
    chatbot_response = gpt(user_message)
    return jsonify({'message': chatbot_response})



if __name__ == '__main__':
    app.run()