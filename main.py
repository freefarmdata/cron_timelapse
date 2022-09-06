import time
import os

import cv2

if __name__ == "__main__":

    device = 0
    folder = f'/etc/timelapse/device_{device}'
    retries = 5

    os.makedirs(folder, exist_ok=True)

    retry = 0
    captured = False
    camera = None

    while retry < retries:
        try:
            camera = cv2.VideoCapture(device)

            # small delay for hardware to initialize
            time.sleep(1)

            if not camera.isOpened():
                raise Exception('Camera not opened')

            result, frame = camera.read()

            if not result:
                raise Exception('Frame failed to capture')

            current_time = int(time.time())
            path = os.path.join(folder, f'{current_time}.jpg')
            cv2.imwrite(path, frame)
            captured = True
            break

        except Exception as e:
            print('Error while capturing image', e)
            retry += 1
            if camera:
                camera.release()

    camera.release()

    if not captured:
        print('Failed to capture image')

