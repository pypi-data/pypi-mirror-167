import requests
from bs4 import BeautifulSoup

def GameData():
    from datetime import datetime
    try:
        from pytz import timezone
    except:
        return({"Error":"pytz not detected! please install pytz! Error code 1"})
    Result = {
        "Online_User": "",
        "WOTDLink" : "",
        "WOTDName" : "",
        "GTTime" : "",
        "GTDate" : ""
    }
    try:
        Website = requests.get(f"https://www.growtopiagame.com/detail").json()

        Result["Online_User"] = Website["online_user"]
        Result["WOTDLink"] = Website["world_day_images"]["full_size"] 
        Result["WOTDName"] = ((Data["WOTDLink"].replace('https://www.growtopiagame.com/worlds/','')).replace('.png','')).upper()
        Result["GTTime"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%X")
        Result["GTDate"] = datetime.now(timezone('UTC')).astimezone(timezone('America/New_York')).strftime("%x")
        return Result
    except: 
        return({"Error":"It looks like we can't reach growtopiagame.com! Error code 2"})

def ItemData(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                Result = {}
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                if len(HTMLResult.select(".gtw-card")) == 1:
                    Properties = HTMLResult.find_all('div',  class_= "card-text")
                    Data = HTMLResult.select(".card-field")
                    Rarity = BeautifulSoup((str((HTMLResult.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
                    PropertiesResult = []
                    for add in Properties:
                        hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                        PropertiesResult.append(hum.text)
                    Result.update({"Description": PropertiesResult[0].strip()})
                    Result.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})
                    try:
                        Result.update({"Rarity": int(Rarity)})
                    except:
                        Result.update({"Rarity": "None"})
                    DataResult = []
                    for typ in Data:
                        mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                        DataResult = (((mus.text).split(",")))
                    res = 0 
                    while res <= (len(DataResult)-3):
                        Result.update({DataResult[res].strip(): DataResult[res+1].strip()})
                        res = res+2
                    check = 0
                    for fix in Result.keys():
                        if check == 3:
                            Result[fix] = Result[fix].split(" - ")
                        if check == 8:
                            Result[fix] = Result[fix].split(" ")
                        if check == 7:
                            restore = []
                            for number in Result[fix].split(" "):
                                input = ""
                                for number2 in number:
                                    if number2.isdigit():
                                        input = input+number2
                                if input != "":
                                    restore.append(input)
                            Result[fix] = {
                                    "Fist":restore[0],
                                    "Pickaxe":restore[1],
                                    "Restore":restore[2]
                            }
                        check +=1
                    try:
                        ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    Result["Title"] = ItemTitle
                else:
                    for HTMLResultTabber in HTMLResult.select(".gtw-card"):   
                        Result2 = {}   
                        PropertiesResult = []
                        Properties = HTMLResultTabber.find_all('div',  class_= "card-text")
                        Data = HTMLResultTabber.select(".card-field")
                        Rarity = BeautifulSoup((str((HTMLResultTabber.find('small'))).replace("(Rarity: ","")).replace(")", ""), "html.parser").text
                        for add in Properties:
                            hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                            PropertiesResult.append(hum.text)
                        Result2.update({"Description": PropertiesResult[0].strip()})
                        Result2.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})

                        try:
                            Result2.update({"Rarity": int(Rarity)})
                        except:
                            Result2.update({"Rarity": "None"})
                        DataResult = []
                        for typ in Data:
                            mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                            DataResult = (mus.get_text(" ",strip=True)).split(",")

                        res = 0 
                        while res <= (len(DataResult)-3):
                            Result2.update({DataResult[res].strip(): DataResult[res+1].strip()})
                            res = res+2  

                        check = 0
                        for fix in Result2.keys():
                            if check == 3:
                                Result2[fix] = Result2[fix].split(" - ")
                            if check == 8:
                                Result2[fix] = Result2[fix].split(" ")
                            if check == 7:
                                restore = []
                                for number in Result2[fix].split(" "):
                                    input = ""
                                    for number2 in number:
                                        if number2.isdigit():
                                            input = input+number2
                                    if input != "":
                                        restore.append(input)
                                Result2[fix] = {
                                        "Fist":restore[0],
                                        "Pickaxe":restore[1],
                                        "Restore":restore[2]
                                }
                            check +=1
                        try:
                            ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        Result[ItemTitle] = Result2
                        Result[ItemTitle]["Title"] = ItemTitle
                try:
                    return Result[ItemFinder["items"][0]["title"]]
                except:
                    if NameItem in Result.keys():
                        return Result[NameItem]
                    else:
                        return Result
            except:
                return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 3"})            
        except IndexError:
            return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 2"})
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later. Error Code 1"})

def ItemRecipe(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                require = []
                Result = {}
                def Insert(this,Recipe):
                    if this in Recipe.keys():
                        Recipe[this].append([])
                        for meh in item.select('td'):
                            meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[this][1].append(meh.replace(u'\xa0', u''))                 
                    else:
                        Recipe[this] = [[]]
                        for meh in item.select('td'):
                            meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[this][0].append(meh.replace(u'\xa0', u'')) 

                def Insert2(this,Recipe):
                    if this in Recipe[meh].keys():
                        Recipe[meh][this].append([])
                        for the in mes.select('td'):
                            the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[meh][this][1].append(the.replace(u'\xa0', u''))                    
                    else:
                        Recipe[meh][this] = [[]]
                        for the in mes.select('td'):
                            the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[meh][this][0].append(the.replace(u'\xa0', u'')) 

                def Title(itemish):
                    try:
                        ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    return ItemTitle
                if Region == "id":
                    ind = HTMLResult.select_one(".tabber.wds-tabber")
                    if len(HTMLResult.select(".gtw-card")) == 1:
                        ws = 0
                        count = 0
                        Recipe = {}
                        for item in HTMLResult.select(".content"):
                            if item.select(".content") == []:
                                if not count in require:
                                    Insert(((item.find('th')).text).strip(), Recipe)
                                ws += 1
                            else:
                                meh = ((item.find('th')).text).strip()
                                Recipe[meh] = {}
                                for mes in item.select(".content"):
                                    Insert2(((mes.find('th')).text).strip(), Recipe)
                                    ws += 1
                                    require.append(ws)
                            count +=1
                        Result[Title(HTMLResult)] = Recipe
                        Result[Title(HTMLResult)]["Title"] = ItemFinder["items"][0]["title"]
                    else:
                        for itemish in ind.select(".wds-tab__content"):
                            ws = 0
                            count = 0
                            Recipe = {}
                            if itemish.select(".content") == []:
                                for item in HTMLResult.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe)
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe)
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                            else:
                                for item in itemish.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe) 
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe) 
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                else:
                    if HTMLResult.select(".wds-tab__content") == []:
                        ws = 0
                        count = 0
                        Recipe = {}
                        for item in HTMLResult.select(".content"):
                            if item.select(".content") == []:
                                if not count in require:
                                    Insert(((item.find('th')).text).strip(), Recipe)
                                ws += 1
                            else:
                                meh = ((item.find('th')).text).strip()
                                Recipe[meh] = {}
                                for mes in item.select(".content"):
                                    Insert2(((mes.find('th')).text).strip(), Recipe)
                                    ws += 1
                                    require.append(ws)
                            count +=1
                        Result[Title(HTMLResult)] = Recipe
                        Result[Title(HTMLResult)]["Title"] = ItemFinder["items"][0]["title"]
                    else:
                        for itemish in HTMLResult.select(".wds-tab__content"):
                            ws = 0
                            count = 0
                            Recipe = {}
                            if itemish.select(".content") == []:
                                for item in HTMLResult.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe)
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe)
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                            else:
                                for item in itemish.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe) 
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe) 
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                try:
                    return Result[ItemFinder["items"][0]["title"]]
                except:
                    if NameItem in Result.keys():
                        return Result[NameItem]
                    else:
                        return Result
            except:
                return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 3"})            
        except IndexError:
            return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 2"})
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later. Error Code 1"})

def ItemSprite(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                Result = {}  
                if len(HTMLResult.select(".gtw-card")) == 1:
                    Data = {
                        "Item" :"",
                        "Tree" :"",
                        "Seed" :""
                    }  
                    images = HTMLResult.find('div', {"class": "gtw-card"})
                    Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                    Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                    Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                    try:
                        ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    Result[ItemTitle] = Data
                    Result[ItemTitle]["Title"] = ItemTitle
                else:
                    for HTMLResultTabber in HTMLResult.select(".wds-tab__content"):
                        Data = {
                            "Item" :"",
                            "Tree" :"",
                            "Seed" :""
                        }  
                        images = HTMLResultTabber.find('div', {"class": "gtw-card"})
                        Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                        Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                        Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                        try:
                            ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        Result[ItemTitle] = Data
                        Result[ItemTitle]["Title"] = ItemTitle
                try:
                    return Result[ItemFinder["items"][0]["title"]]
                except:
                    if NameItem in Result.keys():
                        return Result[NameItem]
                    else:
                        return Result
            except:
                return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 3"})            
        except IndexError:
            return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 2"})
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later. Error Code 1"})