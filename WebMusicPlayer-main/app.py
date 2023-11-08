from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<int:song_number>')
def serve_audio(song_number):
    song_filename = f'static/audio/Audio-{song_number}.mp3'
    return send_from_directory('', song_filename)

@app.route('/get_song_list')
def get_song_list():
    total_number_of_songs = 48 
    song_list = [f'Audio-{i}.mp3' for i in range(1, total_number_of_songs + 1)]
    return jsonify({'songs': song_list})

if __name__ == '__main__':
    app.run(debug=True)