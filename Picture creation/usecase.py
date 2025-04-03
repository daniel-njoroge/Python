from graphviz import Digraph

# Create Use Case Diagram
use_case = Digraph('Use_Case_Diagram', format='png')
use_case.attr(rankdir='LR')

# Actors
use_case.node('Student', shape='ellipse', style='filled', fillcolor='lightblue')
use_case.node('Tutor', shape='ellipse', style='filled', fillcolor='lightgreen')
use_case.node('Parent', shape='ellipse', style='filled', fillcolor='lightcoral')

# Use Cases
use_case.node('Register', shape='box')
use_case.node('Login', shape='box')
use_case.node('Logout', shape='box')
use_case.node('View Materials', shape='box')
use_case.node('Rate Materials', shape='box')
use_case.node('Post Content', shape='box')
use_case.node('View Ratings', shape='box')
use_case.node('View Payments', shape='box')
use_case.node('Withdraw', shape='box')
use_case.node('Make Payment', shape='box')
use_case.node('View Student Usage', shape='box')

# Associations
use_case.edge('Student', 'Register')
use_case.edge('Tutor', 'Register')
use_case.edge('Parent', 'Register')

use_case.edge('Student', 'Login')
use_case.edge('Tutor', 'Login')
use_case.edge('Parent', 'Login')

use_case.edge('Student', 'Logout')
use_case.edge('Tutor', 'Logout')
use_case.edge('Parent', 'Logout')

use_case.edge('Student', 'View Materials')
use_case.edge('Student', 'Rate Materials')

use_case.edge('Tutor', 'Post Content')
use_case.edge('Tutor', 'View Ratings')
use_case.edge('Tutor', 'View Payments')
use_case.edge('Tutor', 'Withdraw')

use_case.edge('Parent', 'Make Payment')
use_case.edge('Parent', 'View Student Usage')

# Render Diagram
use_case_path = r"C:\Users\USER\Desktop\Python\Picture creation\use_case_diagram"
use_case.render(use_case_path)
