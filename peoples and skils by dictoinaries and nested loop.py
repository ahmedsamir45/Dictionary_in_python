peoples = {

    'Osama': {
       'Html': '70%',
        'Css': '80%',
        'js': '70%' 
     },

    'Ahmed': {
       'Html': '90%',
        'Css': '80%',
        'js': '90%'
    },

    'sayed': {
        'Html': '70%',
        'Css': '60%',
        'js': '90%'
    }
}

#print(peoples['Osama']['Css'])
#for name in peoples:
 #   print(f'skills and progress for {name}Is: {peoples[name]} ')

for name in peoples:
    print(f'skills and progress for {name} Is:  ')
    for skill in peoples[name]:
        print(f'{skill.upper()} => {peoples[name][skill]}')
        
        

 
