from django.db import models

# Create your models here.

class Host(models.Model):
    '''主机'''
    hostname = models.CharField(max_length=64, blank=True, null=True, verbose_name='主机名')
    ip = models.CharField(max_length=32, blank=True, null=True, verbose_name='IP地址')
    cpu = models.CharField(max_length=32, blank=True, null=True, verbose_name='CPU')
    mem = models.CharField(max_length=16, blank=True, null=True, verbose_name='内存')
    disk = models.ManyToManyField(to='Disk', blank=True, verbose_name='磁盘')
    is_vm = models.CharField(max_length=8, blank=True, null=True, verbose_name='是否虚拟机')
    master_ip = models.CharField(max_length=32, blank=True, null=True, verbose_name='宿主机IP')
    server_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='服务器型号')
    os = models.CharField(max_length=16, blank=True, null=True, verbose_name='系统')
    server_role = models.CharField(max_length=32, blank=True, null=True, verbose_name='服务器角色')
    manage_ip = models.CharField(max_length=32, blank=True, null=True, verbose_name='管理IP')
    sn = models.CharField(max_length=16, blank=True, null=True, verbose_name='序列号')
    service_id = models.CharField(max_length=16, blank=True, null=True, verbose_name='快速服务代码')
    hostgroup = models.ForeignKey(to='GroupHost', blank=True, null=True, verbose_name='主机组')
    program = models.CharField(max_length=64, blank=True, null=True, verbose_name='运行程序')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name_plural = "主机表"

class GroupHost(models.Model):
    '''主机组'''
    group_name = models.CharField(max_length=16, blank=True, null=True, verbose_name='主机组名')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name_plural = '主机组表'

class Disk(models.Model):
    '''磁盘'''
    path = models.CharField(max_length=32, blank=True, null=True, verbose_name='挂载路径')
    size = models.CharField(max_length=16, blank=True, null=True, verbose_name='大小/G')
    remarks = models.CharField(max_length=2048, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.size

    class Meta:
        verbose_name_plural = '磁盘表'

class Users(models.Model):
    '''用户'''
    username = models.CharField(max_length=32, verbose_name='用户名')
    passwd = models.CharField(max_length=32, verbose_name='密码')
    prosition = models.CharField(max_length=16, blank=True, null=True, verbose_name='职位')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "用户表"