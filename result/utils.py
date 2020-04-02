import result.models
from math import ceil

class SemesterGradeHelper:

    @staticmethod
    def get_grades(obj):
        return result.models.Grade.objects.filter(student=obj.student, course_offering__term=obj.term)

    @staticmethod
    def cal_gp_earned(obj):
        gp_earned = []
        grades = SemesterGradeHelper.get_grades(obj);
        for i, grade in enumerate(grades):
            unit = grade.course_offering.course.units
            gp_earned.append((grade.course_offering, unit, grade.letter_grade * unit))
        return gp_earned;

    # grade weight average as per selected term
    @staticmethod
    def get_gwa(obj):
        total_grade_points = 0
        gp_earned = SemesterGradeHelper.cal_gp_earned(obj);
        for grade_point in gp_earned:
            total_grade_points += grade_point[-1]
        return total_grade_points;

    @staticmethod
    def get_total_credit_hour(obj):
        total_credit_hour = 0
        gp_earned = SemesterGradeHelper.cal_gp_earned(obj);
        for grade_point in gp_earned:
            total_credit_hour += grade_point[1]
        return total_credit_hour

    # reference https://www.wikihow.com/Calculate-GPA
    @staticmethod
    def get_sgpa(obj):
        total_credit_hour = SemesterGradeHelper.get_total_credit_hour(obj)
        if (total_credit_hour):
            return round(SemesterGradeHelper.get_gwa(obj) / SemesterGradeHelper.get_total_credit_hour(obj), 2)
        else:
            return 0.00