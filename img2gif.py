import glob
from PIL import Image
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frames.reverse()
    frame_one = frames[0]
    frame_one.save("D:\資料科學\報告\總輸出\my_awesome.gif", format="GIF", append_images=frames[1:],
               save_all=True, duration=300, loop=0)
    
if __name__ == "__main__":
    make_gif("pic")
   # for image in glob.glob(f"{'pic'}/*.png"):
    #    print(image)
