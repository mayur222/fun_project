import time
import cv2


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    WIDTH = 640
    HEIGHT = 360
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)
    time.sleep(3)
    t1 = time.time()
    COUNT = 0
    ret, main = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (WIDTH, HEIGHT))

    while COUNT < WIDTH:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        i = COUNT % WIDTH
        COUNT = COUNT+1
        temp = img
        main[:, i] = img[:, i]
        temp[:, :i] = main[:, :i]
        temp = cv2.line(temp, (i, 0), (i, HEIGHT-1), (255, 127, 127), 1)
        cv2.imshow('video', temp)
        out.write(temp)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    t2 = time.time()
    print(t2-t1)
    if COUNT == WIDTH:
        cv2.imwrite('output.jpg', main)
        print('Saved')

    cap.release()
    out.release()
    cv2.destroyAllWindows()
