def main():
    file = input("What is path of file? -> ") # Path of file to tif
    with open(f"{file}") as f: #open the file person put in path
        try: #try to get rid of file extension for the name
            file, lel = file.split('.')
        except: #uh oh
            pass #ignore
        for line in f: #lines
           for character in line: #characters
                tif = '​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'#opposite of timmywag
                with open(f"{file}TIF.py", "a", encoding="utf-8") as f: #open the file and write the stuffs
                    f.write(f"{character}{tif}") #write the character and then tif
if __name__ == "__main__": #ngl I don't know what this does
    main() #whole ahh function
