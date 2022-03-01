from get_media import media_list, console, media_type
from get_user_id import username
import requests, random, requests, time, os


session = requests.Session()


def random_name():
    lst = []
    name = ""
    string = ("abcdefghjjklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789")
    for i in range(10):
        x = random.choice(string)
        lst.append(x)
    for i in lst:
        name = name + i
    return name
def create_dir(username):
    direc = "contents"
    individual_path = direc +"/"+username
    try:
        os.mkdir(direc)
        os.mkdir(individual_path)

        return individual_path

    except FileExistsError:
        os.mkdir(individual_path)
        return individual_path

saving_path = create_dir(username)

        
length_list = len(media_list)
console.print(f"Total Media : {length_list}",style = "bold #A020F0")
i = 1
for url in media_list:
   
    console.print(f"Downloading ..  {i} left .. {length_list-i}", style = "bold yellow")

    try:
        save_to_path = saving_path
        if len(url) < 80:
        
            #console.print("Content Type : Image", style = "italic red")
            name = random_name()
            complete_img_name = os.path.join(save_to_path, name+".jpg")
            r = session.get(url,allow_redirects=True)
            open(complete_img_name, 'wb').write(r.content)
            i += 1
            time.sleep(0.1)
        else:
            #console.print("Content Type : Video", style = " italic green")
            name = random_name()
            complete_vid_name = os.path.join(save_to_path, name+".mp4")
            r = session.get(url,allow_redirects=True)
            open(complete_vid_name, 'wb').write(r.content)
            i += 1
            time.sleep(0.1)
    except Exceptiption as e:
        print(e)
            
console.print("Done", style = "Bold red")        
