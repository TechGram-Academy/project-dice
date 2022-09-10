import random 

dice_faces = (
'''
        ┌─────────┐
        │         │
        │    ●    │
        │         │
        └─────────┘
''',
'''  
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘
''',  
''' 
        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘
''',
''' 
        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘
''',
'''
        ┌─────────┐
        │  ●   ●  │ 
        │    ●    │ 
        │  ●   ●  │ 
        └─────────┘ 
''',
'''
         ┌─────────┐ 
         │  ●   ●  │ 
         │  ●   ●  │ 
         │  ●   ●  │ 
         └─────────┘ 
'''
)

def get_dice(num=1):
    for dice in range(0, num):
        print(random.choice(dice_faces))

