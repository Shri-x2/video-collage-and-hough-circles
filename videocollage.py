import os, cv2
from PIL import Image
path = "C:/Users/shryv/Documents/Shriyans JetLearn/pgzero/funimgs"
os.chdir(path)
h = 0
w=0

num_of_imgs = len(os.listdir("."))
print(num_of_imgs)
for i in os.listdir("."):
    img = Image.open(i)
    h += img.height
    w += img.width
h = h//num_of_imgs
w = w//num_of_imgs

for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        img = Image.open(i)
        img = img.resize((w,h))
        img.save(i, "PNG", quality = 95)

videoname = "mycollage.avi"
#os.chdir("C:/Users/shryv/Documents/Shriyans JetLearn/opencv")

imgs = []
for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        imgs.append(i)  

frame = cv2.imread(imgs[0])
height, width, layers = frame.shape
video = cv2.VideoWriter(videoname, 0, 1, (width, height))

for i in imgs:
    video.write(cv2.imread(i))
cv2.destroyAllWindows()
video.release()