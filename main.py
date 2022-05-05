from util import image_read, image_write
from ex5 import  image_rotation

def main():

    sim = image_read('dog.jpeg')
    
    angle = 20
    x = 40
    y = 100
   
    rim = image_rotation( sim, angle, x, y )
    
    image_write( rim, "rotate-out.jpg")
    

if __name__ == "__main__":
    main()