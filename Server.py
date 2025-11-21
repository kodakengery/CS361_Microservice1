import zmq
import random

QUOTES = [
    'You are capable of more than you realize.',
    'Courage grows by taking bold steps',
    'Believe in yourself and all that you are.',
    'Challenges build champions',
    'Don\'t give up! Great things take time',
    'Each step brings you closer to your goal',
    'Your potential is limitless',
    'Stay positive, work hard, make it happen',
    'Small victories lead to big achievements'
]

# Establish Server TCP connection on port 5555
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://localhost:5555')

# Establish loop to receive incoming requests
while True:
    message = socket.recv()
    text = message.decode().strip()

    # Error Handling: Empy message
    if text == '':
        reply = 'Error: Requests for quote must have content'

    # Shut down the server
    elif text == 'Q':
        reply = 'Quitting server'
        socket.send_string(reply)
        break

    # Send back a quote if value is valid
    else:
        try:
            reply = random.choice(QUOTES)

        # Error handling
        except ValueError:
            reply = 'Error: Requests for quote must be a valid string'

    socket.send_string(reply + "\n " + text + " Completed!")

context.destroy()
