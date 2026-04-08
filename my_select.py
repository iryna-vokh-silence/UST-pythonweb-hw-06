from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student, Group, Teacher, Subject, Grade

# Підключення до бази
engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    # 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student)\
        .group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    # 2. Знайти студента із найвищим середнім балом з певного предмета.
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(subject_name):
    # 3. Знайти середній бал у групах з певного предмета.
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Group.id).all()

def select_4():
    # 4. Знайти середній бал на потоці (по всій таблиці оцінок).
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(teacher_name):
    # 5. Знайти які курси читає певний викладач.
    return session.query(Subject.name).join(Teacher)\
        .filter(Teacher.fullname == teacher_name).all()

def select_6(group_name):
    # 6. Знайти список студентів у певній групі.
    return session.query(Student.fullname).join(Group)\
        .filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    # 7. Знайти оцінки студентів у окремій групі з певного предмета.
    return session.query(Student.fullname, Grade.grade)\
        .select_from(Grade).join(Student).join(Group).join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    # 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    return session.query(func.round(func.avg(Grade.grade), 2))\
        .select_from(Grade).join(Subject).join(Teacher)\
        .filter(Teacher.fullname == teacher_name).scalar()

def select_9(student_name):
    # 9. Знайти список курсів, які відвідує певний студент.
    return session.query(Subject.name).distinct().join(Grade).join(Student)\
        .filter(Student.fullname == student_name).all()

def select_10(student_name, teacher_name):
    # 10. Список курсів, які певному студенту читає певний викладач.
    return session.query(Subject.name).distinct()\
        .join(Grade).join(Student).join(Subject.teacher)\
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name).all()

if __name__ == "__main__":
    # Приклади викликів (імена можуть відрізнятися через Faker, перевір у базі)
    print("1:", select_1())
    print("4 (Avg total):", select_4())