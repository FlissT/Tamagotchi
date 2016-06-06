#copy of pet file for editing
import gtk
from random import randint

class Pet(object):
    condition = "Happy puppy"

    def __init__(self, animal, name, age, weight, health, happy):
        self.animal = animal
        self.name = name
        self.age = age
        self.weight = weight
        self.health = health
        self.happy = happy
        

    def my_pet(self): 
        return "Hello! My name is " + self.name + " " + "and I am your pet, a " + str(self.age) + " old "  + self.animal + "!"

    def wellbeing(self):
        return "My weight is " + str(self.weight) + " " + ", I have " + str(self.health) + " health points and " + str(self.happy) + " happy points."
        
    def increase_health(self):
        if self.health <8:
            self.health +=1

    def decrease_health(self):
        if self.health >2:
            self.health -=1
            
    def increase_weight(self):
        if self.weight <8:
            self.weight +=1

    def decrease_weight(self):
        if self.weight >2:
            self.weight -=1
            
    def increase_happy(self):
        if self.happy <8:
            self.happy +=1

    def decrease_happy(self):
        if self.happy >2:
            self.happy -=1

            
my_pet = Pet("dog", "Puppy", "6 month", 5, 5, 5)
print my_pet.my_pet()
print my_pet.wellbeing()

print "Please look after me..."
dog = ("""
  _
=O\\\ 
  \____/
  ^    ^ """)

print dog
print u'\U0001F43E' #inserts pawprint unicode emoji, but not in linux


def feed():
    return randint(1,4)

def hungry():
    if feed() <= 2:
        print my_pet.condition    
    else:
        print "I'm hungry, feed me!"
        food = str(raw_input("Would you like to feed puppy? y/n "))
        if food == "y":
            print "Yay! nomnomnom"
            my_pet.increase_weight()
            if my_pet.weight < 8:
                print "Weight has increased to " + str(my_pet.weight) + "!"
            elif my_pet.weight == 8:
                print "Weight is " + str(my_pet.weight)
            print my_pet.condition
            print dog
        else:
            print "Aww, still hungry puppy :-( "
            my_pet.decrease_weight()
            print "Weight has decreased to " + str(my_pet.weight)


def play_stick():
    playtime = str(raw_input("Would you like to play a game with me? y/n "))
    if playtime == "y":
        print "Yay! Let's play with the stick! Can you throw it for me?!" 
        throw = str(raw_input("Press l for a little throw or press b for a big throw... "))
        if throw == "l":
            print "... Yay caught it, again, again!"
            print str(raw_input("Press l for a little throw or press b for a big throw... "))
            print "... Yay caught it, again, again!"
            print str(raw_input("Press l for a little throw or press b for a big throw... ")) 
        if throw == "b":
            print ".......... Woah, that was a long way, not tired yet though!"
            throw = str(raw_input("Press l for a little throw or press b for a big throw... "))

        my_pet.increase_health()
        if my_pet.health < 8:
            print "Health has increased to " + str(my_pet.health) + "!"
        elif my_pet.health == 8:
            print "Health is " + str(my_pet.health)
    else:
        my_pet.decrease_health()
        print "Health has decreased to " + str(my_pet.health)


def sleep(): 
    sleeptime = str(raw_input("Would you like to put Puppy to bed? y/n "))
    if sleeptime == "y":
        my_pet.increase_health()
        if my_pet.health < 8:
            print "Health has increased to " + str(my_pet.health) + "!"
        elif my_pet.health == 8:
            print "Health is " + str(my_pet.health)
        sleepy = "Zzzzzz...Zzzzzz..." + str(raw_input("Puppy still sleeping...(y) "))
        print sleepy
        print "Time for Puppy to wake up now!"
    else:
        print "Are you sure? Puppy is so sleepy"
        my_pet.decrease_health()
        print "Health has decreased to " + str(my_pet.health)

                            
def toilet_time():
    toilet = str(raw_input("Oops, Puppy needed the toilet...press y to clean up "))
    if toilet == "y":
        my_pet.increase_happy()
        if my_pet.happy < 8:
            print "Happiness has increased to " + str(my_pet.happy) + "!"
        elif my_pet.happy == 8:
            print "Happiness is " + str(my_pet.happy)
        print my_pet.condition
        print dog
    else:
        my_pet.decrease_happy()
        print "Happiness has decreased to " + str(my_pet.happy)
        


def cuddles():
    cuddle = str(raw_input("Puppy loves cuddles...would you like to give Puppy a cuddle? y/n "))
    if cuddle == "y":
        my_pet.increase_happy()
        if my_pet.happy < 8:
            print "Happiness has increased to " + str(my_pet.happy) + "!"
        elif my_pet.happy == 8:
            print "Happiness is " + str(my_pet.happy)
        print my_pet.condition
        print dog   
    else:
        print "Are you sure? Puppy really loves cuddles!"
        my_pet.decrease_happy()
        print "Happiness has decreased to " + str(my_pet.happy) + "!"

