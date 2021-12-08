from random import randint
import os

# [lower bound, upper bound]
age = [25, 65]
# list of possible locations
location = ['Dickson, ACT', 'Franklin, ACT', 'Acton, ACT', 'Ainslie, ACT', 'Braddon, ACT',
            'Campbell, ACT', 'Downer, ACT', 'Hackett, ACT', 'Lyneham, ACT', 'Reid, ACT',
            'Turner, ACT', 'Watson, ACT', 'Barton, ACT', 'Deakin, ACT', 'Forrest, ACT',
            'Kingston, ACT', 'Griffith, ACT', 'Narrabundah, ACT', 'Red Hill, ACT', 'Yarralumla, ACT,',
            'Aranda, ACT', 'Belconnen, ACT', 'Bruce, ACT', 'Cook, ACT', 'Dunlop, ACT', 'Evatt, ACT',
            'Florey, ACT', 'Flynn, ACT', 'Gooromon, ACT', 'Holt, ACT', 'Lawson, ACT', 'Macquarie, ACT']
# list of possible institutions
institutions = ['Westfarmers', 'Woolworths', 'Australian National University', 'University of New South Wales',
                'Commonwealth Bank', 'BHP', 'National Australian Bank', 'AGL Energy', 'University of South Australia',
                'AMP', 'Ansell', 'Jetstar', 'Virgin', 'David Jones', 'Delta', 'Energex', 'Foxtel',
                'Goodman Fielder', 'IGA', 'iiNet', 'Internode', 'Lion', 'Macquarie Group', 'Origin',
                'Qantas', 'SPC Ardmona', 'Slater & Gordon', 'St George Bank', 'Seven', 'Tarocash',
                'Tabcorp Holdings', 'Sydney Water', 'UGL Limited', 'Village Cinemas', 'Zinifex',
                'Woords Bagot', 'Westpac', 'Westnet', 'WorleyParsons']

def main():
    mainDirectory = './library'
    subdirectories = [x[0] for x in os.walk(mainDirectory)]
    for subdir in subdirectories[1:]:
        print(subdir)
        infoFile = open(subdir + '/info.txt', "w+")
        people_id = subdir.split('\\')[-1]
        name = people_id.replace('_',' ')
        
        # print('name: '+name)
        # print(name.replace('_',' '))
        # name = subdir.split('/')[-1].split('_')
        # print("name ",name)
        # if len(name) > 1:
        #     name = name[0] + " " + name[1]
        # else:
        #     name = name[0]
        # print('name2: '+name)
        infoFile.write(str(people_id) + "%" + str(name) + "%" + str(randint(age[0], age[1])) + "%" + location[randint(0, len(location)-1)] + "%" + institutions[randint(0, len(institutions)-1)])
        infoFile.close()


if __name__ == '__main__':
    main()
