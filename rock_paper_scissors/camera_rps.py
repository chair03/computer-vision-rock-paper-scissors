from typing import List
import cv2
from keras.models import load_model
import numpy as np
import time

class rock_paper_scissors_model:
    def __init__(self):
        self.game_values = ['rock','paper','scissors','None']
    
    '''
    The prediction is a 2d array so we have to index into it to get the actual probabilities
    Returns the string output ie rock 
    '''
    def get_prediction(self,prediction :List)->str:
        prediction_value = prediction[0]
        max_index = np.argmax(prediction_value)
        return self.game_values[max_index]

    '''
    Open a webcam and get the model predictions
    The camera will wait two seconds to let the user make a pose
    '''
    def get_user_prediction()->str:
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        init_time = time.time()

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.putText(frame,"Please enter your move!!",(200,300),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            time_elapsed = time.time() - init_time
            if (cv2.waitKey(1) & 0xFF == ord('q')) or (time_elapsed>2):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return prediction

    