from django.db import models
from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(verbose_name="城市名称", max_length=20)
    desc = models.CharField(verbose_name="描述", max_length=200)

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=200, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    tag = models.CharField(default="全国知名", verbose_name="机构标签", max_length=50)
    Category = models.CharField(default="pxjg", verbose_name="机构类别", max_length=4,
                                choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name="点击人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    Image = models.ImageField(upload_to="media/org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(verbose_name=u"教师名", max_length=50)
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=100, verbose_name="就职公司")
    work_position = models.CharField(max_length=100, verbose_name="公司职位")
    points = models.CharField(max_length=200, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄")
    imag = models.ImageField(upload_to="media/teacher/%Y/%m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

