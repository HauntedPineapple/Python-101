# https://www.pygame.org/docs/ref/event.html
import math, time, random, os
import pygame
from pygame.locals import *

pygame.init()

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Title')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

clock = pygame.time.Clock()

# Pygame handles all its event messaging through an event queue
# The event queue has an upper limit on the number of events it can hold
# The event queue also offers some simple filtering which can slightly help performance by blocking certain event types from the queue
# Use pygame.event.set_allowed()which events are allowed on the queue and 
# pygame.event.set_blocked() which events are allowed on the queue to change this filtering. 
# By default, all event types can be placed on the queue
# To get the state of various input devices, you can forego the event queue and 
# access the input devices directly with their appropriate modules: 
#   pygame.mouse module to work with the mouse
#       https://www.pygame.org/docs/ref/mouse.html
#   pygame.key module to work with the keyboard
#       https://www.pygame.org/docs/ref/key.html
#   pygame.joystick module for interacting with joysticks, gamepads, and trackballs
#       https://www.pygame.org/docs/ref/joystick.html
#       note: Joysticks will not send any events until the device has been initialized.
# Pygame requires some form of communication with the system window manager and other parts of the platform for this method of event handling
# To keep pygame in sync with the system, you will need to call pygame.event.pump() to keep everything current
# Usually, this should be called once per game loop

# Methods:
# pygame.event.pump()
# note: This function should only be called in the thread that initialized pygame.display
# internally process pygame event handlers
#   pump() -> None

# pygame.event.get()
# note: This function should only be called in the thread that initialized pygame.display
# get events from the queue
#   get(eventtype=None) -> Eventlist
#   get(eventtype=None, pump=True) -> Eventlist

# pygame.event.poll()
# note: This function should only be called in the thread that initialized pygame.display
# get a single event from the queue
#   poll() -> EventType instance

# pygame.event.wait()
# note: This function should only be called in the thread that initialized pygame.display
# wait for a single event from the queue
#   wait() -> EventType instance
#   wait(timeout) -> EventType instance

# pygame.event.peek()
# test if event types are waiting on the queue
#   peek(eventtype=None) -> bool
#   peek(eventtype=None, pump=True) -> bool

# pygame.event.clear()
# remove all events from the queue
#   clear(eventtype=None) -> None
#   clear(eventtype=None, pump=True) -> None

# pygame.event.event_name()
# get the string name from an event id
#   event_name(type) -> string

# pygame.event.set_blocked()
# control which events are allowed on the queue
#   set_blocked(type) -> None
#   set_blocked(typelist) -> None
#   set_blocked(None) -> None

# pygame.event.get_blocked()
# test if a type of event is blocked from the queue
#   get_blocked(type) -> bool
#   get_blocked(typelist) -> bool

# pygame.event.set_allowed()
# control which events are allowed on the queue
#   set_allowed(type) -> None
#   set_allowed(typelist) -> None
#   set_allowed(None) -> None

# pygame.event.set_grab()
# control the sharing of input devices with other applications
#   set_grab(bool) -> None

# pygame.event.get_grab()
# test if the program is sharing input devices
#   get_grab() -> bool

# pygame.event.post()
# place a new event on the queue
#   post(Event) -> None

# pygame.event.custom_type()
# make custom user event type
#   custom_type() -> int

# pygame.event.Event()
# create a new event object
#   Event(type, dict) -> EventType instance
#   Event(type, **attributes) -> EventType instance

while True:
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.KEYUP:
            pass
        
    pygame.display.update()
    clock.tick(60)