def chase_tail():
    print "Puppy is having lots of fun chasing his tail...can't quite catch it!"
    my_pet.increase_happy()
    if my_pet.happy < 8:
        print "Happiness has increased to " + str(my_pet.happy) + "!"
    elif my_pet.happy == 8:
        print "Happiness is " + str(my_pet.happy)
    print my_pet.condition   
    print dog
    
def car_journey():
    print "Come on Puppy, time for a ride in the car!"
    window = str(raw_input("Press w to wind down the window "))
    if window == "w":
        print "Yay, Puppy loves looking out of the window!"
        my_pet.increase_happy()
        if my_pet.happy < 8:
            print "Happiness has increased to " + str(my_pet.happy) + "!"
        elif my_pet.happy == 8:
            print "Happiness is " + str(my_pet.happy)
        print my_pet.condition   
        print ("""
  //
=O\ 
  \____/
  ^    ^ """)
    else:
        my_pet.decrease_happy()
        print "Happiness has decreased to " + str(my_pet.happy) + "!"
        
import random
def puppy_life():
    life = [hungry, play_stick, toilet_time, cuddles, chase_tail, car_journey]
    for x in range(10):
        lf = random.choice(life)
        lf()
    sleep()
    for x in range(5):
        lf = random.choice(life)
        lf()
    

#puppy_life()             
    
