from sqlalchemy import func, desc
from models import Student, Group, Teacher, Subject, Grade
from db import get_session

def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Student) \
        .join(Grade) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5).all()

def select_2(session, subject_name: str):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Subject) \
        .filter(Subject.name == subject_name) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .first()

def select_3(session, subject_name: str):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Group) \
        .join(Student) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.id).all()

def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(session, teacher_name: str):
    return session.query(Subject.name) \
        .join(Teacher) \
        .filter(Teacher.fullname == teacher_name).all()

def select_6(session, group_name: str):
    return session.query(Student.fullname) \
        .join(Group) \
        .filter(Group.name == group_name).all()

def select_7(session, group_name: str, subject_name: str):
    return session.query(Student.fullname, Grade.grade) \
        .select_from(Grade) \
        .join(Student) \
        .join(Group) \
        .join(Subject) \
        .filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(session, teacher_name: str):
    return session.query(func.round(func.avg(Grade.grade), 2)) \
        .select_from(Grade) \
        .join(Subject) \
        .join(Teacher) \
        .filter(Teacher.fullname == teacher_name).scalar()

def select_9(session, student_name: str):
    return session.query(Subject.name) \
        .join(Grade) \
        .join(Student) \
        .filter(Student.fullname == student_name) \
        .distinct().all()

def select_10(session, student_name: str, teacher_name: str):
    return session.query(Subject.name) \
        .join(Grade) \
        .join(Student) \
        .join(Subject) \
        .join(Teacher) \
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name) \
        .distinct().all()

if __name__ == "__main__":
    with get_session() as session:
        print("1:", select_1(session))
        print("4 (Avg total):", select_4(session))
        