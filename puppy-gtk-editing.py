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
        if self.health < 8:
            self.health += 1

    def decrease_health(self):
        if self.health > 2:
            self.health -= 1
            
    def increase_weight(self):
        if self.weight < 8:
            self.weight += 1

    def decrease_weight(self):
        if self.weight > 2:
            self.weight -= 1
            
    def increase_happy(self):
        if self.happy < 8:
            self.happy += 1

    def decrease_happy(self):
        if self.happy > 2:
            self.happy -= 1

            
print "Please look after me..."
dog = ("""
  _
=O\\\ 
  \____/
  ^    ^ """)

print dog

    
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
        self.disconnect_buttons()
        self.label.set_text("Do you want to give Puppy a cuddle?")
        
        def on_yes(button):
            print "on_yes"
            self.disconnect_buttons()
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Yay! Happiness has increased to " + str(self.pet.happy) + "!" +
" " + u'\U0001F43E')
            elif self.pet.happy == 8:
                self.label.set_text("Yay! Happiness is " + str(self.pet.happy) + " " + u'\U0001F43E')
            self.wait_for_click(self.puppy_day)
            
        def on_no(button):
            print "on_no"
            self.disconnect_buttons()
            self.pet.decrease_happy()
            self.label.set_text("""Are you sure? Puppy really loves cuddles!
Happiness has decreased to """ + str(self.pet.happy) + "!")
            self.wait_for_click(self.puppy_day)

        self.connect_buttons("Yes", on_yes, "No", on_no)
    

    def hungry(self):
        self.disconnect_buttons()
        self.label.set_text("""I'm hungry, feed me!
Would you like to feed puppy?""")

        def on_yes(button):
            print "on_yes"
            self.disconnect_buttons()
            if self.pet.weight < 8:
                self.pet.increase_weight()
                self.label.set_text("""Yay! nomnomnom
Weight has increased to """ + str(self.pet.weight) + "!" + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            elif self.pet.weight == 8:
                self.label.set_text("""Yay! nomnomnom
Weight is """ + str(self.pet.weight) + "!" +  " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            
        def on_no(button):
            print "on_no"
            self.disconnect_buttons()
            self.pet.decrease_weight()
            self.label.set_text("""Aww, still hungry puppy
Weight has decreased to """ + str(self.pet.weight))
            self.wait_for_click(self.puppy_day)

        self.connect_buttons("Yes", on_yes, "No", on_no)
        

    def play_stick(self):
        self.disconnect_buttons()
        self.label.set_text("Would you like to play a game with me?")
        self.exercised = 0

        def on_yes(*args):
            print "on_yes"
            self.disconnect_buttons()
            self.label.set_text("Yay! Let's play with the stick! Can you throw it for me?!")

            def little_throw(button):
                print "little"
                self.disconnect_buttons()
                self.label.set_text("""Little throw
Yay caught it, again, again!""")
                self.exercised += 2
                self.wait_for_click(on_yes)
                
            def big_throw(button):
                print "big"
                self.disconnect_buttons()
                self.label.set_text("""Big throw
.......... Woah, that was a long way, not tired yet though!""")
                self.exercised += 3
                self.wait_for_click(on_yes)

            if (self.exercised < 6):
                self.connect_buttons("Little throw", little_throw, "Big throw", big_throw)
                
            else:
                self.label.set_text("")
                
                if self.pet.health < 8:
                    self.pet.increase_health()
                    self.label.set_text("""That's enough running around now
Health has increased to """ + str(self.pet.health) + "!" + " " + u'\U0001F43E')
                    self.wait_for_click(self.puppy_day)
            
                elif self.pet.health == 8:
                    self.label.set_text("Health is " + str(self.pet.health) + " " + u'\U0001F43E')
                    self.wait_for_click(self.puppy_day)
            
        def on_no(button):
            print "on_no"
            self.disconnect_buttons()
            self.pet.decrease_health()
            self.label.set_text("Health has decreased to " + str(self.pet.health))
            self.wait_for_click(self.puppy_day)

        self.connect_buttons("Yes", on_yes, "No", on_no)

        
    def sleep(self):
        self.disconnect_buttons()
        self.label.set_text("Would you like to put Puppy to bed?")

        def on_yes(*args):
            print "on_yes"
            self.disconnect_buttons()
            self.pet.increase_health()
            if self.pet.health < 8:
                self.label.set_text("Health has increased to " + str(self.pet.health) + """!
Zzzzzz...Zzzzzz...Puppy still sleeping...""" + " " + u'\U0001F43E')
                
            elif self.pet.health == 8:
                self.label.set_text("Health is " + str(self.pet.health) + """
Zzzzzz...Zzzzzz...Puppy still sleeping...""" + " " + u'\U0001F43E')

            def wake_up(button):
                print "wake up"
                self.disconnect_buttons()
                self.label.set_text("Time for Puppy to wake up now!")
                self.wait_for_click(self.puppy_day)

            self.connect_buttons("", None, "Okay", wake_up)                                
            
        def on_no(button):
            print "on_no"
            self.disconnect_buttons()
            self.pet.decrease_health()
            self.label.set_text("""Are you sure? Puppy is so sleepy
Health has decreased to """ + str(self.pet.health))
            def no_sleep(button):
                print "no_sleep"
                self.disconnect_buttons()
                self.label.set_text("But Puppy is sleepy!")
                self.wait_for_click(self.puppy_day)
            
            def yes_sleep(button):
                print "yes_sleep"
                self.disconnect_buttons()
                self.label.set_text("Sleep time now")
                self.wait_for_click(on_yes)

            self.connect_buttons("Yes", no_sleep, "No", yes_sleep)

        self.connect_buttons("Yes", on_yes, "No", on_no)


    def chase_tail(self):
        self.disconnect_buttons()
        self.label.set_text("Puppy is having lots of fun chasing his tail...can't quite catch it!")

        def chase(button):
            print "chase"
            self.disconnect_buttons()
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!" + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy) + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            
        self.connect_buttons(None, None, "Chase tail", chase)

    def toilet_time(self):
        self.disconnect_buttons()
        self.label.set_text("Oops, Puppy needed the toilet...please clean up!")
        
        def on_yes(button):
            print "on_yes"
            self.disconnect_buttons()
            self.label.set_text("Puppy feels much better now")
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!" + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy) + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
                
        def on_no(button):
            print "on_no"
            self.disconnect_buttons()
            self.pet.decrease_happy()
            self.label.set_text("""But not cleaning up will make Puppy sick
Happiness has decreased to """ + str(self.pet.happy))
            self.wait_for_click(self.puppy_day)
            

        self.connect_buttons("Yes", on_yes, "No", on_no)
         
    def car_journey(self):
        self.disconnect_buttons()
        self.label.set_text("""Come on Puppy, time for a ride in the car
Let's wind down the window""")
        
        def on_yes(button):
            print "on_yes"
            self.disconnect_buttons()
            self.label.set_text("Yay, Puppy loves looking out of the window!")
            self.pet.increase_happy()
            if self.pet.happy < 8:
                self.label.set_text("Happiness has increased to " + str(self.pet.happy) + "!" + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            elif self.pet.happy == 8:
                self.label.set_text("Happiness is " + str(self.pet.happy) + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)

        self.connect_buttons(None, None, "Yes", on_yes)

    def walk(self):
        self.disconnect_buttons()
        self.label.set_text("Would Puppy like to go for a walk?")

        def on_yes(button):
            print "on_yes"
            self.disconnect_buttons()
            self.label.set_text("Yay! Off we go...")
            self.pet.increase_health()
            if self.pet.health < 8:
                self.label.set_text("Health has increased to " + str(self.pet.health) + "!" + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
            elif self.pet.health == 8:
                self.label.set_text("Health is " + str(self.pet.health) + " " + u'\U0001F43E')
                self.wait_for_click(self.puppy_day)
        def on_no(button):
            self.disconnect_buttons()
            self.pet.decrease_health()
            self.label.set_text("""Oh, but Puppy needs his exercise!
Health has decreased to """ + str(self.pet.health))
            self.wait_for_click(self.puppy_day)

        self.connect_buttons("Yes", on_yes, "No", on_no)
            

    def puppy_day(self):
        import random
        day = [self.hungry, self.play_stick, self.sleep, self.toilet_time, self.cuddles, self.walk, self.chase_tail, self.car_journey]
        random.choice(day)()

        
    def disconnect_buttons(self):
        if self.button1_connection > 0:
            self.button1.disconnect(self.button1_connection)
            self.button1_connection = 0
        if self.button2_connection > 0:
            self.button2.disconnect(self.button2_connection)
            self.button2_connection = 0

    def connect_buttons(self, label1, func1, label2, func2):
        self.disconnect_buttons()
        if label1:
            self.button1.set_sensitive(True)
            self.button1.set_label(label1)
        else:
            self.button1.set_sensitive(False)
            self.button1.set_label("")
            
        if func1:
            self.button1_connection = self.button1.connect("clicked", func1)
            
        if label2:
            self.button2.set_sensitive(True)
            self.button2.set_label(label2)
        else:
            self.button2.set_sensitive(False)
            self.button2.set_label("")
            
        if func2:
            self.button2_connection = self.button2.connect("clicked", func2)
        

    def wait_for_click(self, okay_function):
        def on_okay(button):
            self.disconnect_buttons()
            okay_function()            
        self.connect_buttons("", None, "Okay", on_okay)
        
window = MyWindow()

gtk.main()

    




        
