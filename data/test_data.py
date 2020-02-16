import random
from datetime import datetime


def generate_user_data():
    user_data = {
        'name': random.choice(['Tomasz Kowalski', "Jan Nowak"]),
        'username': f"newuser_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'address':
            {'street': random.choice(['Prosta', "Krzywa"]),
             'city': random.choice(['Katowice', "Warszawa"]),
             'zipcode': "{0:02d}-{1:03d}".format(random.randint(0, 99), random.randint(0, 999))
             },
        'phone': str(random.randint(111111111, 999999999)),
        'website': random.choice(['website1.org', "website2.pl"]),
        'company':
            {'name': 'MyCompany'}
    }
    user_data['email'] = f"{user_data['username']}@mail.pl"
    return user_data
