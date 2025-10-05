import os

def main():
    i = 0
    path = "C:/Users/Lenovo/Pictures/Screenshots"
    for filename in os.listdir(path):
        if not filename.lower().endswith('.png'):
            continue
        my_dest = "img" + str(i) + ".png"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest)
        os.rename(my_source, my_dest)
        i += 1
        
if __name__ == '__main__':
    main()