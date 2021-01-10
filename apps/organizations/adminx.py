import xadmin
from apps.organizations.models import  Teacher, CourseOrg, City


class CourseOrgAdmin(object):
    list_display = ['id', 'name', 'desc', 'course_nums', 'students', 'address']
    search_fields = ['name', 'address']
    list_filter = ['name', 'add_time']
    list_editable = ['name', '']


class TeacherAdmin(object):
    list_display = ['id', 'name', 'work_years', 'work_company', 'work_position', 'points']
    search_fields = ['name', 'work_company', 'work_position']
    list_filter = ['name', 'work_company', 'work_position', 'add_time']
    list_editable = ['name', 'work_company', 'work_position']


class CityAdmin(object):
    list_display = ['id', 'name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)


