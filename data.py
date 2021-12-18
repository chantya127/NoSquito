"""
Moro's data points
10 data points
Area kothruds's Hotspots(remain inside the boundary of th given area)(slums,sewage canals..)
https://www.google.com/maps/place/Kothrud,+Pune,+Maharashtra/@18.5140546,73.7935872,14z/data=!4m5!3m4!1s0x3bc2bfb732af849d:0xd4078b48b3fe44f0!8m2!3d18.5073514!4d73.8076543
keep a aprroximate distance of 1.5 to 2 km between traps

Imp Points
    everyting in smallcase
    if culex poro species remove space and everyting in small case
    date 09_03_2021 and not 09-03-2021

max (70-60%combine)
    anopheles = malaria (trap ht = 0.9 to 1)
    aedesaegypti = dengue (trap ht = 0.9 to 2)
min (8-10% chikungunya + remaining others)
    aedesaegypti,aedesalbopictus = chikungunya (trap ht = 0.9 to 2)
	culextritaeniorhynchus = japaneseencephalitis (trap ht = 1.3 to 1.5)#use it rarely can say in hackathon we found the species after 50 yrs in Pune
    aedesaegypti = yellowfever (trap ht = 2.2 to 2.5)

Trap date between 15_02_2021 to 15_04_2021
Insert only 4 diseases(max=2)(min any two)
"""

"""
Bhusari Colony, Shashwat Hospital, Suyash Hospital, krushna hospital
"""

data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.4993006,73.8138217',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_02_2021',
    'malaria ': {
        'percentage': 90,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 8,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':2,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.509200719257542,73.81273615321413',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_02_2021',
    'malaria ': {
        'percentage': 90,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 10,
        'species': ['aedesaegypti']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 2,
    'city': 'pune',
    'location':'18.50169224425977,73.80861628016726',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_02_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 18,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':2,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 2,
    'city': 'pune',
    'location':'18.504886947315654,73.82167327365175',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_02_2021',
    'malaria ': {
        'percentage': 50,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 30,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':20,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}


data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.5104269,73.7945643',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_03_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 20,
        'species': ['aedesaegypti']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.509200719257542,73.81273615321413',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_03_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 15,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':5,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.4948349,73.8135271',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_03_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 18,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':2,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.4981982,73.8139826',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_03_2021',
    'malaria ': {
        'percentage': 70,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 20,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':10,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}


data = {
    'no': 'trap'+str(trap_no),
    'ht': 1.4,
    'city': 'pune',
    'location':'18.4981982,73.8139826',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_04_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 20,
        'species': ['aedesaegypti']
    },
    'japaneseencephalitis': {
        'percentage': 10,
        'species': ['culextritaeniorhynchus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.50238311504308,73.81516172756942',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_04_2021',
    'malaria ': {
        'percentage': 70,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 28,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':2,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.50238311504308,73.81516172756942',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_04_2021',
    'malaria ': {
        'percentage': 80,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 20,
        'species': ['aedesaegypti']
    }
}
data = {
    'no': 'trap'+str(trap_no),
    'ht': 1,
    'city': 'pune',
    'location':'18.495388163322463,73.81178080310599',#latitude,longitude
    'coordinates': 'xyz',
    'date':'15_04_2021',
    'malaria ': {
        'percentage': 70,
        'species': ['anopheles']
     },
    'dengue': {
        'percentage': 20,
        'species': ['aedesaegypti']
    },
    'chikungunya': {
        'percentage':10,
        'species': ['aedesaegypti','aedesalbopictus']
    }
}





