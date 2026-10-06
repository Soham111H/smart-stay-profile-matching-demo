from django.core.management.base import BaseCommand
from matching.models import RoommateProfile

DATA = [
('Aarav',20,'Vadodara',9000,'normal','high','veg','never','balanced','quiet','rare',True,True,'Calm student who likes a clean and study-friendly room.'),
('Riya',21,'Vadodara',8500,'normal','high','veg','never','social','moderate','sometimes',True,True,'Friendly, organized and enjoys cooking occasionally.'),
('Kunal',22,'Vadodara',10000,'late','medium','nonveg','sometimes','social','moderate','often',True,False,'Night owl, social and comfortable with guests.'),
('Meera',20,'Vadodara',8000,'early','high','veg','never','quiet','quiet','rare',False,True,'Early sleeper, quiet lifestyle and very tidy.'),
('Dev',23,'Vadodara',9500,'late','low','nonveg','yes','social','loud','often',True,False,'Outgoing person who is relaxed about room rules.'),
('Ishita',21,'Vadodara',9000,'normal','medium','both','never','balanced','moderate','sometimes',True,True,'Balanced habits, likes a practical and flexible roommate.'),
('Harsh',22,'Vadodara',7500,'normal','low','nonveg','sometimes','quiet','moderate','rare',False,True,'Budget-conscious and focused on academics.'),
]

class Command(BaseCommand):
    help='Reset and create demo roommate profiles.'
    def handle(self,*args,**opts):
        RoommateProfile.objects.all().delete()
        for row in DATA:
            RoommateProfile.objects.create(name=row[0],age=row[1],city=row[2],budget=row[3],sleep=row[4],cleanliness=row[5],food=row[6],smoking=row[7],social=row[8],noise=row[9],guests=row[10],cooking=row[11],study_work=row[12],bio=row[13])
        self.stdout.write(self.style.SUCCESS(f'Created {len(DATA)} demo profiles. First profile is the current demo user.'))
