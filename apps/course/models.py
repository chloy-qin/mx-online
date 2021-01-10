from django.db import models
from apps.users.models import BaseModel
from apps.organizations.models import Teacher


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(verbose_name="课程名称", max_length=100)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)", )
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击人数")
    category = models.CharField(default=u"后端开发", max_length=30, verbose_name="课程类别")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=50)
    youneed_know = models.CharField(default="", verbose_name="课程须知", max_length=100)
    teacher_tell = models.CharField(default="", verbose_name="老师告诉你", max_length=100)

    detail = models.TextField(default="", verbose_name="课程详情")
    image = models.ImageField(upload_to="media/courses/%Y/%m", verbose_name="封面图", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")  # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name=u"章节名称")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名称")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    url = models.CharField(verbose_name="访问地址", max_length=200)

    class Meta:
        verbose_name = "视频信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(verbose_name="资源名称", max_length=200)
    download = models.FileField(upload_to="course/resourse/%Y/%m", verbose_name="下载地址", max_length=300)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

