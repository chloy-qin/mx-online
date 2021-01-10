import xadmin
from apps.course.models import Course, Lesson, Video, CourseResource


class GlobalSetting(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
#    menu_style = 'accordion'


class CourseAdmin(object):
    list_display = ['name', 'degree', 'teacher', 'learn_times', 'students', 'desc', 'fav_nums', 'detail']
    search_fields = ['name', 'degree', 'learn_times', 'student', 'desc']
    list_filter = ['name', 'degree', 'teacher__name', 'learn_times', 'desc']
    list_editable = ['name', 'degree', 'learn_times']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time', 'download']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']
    list_editable = ['course', 'name']


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']
    list_editable = ['course', 'name', 'learn_times']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'learn_times']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    list_editable = ['lesson', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)

xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
