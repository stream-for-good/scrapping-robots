import json
from test import select_video, watch_the_video_for, dislike_video, like_video, go_to_channel, search_with_url, search_bar, YouTube_Acces_Website, YouTube_FireFox_Accept_Cookies, YouTube_Deny_Log_In_And_Validate_General_Condition, YouTube_Get_Current_Url, YouTube_Get_Video_Id_From_Url
import time



# FAIRE LE PONT ENTRE SYLVAIN ET MOI
# SE LOGER SUR COMPTE GOOGLE

"""
TODO

Etoffer l'arbre
Faire en sorte que les fonctions de déplacement sur YouTube soient plus robustes

Créer un générateur de fichier json

Créer une session
Envoyer le numéro d'envoyer de la vidéo, et de quelle action il provient
Récupérer toutes les vidéos recommandée
VideoID, IndexOfVideo, AllRecommandedVideo
Faire un json exemple et l'envoyer sur discord

Dans 1 premier temps ; envoyer directement les données dès qu'on les as

"""


with open('bot.json') as jfile:
    file = json.load(jfile)["0"]
for x in file:
    print(x)
print("--"*10)

YouTube_Acces_Website()
time.sleep(5)
YouTube_Deny_Log_In_And_Validate_General_Condition()

with open("sessionURL--"+time.strftime("%d-%m-%y@%Hh%Mm%Ss",time.localtime()) + ".txt",'w+') as urlFile:
    for x in file:
        # Je ne vois pas trop comment l'implémenter ... Possible avec un object ou variable statique.
        if x["action"] == 'settings':
            pass
        elif x["action"] == 'search':
            search_bar(x["toSearch"])
        elif x["action"] == 'watch':
            if "url" in x:
                search_with_url(x["url"])
            elif "index" in x :
                select_video(x["index"])
            if "watchContext" in x:
                # LA : le paramètre doit être un nombre qui indique le nombre de seconde
                watch_the_video_for(x["watchContext"]["stopsAt"])
                if len(x["watchContext"]) != 1:
                    if x["watchContext"]["social"] == 'like':
                        like_video()
                    else :
                        dislike_video()
            # Write video url in file
            urlFile.write(YouTube_Get_Current_Url+"\n")
        elif x["action"] == 'goToChannel':
            go_to_channel()
    
