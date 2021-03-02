from django.db import models
#
#
# #
# # class Post(models.Model):
# #     title = models.CharField(max_length=100)
# #     content = models.TextField()
# #     img = models.ImageField()
# #     created_at = models.DateTimeField(auto_now_add=True)
# #
# #     def __str__(self):
# #         return self.title
# #
# #
# # class Comment(models.Model):
# #     post = models.ForeignKey(Post, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=100)
# #     text = models.TextField()
# #
# #     def __str__(self):
# #         return self.title
# #
# # class Admin_Comment(models.Model):
# #     post = models.OneToOneField(Post, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=100)
# #     text = models.TextField()
# #
# #     def __str__(self):
# #         return self.title
#
#
# class Group(models.Model):
#     name_of_group = models.CharField(max_length=100)
#     photo_of_group = models.ImageField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name_of_group
#
#
# class Student(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     name_of_student = models.CharField(max_length=100)
#     date_of_birthday = models.DateField()
#     photo_of_student = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name_of_student
#
#
# class Work(models.Model):
#     work = models.ForeignKey(Student, on_delete=models.CASCADE)
#     name_of_work = models.CharField(max_length=100)
#     about_work = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name_of_work
#
#
# class Book(models.Model):
#     student = models.ManyToManyField(Student)
#     name = models.CharField(max_length=100)
#     pages = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    comment = models.TextField(max_length=1000)

    class Meta:
        ordering = ('name', 'price')
        index_together = (('id', 'name'),)

    def __str__(self):
        return self.name