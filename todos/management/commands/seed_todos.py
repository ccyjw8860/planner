from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from users.models import User
from rooms.models import Room
from todos.models import Todo, TodoPhoto
from datetime import datetime, timedelta
import random
import os

names = [
    '달리기',
    '줄넘기',
    "뉴스대본 읽기 (평일)",
    "운동 주 5-6회",
    "영상 주 1회",
    "글 주 3~5회",
    "운동 주 5회 (1h)",
    "아침9시기상",
    "아침 8시 산책",
    "10분 운동하기",
    "주말 그림작업",
    "분리수거 인증(2020/11/16~)",
    "1일 1코드 작성",
    "1일 1코드 인증 주소",
    "매일 15분 스트레칭",
    "주말 러시아어 (1h)",
    "매일 한 일 인증",
    "주 4일 필라테스/명상",
    "포레스트 앱 인증",
    "브런치 글쓰기 주 2회 (종료)",
    "평일 하루 1시간 업무 외 확보",
    "필라테스 주 3회",
    "아침 스트레칭 20분",
    "주 30km 이상 걷기",
    "주 2회 책 읽기 ",
    "다이어리 매일 기록",
    "주 2회 운동",
    "평일 7시 이전 기상/산책",
    "매일 일기쓰기",
    "주 40km 이상 걷기",
    "영화 or 책 주 1회 1편",
    "2일 1포스팅",
    "주 3회 아침운동",
    "주 3회 운동",
    "따~뜻한 차 한잔 마시기",
    "업무일기 11/14(토)"
]

todo_photos = os.listdir('./uploads/room_photos')

today = datetime.now()
today = today.date()

def get_start_date():
    return today + timedelta(days=random.randint(-10,10))

def get_end_date(start_date):
    return start_date + timedelta(days=random.randint(0,5))

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='how many users do you want to create')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        start_date = get_start_date()
        seeder.add_entity(Todo, number, {
            'user': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'title': lambda x: random.choice(names),
            'start_date': lambda x: str(start_date),
            'end_date': lambda x: str(get_end_date(start_date))
        })
        created_todos = seeder.execute()
        created_clean = flatten(list(created_todos.values()))
        for pk in created_clean:
            todo = Todo.objects.get(pk=pk)
            howmany = random.randint(0,3)
            if howmany > 0:
                for i in range(howmany):
                    TodoPhoto.objects.create(
                        caption = seeder.faker.sentence(),
                        todo = todo,
                        file=f"rooms_photos/{random.choice(todo_photos)}"
                    )
        self.stdout.write(self.style.SUCCESS(f'{number} of users are created!'))