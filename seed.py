import faker
from random import randint, choice 
from db import get_session  # Імпортуємо наш менеджер сесій
from models import Group, Student, Teacher, Subject, Grade

fake = faker.Faker()

def seed_data(session):
    # 1. Створюємо групи
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)

    # 2. Створюємо викладачів
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    # 3. Створюємо предмети
    subjects_names = ["Math", "Physics", "History", "Programming", "Biology"]
    subjects = []
    for name in subjects_names:
        sub = Subject(name=name, teacher_id=choice(teachers).id)
        subjects.append(sub)
    session.add_all(subjects)
    session.commit()

    # 4. Створюємо студентів
    students = []
    for _ in range(30):
        student = Student(fullname=fake.name(), group_id=choice(groups).id)
        students.append(student)
    session.add_all(students)
    session.commit()

    # 5. Створюємо оцінки
    for student in students:
        for _ in range(20):
            grade = Grade(
                student_id=student.id,
                subject_id=choice(subjects).id,
                grade=randint(1, 12),
                date_received=fake.date_this_year()
            )
            session.add(grade)
    
    session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    with get_session() as session:
        seed_data(session)