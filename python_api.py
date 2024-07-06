from flask import Flask, Response, request, jsonify
#from picamera import PiCamera

app = Flask(__name__)
#camera = PiCamera()

gyro_data = {}
distance_data = 0.0

@app.route('/gyro', methods=['POST'])
def receive_gyro_data():
    data = request.get_json()
    gyro_x = data['gyro_x']
    gyro_y = data['gyro_y']
    gyro_z = data['gyro_z']
    gyro_data['gyro_x'] = gyro_x
    gyro_data['gyro_y'] = gyro_y
    gyro_data['gyro_z'] = gyro_z
    return jsonify({'success': True})

@app.route('/distance', methods=['POST'])
def receive_distance_data():
    data = request.get_json()
    distance = data['distance']
    distance_data = distance
    return jsonify({'success': True})

@app.route('/gyro_values', methods=['GET'])
def get_gyro_values():
    return jsonify(gyro_data)

@app.route('/distance_value', methods=['GET'])
def get_distance_value():
    return jsonify({'distance': distance_data})

# =============================================================================
# # Route to stream the video
# @app.route('/video_feed')
# =============================================================================
# =============================================================================
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# =============================================================================

# Function to generate video frames
# =============================================================================
# def generate_frames():
#     while True:
#         # Capture a frame from the camera
#         camera.capture('frame.jpg', format='jpeg')
# 
#         # Read the captured frame
#         with open('frame.jpg', 'rb') as frame_file:
#             frame = frame_file.read()
# 
#         # Yield the frame as a response
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# 
# =============================================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
