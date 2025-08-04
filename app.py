# import random

# subjects =[

# ]



# actions =[
   
# ]

# places_or_things = [
   

# ]

# while True:
#     subject = random.choice(subjects)
#     action = random.choice(actions)
#     place_or_thing = random.choice(places_or_things)

#     headline = F"BREAKING NEWS : {subject} {action} {place_or_thing}"
#     print("\n" + headline)

#     user_input = input("\n Do you want another headline? (yes/no)").strip().lower()
#     if user_input != "yes":
#         break
# print("\n Thank for used fake news generator . have a fun day")

from flask import Flask, render_template
import random

app = Flask(__name__)

subjects = ["Hardik Pandya", "Rakhi Sawant", "Virat Kohli", "Salman Khan", "Narendra Modi", 
    "Hardik Pandya", "Narendra Modi", "Virat Kohli", "Salman Khan", "Elon Musk",
    "Ranveer Singh", "MS Dhoni", "Shah Rukh Khan", "Amit Shah", "Alia Bhatt",
    "Rakhi Sawant", "Sunny Deol", "Kangana Ranaut", "Amitabh Bachchan", "Rahul Gandhi",
    "Arnab Goswami", "Pankaj Tripathi", "Kartik Aaryan", "Kapil Sharma", "Priyanka Chopra",
    "Sachin Tendulkar", "KL Rahul", "Deepika Padukone", "P.V. Sindhu", "Neeraj Chopra",
    "Yogi Adityanath", "Shubman Gill", "Sundar Pichai", "Ratan Tata", "Mukesh Ambani",
    "Sanjay Dutt", "Rajinikanth", "Vicky Kaushal", "Nawazuddin Siddiqui", "Ananya Pandey",
    "Tiger Shroff", "Disha Patani", "Nirmala Sitharaman", "Smriti Irani", "Rohit Sharma",
    "Ajay Devgn", "Baba Ramdev", "Bhuvan Bam", "CarryMinati", "Tanmay Bhat",
    "Kenny Sebastian", "Zakir Khan", "Ashneer Grover", "Bhagat Singh", "Lalu Prasad Yadav",
    "Akshay Kumar", "Anupam Kher", "Jethalal", "Baburao Apte", "Munna Bhai",
    "Circuit", "Biswa Kalyan Rath", "Kunal Kamra", "Harsh Beniwal", "Ravish Kumar",
    "Gautam Adani", "Abdul Kalam", "Chacha Chaudhary", "Tenali Rama", "Birbal",
    "Santa Singh", "Banta Singh", "Arnold Schwarzenegger", "The Rock", "Will Smith",
    "Tony Stark", "Captain Jack Sparrow", "Harry Potter", "Doraemon", "Shinchan",
    "Nobita", "Ash Ketchum", "Pikachu", "Thor", "Loki",
    "Captain America", "Iron Man", "Hulk", "Spiderman", "Doctor Strange",
    "Batman", "Superman", "Joker", "Deadpool", "Venom",
    "Thanos", "Black Panther", "Groot", "Rocket Raccoon", "Ant-Man",
    "Peppa Pig", "Motu", "Patlu", "Chhota Bheem", "Tom",
    "Jerry", "Scooby-Doo", "Johnny Bravo", "Mr. Bean", "Mario"] 
actions = ["debugged", "hacked", "wrestled with", "cooked", "danced on", "debugged", "hacked", "painted", "cooked", "wrestled with", "interviewed",
    "played cricket with", "argued with", "danced on", "slept inside",
    "washed", "chased", "punched", "celebrated", "fought",
    "sang to", "exploded", "meditated on", "licked", "kissed",
    "stared at", "meowed at", "barked at", "slapped", "hugged",
    "kissed goodbye", "zoomed into", "vanished into", "rebooted", "installed",
    "updated", "uninstalled", "deleted", "escaped from", "hired",
    "fired", "watered", "fed", "drew", "climbed",
    "jumped over", "sniffed", "borrowed", "investigated", "mopped",
    "vacuumed", "messed up", "repaired", "scratched", "created",
    "destroyed", "uploaded", "downloaded", "blocked", "followed",
    "unfollowed", "liked", "shared", "stalked", "ignored",
    "forgave", "scanned", "copied", "pasted", "played with",
    "robbed", "insulted", "praised", "challenged", "spammed",
    "googled", "studied", "screamed at", "threw", "ate",
    "drank", "hid in", "teleported to", "tried to sell", "laughed at",
    "danced with", "photo-bombed", "cleaned", "signed", "stole",
    "traded", "offered", "rejected", "drew", "bit",
    "blew up", "squashed", "tickled", "tripped on", "smashed",
    "snored inside", "posed with", "charmed", "adopted", "ran over"]  # Add 100
objects = ["a haunted scooter", "a traffic signal", "a shampoo factory", "a traffic signal", "a refrigerator", "the moon", "a shampoo factory", "a haunted scooter",
    "a coding bootcamp", "a watermelon", "a broken drone", "a washing machine", "a tea stall",
    "a dustbin", "a banana peel", "a rocket", "a flying auto-rickshaw", "a submarine made of paper",
    "a floating chair", "a giant paratha", "a mobile charger", "a vending machine", "a broken AC",
    "a talking mirror", "a power bank", "a baby dinosaur", "a rusted iron", "a book that screams",
    "a haunted house", "a dancing robot", "a marshmallow tower", "a secret lair", "a potato farm",
    "a flying laptop", "a rainbow umbrella", "a pink scooter", "a farting pillow", "a tea cup spaceship",
    "a cricket bat", "a giant teddy bear", "a scary swing", "a teleporting elevator", "a wifi signal",
    "a chocolate volcano", "a haunted keyboard", "a singing guitar", "a fake passport", "a rocket shoe",
    "a salad spaceship", "a milkshake monster", "a traffic cone", "a lost charger", "a cat café",
    "a brain scanner", "a love letter printer", "a broken helmet", "a laughing mirror", "a time machine",
    "a mango missile", "a digital dhol", "a sarcastic Alexa", "a robotic chair", "a twerking toaster",
    "a spaghetti bridge", "a code generator", "a Bluetooth cow", "a neon banana", "a sleeping bag full of ants",
    "a dinosaur costume", "a bubble gun", "a dancing floor mat", "a disco rickshaw", "a mirror maze",
    "a chocolate fridge", "a yogurt bike", "a cow-shaped drone", "a game console", "a flying slipper",
    "a fake currency note", "a monkey-powered scooter", "a spinning coconut", "a microwave oven",
    "a spaghetti fountain", "a laughing statue", "a zoom call trap", "a pillow fort", "a poop emoji pillow",
    "a water bottle bazooka", "a selfie stick bazooka", "a unicorn helmet", "a glittery laptop",
    "a fart-powered rocket", "a flying pan", "a code bug zoo", "a WiFi temple", "a TikTok tripod",
    "a haunted Zoom meeting", "a fish tank classroom", "a sugarcane bazooka", "a coconut router",
    "a bug-ridden software", "a solar powered lassi machine", "a banana laptop", "a pizza spaceship", "a pajama lab"]  # Add 100

@app.route("/")
def home():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    sentence = f"{subject} {action} {obj}."
    return render_template("index.html", sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
