

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
actions = ["danced on", "hugged", "slapped", "licked", "argued with",
    "screamed at", "sang to", "tickled", "ran over", "kissed",
    "ate", "drank", "photo-bombed", "posed with", "googled",
    "debugged", "hacked", "wrestled with", "teleported to", "stole",
    "laughed at", "spammed", "ignored", "hid inside", "rode",
    "washed", "snored inside", "borrowed", "jumped over", "investigated"]

objects = [ "a fart-powered rocket", "a haunted scooter", "a giant samosa", "a dancing robot",
    "a banana laptop", "a talking mirror", "a poop emoji pillow", "a flying slipper",
    "a shampoo factory", "a watermelon", "a WiFi temple", "a chocolate volcano",
    "a spaghetti fountain", "a unicorn helmet", "a banana peel", "a rocket shoe",
    "a farting pillow", "a disco rickshaw", "a sugarcane bazooka", "a pizza spaceship",
    "a potato farm", "a neon banana", "a laughing statue", "a time machine", "a tea cup spaceship", "a pajama lab"]  

@app.route("/")
def home():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    sentence = f"{subject} {action} {obj}."
    return render_template("index.html", sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)

