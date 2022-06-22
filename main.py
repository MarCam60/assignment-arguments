# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line





def greet ( name, greeting_template = "Hello, <name>!" ):
    x = greeting_template. replace ("<name>",name)
    
    return (x)

greet ("Doc")
greet ( "Bob", "What's up, <name>!")






def force (mass, body = 'earth'):
    
    bodies = {'sun': 274, 'jupiter':24.9, 'neptune':11.2, 'saturn':10.4, 'earth':9.8, 'uranus':8.9, 'venus':8.9, 'mars':3.7, 'mercury':3.7, 'moon':1.6, 'pluto':0.6}
       
    return mass * bodies[body]
 

print (force (0.98, 'jupiter'))

G= 6.674*10**-11

def pull (m1,m2,d):
    return (G *(m1*m2)* (d**-2))

print (pull(800,1500,3))   