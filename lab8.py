from flask import Blueprint, render_template, abort

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('/lab8/index.html')


courses = [
    {"name": "C++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "c#", "videos": 8}
]


@lab8.route('/lab8/api/courses/', methods=["GET"])
def get_courses():
    return courses


@lab8.route('/lab8/api/courses/<int:course_num>', methods=["GET"])
def get_course(course_num):
    if course_num > len(courses) or course_num <= 0:
        abort(404)
    else:
        course_num = course_num - 1
        return courses[course_num]
