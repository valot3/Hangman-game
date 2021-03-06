def level_template(lvl_number):
       print("""
       \t====================    LEVEL {}    ====================
       """.format(lvl_number))
   

def main_template():
    print("""
    \t     _   _                                          
    \t    | | | |                                         
    \t    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __   
    \t    |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
    \t    | | | | (_| | | | | (_| | | | | | | (_| | | | | 
    \t    \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
    \t                        __/ |                       
    \t                       |___/                        
    """)


hangman_pics = {
    '0' : '''                  
\t           +-----------+     
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________                    
''',
    '1' : '''       
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________                           
''',
    '2' : '''       
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t           |           |       
\t           |           |       
\t           |           |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________                    
''',
    '3' : '''       
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t         / |           |       
\t        /  |           |       
\t       /   |           |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________                       
''',
    '4' : '''       
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t         / | \         |       
\t        /  |  \        |       
\t       /   |   \       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________       
''', 
    '5' : '''                        
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t         / | \         |       
\t        /  |  \        |       
\t       /   |   \       |       
\t          /            |       
\t         /             |       
\t        /              |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________       
''', 
    '6' : '''       
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t         / | \         |       
\t        /  |  \        |       
\t       /   |   \       |       
\t          / \          |       
\t         /   \         |       
\t        /     \        |       
\t                       |       
\t                       |       
\t                       |       
\t    ___________________________
\t    ___________________________       
''',
    'you_lost' : ''' 
\t           +-----------+      
\t           |           |       
\t           |           |       
\t           |           |       
\t           |           |       
\t           _           |       
\t          / \          |       
\t          \_/          |       
\t         / | \         |       
\t        /  |  \        |       
\t       /   |   \       |       
\t          / \          |       
\t         /   \         |       
\t        /     \        |       
\t                       |       
\t                       |       
\t                       |       
\t                  /_________
\t                 / _________
\t                /           
\t               /            
\t              /             
\t             /              
\t            /               
\t           /                
\t          /                 
''',
    'you_won' : """       
\t           +-----------+      
\t           |           |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t                       |       
\t      \    _    /      |       
\t       \  / \  /       |       
\t        \ \_/ /        |       
\t         \ | /         |       
\t           |           |       
\t           |           |       
\t          / \          |       
\t         /   \         |       
\t        /     \        |       
\t    ___________________________
\t    ___________________________                           
"""
  }





                                      
