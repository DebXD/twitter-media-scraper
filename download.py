from get_media import media_list, console, media_type
import requests, random, requests, time

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
        
length_list = len(media_list)
console.print(f"Total Media : {length_list}",style = "bold #A020F0")
i = 1
for url in media_list:
   
    console.print(f"Downloading ..  {i} left .. {length_list-i}", style = "bold yellow")
    try:
        if len(url) < 80:
        
            #console.print("Content Type : Image", style = "italic red")
            name = random_name()
            r = session.get(url,allow_redirects=True)
            open(name+'.jpg', 'wb').write(r.content)
            i += 1
            time.sleep(0.1)
        else:
            #console.print("Content Type : Video", style = " italic green")
            name = random_name()
            r = session.get(url,allow_redirects=True)
            open(name+'.mp4', 'wb').write(r.content)
            i += 1
            time.sleep(0.1)
    except Exceptiption as e:
        print(e)
            
console.print("Done", style = "Bold red")        
