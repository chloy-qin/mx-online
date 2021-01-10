import xadmin
from apps.operation.models import  UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['id', 'name', 'course', 'mobile']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course', 'add_time']



class UserFavoriteAdmin(object):
    list_display = ['id', 'user', 'fav_id', 'fav_type']
    search_fields = ['user', 'fav_type']
    list_filter = ['user', 'fav_type', 'add_time']

class UserMessageAdmin(object):
    list_display = ['id', 'user', 'message']
    search_fields = ['user', 'message']
    list_filter = ['user', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['id', 'user', 'course']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['id', 'user', 'course']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)