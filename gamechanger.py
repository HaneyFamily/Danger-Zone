import webbrowser
import os
import time
import sys
from datetime import datetime

# the html code which will go in the file
html_template = """
// a key map of allowed keys
var allowedKeys = {
  37: 'left',
  38: 'up',
  39: 'right',
  40: 'down',
  65: 'a',
  66: 'b'
};

// the 'official' Konami Code sequence
var konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

// a variable to remember the 'position' the user has reached so far.
var konamiCodePosition = 0;

// add keydown event listener
document.addEventListener('keydown', function(e) {
  // get the value of the key code from the key map
  var key = allowedKeys[e.keyCode];
  // get the value of the required key from the konami code
  var requiredKey = konamiCode[konamiCodePosition];

  // compare the key with the required key
  if (key == requiredKey) {

    // move to the next key in the konami code sequence
    konamiCodePosition++;

    // if the last key is reached, activate cheats
    if (konamiCodePosition == konamiCode.length) {
      activateCheats();
      konamiCodePosition = 0;
    }
  } else {
    konamiCodePosition = 0;
  }
});

function activateCheats() {
  alert("cheats activated");
  localStorage.setItem("money", 999999999)
  localStorage.setItem("health", 500000)
  localStorage.setItem("level", 100)
  localStorage.setItem("armor 1", 10000)
  localStorage.setItem("armor 2", 10000)
  localStorage.setItem("armor 3", 10000)
  localStorage.setItem("armor 4", 10000)
let money = localStorage.getItem("money")
let health = localStorage.getItem("health")
let level = localStorage.getItem("level")
let a1 = localStorage.getItem("armor 1")
let a2 = localStorage.getItem("armor 2")
let a3 = localStorage.getItem("armor 3")
let a4 = localStorage.getItem("armor 4")
let war = localStorage.getItem("Warrior");
console.log(war);
moneyuser.value = money;
heartsuser.value = health;
}
"""

time_template = """
function Time() {
 // Creating object of the Date class
 var date = new Date();
 // Get current hour
 var hour = date.getHours();
 // Get current minute
 var minute = date.getMinutes();
 // Get current second
 var second = date.getSeconds();
 // Variable to store AM / PM
 var period = "";
 // Assigning AM / PM according to the current hour
 if (hour >= 12) {
 period = "PM";
 } else {
 period = "AM";
 }
 // Converting the hour in 12-hour format
 if (hour == 0) {
 hour = 12;
 } else {
 if (hour > 12) {
 hour = hour - 12;
 }
 }
 // Updating hour, minute, and second
 // if they are less than 10
 hour = update(hour);
 minute = update(minute);
 second = update(second);
 // Adding time elements to the div
 document.getElementById("digital-clock").innerText = hour + " : " + minute + " : " + second + " " + period;
 // Set Timer to 1 sec (1000 ms)
 setTimeout(Time, 1000);
}
 // Function to update time elements if they are less than 10
 // Append 0 before time elements if they are less than 10
function update(t) {
 if (t < 10) {
 return "0" + t;
 }
 else {
 return t;
 }
}
Time();
"""

def installCheats():
    # to open/create a new html file in the write mode
    f = open('Cheat Code.js', 'w')
    # writing the code into the file
    f.write(html_template)  
    # close the file
    f.close()
    print("Cheats Installed")

def uninstallCheats():
    # to open/create a new html file in the write mode
    f = open('Cheat Code.js', 'w')
    # writing the code into the file
    f.write("")  
    # close the file
    f.close()
    print("Cheats Uninstalled")

def openGame():
    # 1st method how to open html files in chrome using
    filename = 'file:///'+os.getcwd()+'/' + 'Danger Zone.html'
    webbrowser.open_new_tab(filename)

def close():
    quit()

def installTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("The time is ", current_time)
    f = open('Time.js', 'w')
    f.write(time_template)
    f.close()
    print("Time Installed")

def uninstallTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("The time is ", current_time)
    f = open('Time.js', 'w')
    f.write("")
    f.close()
    print("Time Uninstalled")

def installSignIn(passcode, oldPassword):
    f = open('Password.txt', 'r')
    contents = f.read()
    f.close()
    if (contents == oldPassword):
        f = open('Password.txt', 'w')
        f.write(passcode)
        f.close()
        passwordtemp = """
        passinput = prompt("Password:", "Quit")
        if (passinput === """ + "'" + passcode + "'" """) {
        } else if (passinput === "Quit") {
        self.close();
        } else {
        window.location.reload();
        }
        """
        f = open('Password.js', 'w')
        f.write(passwordtemp)
        f.close()
        print("Password Set")
    else:
        print("Wrong Password")

def uninstallSignIn(oldPasscode):
    f = open('Password.txt', 'r')
    contents = f.read()
    f.close()
    if (contents == oldPasscode):
        f = open('Password.txt', 'w')
        f.write("")
        f.close()
        f = open('Password.js', 'w')
        f.write("")
        f.close()
        print("Password uninstalled")
    else:
        print("Wrong Password")

def inputer():
    x = input(">> ")
    if (x == "install cheats"):
        installCheats()
    
    elif (x == "uninstall cheats"):
        uninstallCheats()
        
    elif (x == "open game"):
        openGame()
        
    elif (x == "close"):
        close()
        
    elif (x == "install time"):
        installTime()
        
    elif (x == "uninstall time"):
        uninstallTime()
        
    elif (x == "install sign in"):
        x1 = input("Password : ")
        x3 = input("Old Password (Put Nothing If There is No Password In Place) : ")
        installSignIn(x1, x3)
        
    elif (x == "uninstall sign in"):
        x1 = input("Password : ")
        uninstallSignIn(x1)

    elif (x == "189756423arbvk59"):
        print("Please don't close...")
        print("This might take a little while...")
        time.sleep(2)
        uninstallCheats()
        print("Uninstalled Cheats")
        time.sleep(2)
        f = open('Password.txt', 'w')
        f.write("")
        f.close()
        f = open('Password.js', 'w')
        f.write("")
        f.close()
        print("Password uninstalled")
        time.sleep(2)
        uninstallTime()
        print("Time Uninstalled")
        print("Almost Done...")
        time.sleep(5)
        print("Good Bye!")
        time.sleep(2)
        f = open('gamechanger.py', 'w')
        f.write("")
        f.close()
        sys.exit()
        
    else:
        print("Unknown statment", '"', x, '"')
    
    x2 = input("New Input? : ")
    if (x2 == "yes"):
        inputer()
    else:
        close()
inputer()