class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.pet = Pet("dog", "Puppy", "6 month", 5, 5, 5)
        self.button1_connection = 0
        self.button2_connection = 0
        
        self.set_title(self.pet.name)
        self.label = gtk.Label(self.pet.my_pet()) 
        self.button1 = gtk.Button()
        self.button2 = gtk.Button()

        vbox = gtk.VBox()
        bbox = gtk.HButtonBox()
        bbox.add(self.button1)
        bbox.add(self.button2)
        vbox.add(self.label)
        vbox.add(bbox)
        self.add(vbox)
        
        self.show_all()
        self.connect("delete-event", self.on_quit)

        self.wait_for_click(self.puppy_day)


    def on_quit(self, widget, event):
        gtk.main_quit()

    def cuddles(self):
        self.label.set_text("Do you want to give Puppy a cuddle?")


        def on_yes(button):
            self.disconnect_buttons()
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!")
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy))
            self.wait_for_click(self.puppy_day)
    

        def on_no(button):
            self.disconnect_buttons()
            self.label.set_text("Are you sure? Puppy really loves cuddles!")
            self.pet.decrease_happy()
            self.label.set_text("Happiness has decreased to " + str(self.pet.happy) + "!")
            self.wait_for_click(self.puppy_day)

        self.button1.set_label("Yes")
        self.button1_connection = self.button1.connect("clicked", on_yes)

        self.button2.set_label("No")
        self.button2_connection = self.button2.connect("clicked", on_no)

    def puppy_day(self):
        #self.cuddles()
        #self.hungry()
        #self.play_stick()
        self.sleep()
        #self.chase_tail()
        #self.toilet_time()
        #self.car_journey()
    
        
    def feed():
        return randint(1,4)

    def hungry(self):
        if feed() <= 2:
            self.label.set_text(self.pet.condition)
            self.wait_for_click(self.puppy_day)
            return 
        
        self.label.set_text("""I'm hungry, feed me!
Would you like to feed puppy?""")

        def on_yes(button):
            self.disconnect_buttons()
            if self.pet.weight < 8:
                self.pet.increase_weight()
                self.label.set_text("""Yay! nomnomnom
Weight has increased to """ + str(self.pet.weight) + "!""")
                self.wait_for_click(self.puppy_day)
                return
            elif self.pet.weight == 8:
                self.label.set_text("""Yay! nomnomnom
Weight is """ + str(self.pet.weight) + "!""")
                self.wait_for_click(self.puppy_day)
            
        def on_no(button):
            self.disconnect_buttons()
            self.pet.decrease_weight()
            self.label.set_text("""Aww, still hungry puppy :-(
Weight has decreased to """ + str(self.pet.weight))
            self.wait_for_click(self.puppy_day)

        self.button1.set_label("Yes")
        self.button1_connection = self.button1.connect("clicked", on_yes)

        self.button2.set_label("No")
        self.button2_connection = self.button2.connect("clicked", on_no)
        

    def play_stick(self):
        self.disconnect_buttons()
        self.label.set_text("Would you like to play a game with me?")
        self.exercised = 0

        def on_yes(*kwargs):
            self.disconnect_buttons()
            self.label.set_text("Yay! Let's play with the stick! Can you throw it for me?!")

            def little_throw(button):
                self.disconnect_buttons()
                self.label.set_text("""Little throw
Yay caught it, again, again!""")
                self.exercised += 2
                self.wait_for_click(on_yes)
                
            def big_throw(button):
                self.disconnect_buttons()
                self.label.set_text("""Big throw
.......... Woah, that was a long way, not tired yet though!""")
                self.exercised += 3
                self.wait_for_click(on_yes)

            if (self.exercised < 6):
                self.button1.set_label("Little throw")
                self.button1_connection = self.button1.connect("clicked", little_throw)

                self.button2.set_label("Big throw")
                self.button2_connection = self.button2.connect("clicked", big_throw)
            else:
                self.label.set_text("")
                
                if self.pet.health < 8:
                    self.pet.increase_health()
                    self.label.set_text("""That's enough running around now
Health has increased to """ + str(self.pet.health) + "!")
                    self.wait_for_click(self.puppy_day)
            
                elif self.pet.health == 8:
                    self.label.set_text("Health is " + str(self.pet.health))
                    self.wait_for_click(self.puppy_day)
            

        def on_no(button):
            self.disconnect_buttons()
            self.pet.decrease_health()
            self.label.set_text("Health has decreased to " + str(self.pet.health))
                
            self.wait_for_click(self.puppy_day)

        self.button1.set_label("Yes")
        self.button1_connection = self.button1.connect("clicked", on_yes)

        self.button2.set_label("No")
        self.button2_connection = self.button2.connect("clicked", on_no)

        

    def sleep(self):
        self.label.set_text("Would you like to put Puppy to bed?")

        def on_yes(button):
            print("on_yes")
            self.disconnect_buttons()
            self.pet.increase_health()
            if self.pet.health < 8:
                self.label.set_text("Health has increased to " + str(self.pet.health) + """!
Zzzzzz...Zzzzzz...Puppy still sleeping...""")
                
            elif self.pet.health == 8:
                self.label.set_text("Health is " + str(self.pet.health) + """
Zzzzzz...Zzzzzz...Puppy still sleeping...""")
            self.wait_for_click(self.puppy_day)

            def wake_up(*kwargs):
                print("wake_up")
                self.disconnect_buttons()
                self.label.set_text("Time for Puppy to wake up now!")
                self.wait_for_click(self.puppy_day)

            self.wait_for_click(wake_up)
            self.button2.set_label("Okay")
            self.button2_connection = self.button2.connect("clicked", on_yes)                             
            
            
        def on_no(button):
            print("on_no")
            self.disconnect_buttons()
            self.pet.decrease_health()
            self.label.set_text("""Are you sure? Puppy is so sleepy
Health has decreased to """ + str(self.pet.health))
            def no_sleep(button):
                print("no_sleep")
                self.disconnect_buttons()
                self.label.set_text("But Puppy is sleepy!")
                #self.wait_for_click(no_sleep)
                self.wait_for_click(self.puppy_day)
            
            def yes_sleep(button):
                print("yes_sleep")
                self.disconnect_buttons()
                self.label.set_text("Sleep time now")
                self.wait_for_click(yes_sleep)
            self.wait_for_click(self.sleep)

            self.button1.set_label("Yes")
            self.button1_connection = self.button1.connect("clicked", no_sleep)

            self.button2.set_label("No")
            self.button2_connection = self.button2.connect("clicked", yes_sleep)
            

        self.button1.set_label("Yes")
        self.button1_connection = self.button1.connect("clicked", on_yes)

        self.button2.set_label("No")
        self.button2_connection = self.button2.connect("clicked", on_no)


    def chase_tail(self):
        self.label.set_text("Puppy is having lots of fun chasing his tail...can't quite catch it!")
        def chase_tail(button):
            self.disconnect_buttons()
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!")
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy))
                self.wait_for_click(self.puppy_day)
            
        self.button2.set_label("Chase tail")
        self.button2_connection = self.button2.connect("clicked", chase_tail)

    def toilet_time(self):
        self.label.set_text("Oops, Puppy needed the toilet...please clean up!")
        
        def on_yes(button):
            self.disconnect_buttons()
            self.label.set_text("Puppy feels much better now")
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!")
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy))
                self.wait_for_click(self.puppy_day)
                
        def on_no(button):
            self.disconnect_buttons()
            self.pet.decrease_happy()
            self.label.set_text("""But not cleaning up will make Puppy sick :-(
Happiness has decreased to """ + str(self.pet.happy))
            self.wait_for_click(self.puppy_day)
            

        self.button1.set_label("Yes")
        self.button1_connection = self.button1.connect("clicked", on_yes)

        self.button2.set_label("No")
        self.button2_connection = self.button2.connect("clicked", on_no)
         
    def car_journey(self):
        self.label.set_text("""Come on Puppy, time for a ride in the car
let's wind down the window""")
        
        def on_yes(button):
            self.disconnect_buttons()
            self.label.set_text("Yay, Puppy loves looking out of the window!")
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!")
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy))
                self.wait_for_click(self.puppy_day)
        self.wait_for_click(self.puppy_day)

    
        self.button2.set_label("Yes")
        self.button2_connection = self.button2.connect("clicked", on_yes)

        self.button1.set_label("")
        

    def disconnect_buttons(self):
        if self.button1_connection > 0:
            self.button1.disconnect(self.button1_connection)
            self.button1_connection = 0
        if self.button2_connection > 0:
            self.button2.disconnect(self.button2_connection)
            self.button2_connection = 0

    def wait_for_click(self, okay_function):
        self.button1.set_label("")

        def on_okay(button):
            self.disconnect_buttons()
            okay_function()            

        self.button2.set_label("Okay")
        self.button2_connection = self.button2.connect("clicked", on_okay)
        
window = MyWindow()

gtk.main()

    




        
