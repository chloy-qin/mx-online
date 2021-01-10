from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.course.models import Course

UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(max_length=50, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course = models.CharField(max_length=50, verbose_name="课程名称")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{name}_{course}({mobile})'.format(name = self.name, course = self.course, mobile = self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    comment = models.CharField(max_length = 200, verbose_name = "评论内容")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据id")
    fav_type = models.CharField(
        choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), verbose_name="收藏类型", max_length=4)

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}_{id}'.format(user = self.user.username, id = self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE, verbose_name = "用户")
    course = models.ForeignKey(Course, on_delete = models.CASCADE, verbose_name = "课程")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}_{course}'.format(user = self.user.name, course = self.course.name)