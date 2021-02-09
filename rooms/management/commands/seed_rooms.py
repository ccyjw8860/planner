from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from users.models import User
from rooms.models import Room
import random
import os


img_list = os.listdir('./uploads/room_photos')

title_list = [
    '매일 농구 인증',
    '캠핑 상자',
    '일주일에 5일 운동하기',
    '만보 걷기',
    '매일 10분 악기, 노래 연습',
    '달리기, 마라톤',
    '매일 10k 러닝 인증',
    '다이어트(독하게 살뺄 사람만)',
    '매일매일 조금씩 독서 인증',
    '크리오 타는 사람들',
    '나무 젓가락 공예',
    '하루에 영단어 하나씩 외우기',
    '매일 우리 역시 알아보기',
    '유튜브 함께만들고 함께 성장하는 유튜버 모임',
    '매일 사전 베끼기',
    '그리다 만들다',
    '하루 오천보 걷기 인증',
    '운동일지',
    '삼시세끼 요리하고 인증',
    '시사 인증',
    '하루 푸쉬업 100회하기'
]

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='how many users do you want to create')

    def handle(self, *args, **options):
        number = options.get('number')
        users = User.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(Room, number, {
            'title': lambda x: random.choice(title_list),
            'description': '테스트용 description',
            'host': lambda x: random.choice(users),
            'photo': lambda x: f"room_photos/{random.choice(img_list)}",
            'photo_caption': lambda x: seeder.faker.sentence()
        })
        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for user in users:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    room.participants.add(user)

        self.stdout.write(self.style.SUCCESS(f'{number} of rooms are created!'))