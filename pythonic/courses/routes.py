from flask import Blueprint, request

from pythonic.models import Lesson, Course
from flask import (
    render_template,
)


courses_bp = Blueprint("courses", __name__)


@courses_bp.route("/<string:course_title>")
def course(course_title):
    course = Course.query.filter_by(title=course_title).first()
    course_id = course.id if course else None
    course = Course.query.get_or_404(course_id)
    return render_template(
        "course.html",
        title=course.title,
        course=course,
    )




@courses_bp.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("courses.html", title="Courses", courses=courses)



