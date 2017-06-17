def signup():
    b = raw_input('Host or Guest? ')
    if b == 'Host':
        c = raw_input('Sign in or Sign Up? ')
        if c == 'Sign in':
            username = raw_input('Username = ')
            password = raw_input('Password = ')
            if verify_username_and_password(username, password, database) == "no":
                print "incorrect username, Sign up"
                username = raw_input('Username = ')
                password = raw_input('Password = ')
                database[username] = password
                names[username] = raw_input('Name = ')
                address[username] = raw_input('Address = ')
                max_limit[username] = raw_input('Max Limit of Bags per day = ')
                contact_number[username] = raw_input("Contact number")
                email[username] = raw_input("Email")
                rating[username] = 5
                price[username] = raw_input("price per hour")
                #return database, names, address, max_limit
        else:
            username = raw_input('Username = ')
            password = raw_input('Password = ')
            database[username] = password
            names[username] = raw_input('Name = ')
            address[username] = raw_input('Address = ')
            max_limit[username] = raw_input('Max Limit of Bags per day = ')
            contact_number[username] = raw_input("Contact number")
            email[username] = raw_input("Email")
            current_limit[username] = 0
            rating[username] = 5
            price[username] = raw_input("price per hour")
            #return database, names, address, max_limit
    else:
        print "Sign Up Guest"
        username = raw_input('Username = ')
        password = raw_input('Password = ')
        database[username] = password
        namesguest[username] = raw_input('Name = ')
        currentaddress[username] = raw_input("Current address = ")
        jj = currentaddress[username]
        NumberOfBags[username] = raw_input("NumberOfBags = ")
        numb = NumberOfBags[username]
        suitableusernames = []
        rating[username] = 5
        for username in names:
            p = int(current_limit[username]) + int(numb)
            if p <= int(max_limit[username]):
                print username
                suitableusernames.append(username)
        print len(suitableusernames)
        if len(suitableusernames) > 0:
            rankingoflist(suitableusernames, jj)
            
            


                         
                    

def verify_username_and_password(username, password, database):
    if username in database:
        pass1 = database[username]
    if database[username] == password:
        return "Signed In"
    else:
        return "no"
    
def listprint():
    print "database list"
    print database
    print "names list"
    print names
    print "address list"
    print address
    print "max_limit list"
    print max_limit
    print "email list"
    print email
    print "current_limit list"
    print current_limit
    print "rating"
    print rating


def reverse_geocoding(place):
    import requests
    #place = "amherst massachusetts"
    place = place.replace(" ","+")
    link = 'https://maps.googleapis.com/maps/api/geocode/json?address='+place
    response = requests.get(link)
    resp_json_payload = response.json()
    return resp_json_payload['results'][0]['geometry']['location']['lat'], resp_json_payload['results'][0]['geometry']['location']['lng']

def distance_in_time(place1, place2):
    import simplejson, urllib
    import geopy.distance
    orig_coord = reverse_geocoding(place1)
    dest_coord = reverse_geocoding(place2)
    return geopy.distance.vincenty(orig_coord, dest_coord).km
 
def rankingoflist(usernames, currentguestaddress):
    new_list = {}
    dist = {}
    print "ok"
    for username in usernames:
        host_Address = address[username]
        distance = distance_in_time(host_Address, currentguestaddress)
        dist[username] = distance
        ranking_Score = float(rating[username])*float(distance)*float(price[username])
        ranking_Score = ranking_Score/10
        new_list[username] = ranking_Score
    p = sorted([(value,key) for (key,value) in new_list.items()])
    print "Suggestions listed nearby"
    for u in p:
        x = u[1]
        print "username : " + str(x)
        print "address : " + str(address[x])
        print "contact number : " + str(contact_number[x])
        print "distance from this location : " + str(dist[x])
        print "\n"
    
    
print "Welcome to Bagdrop"
print "----------------------"
database = {}
#database['abc'] = 'xyz'
names = {}
address = {}
max_limit = {}
currentaddress = {}
NumberOfBags = {}
namesguest = {}
current_limit = {}
contact_number = {}
email = {}
rating = {}
price = {}
#current_limit['abc'] = 0
signup()
print "----------------"
print "new list"
print "---------------"
listprint()
