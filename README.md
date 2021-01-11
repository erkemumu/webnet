# webnet
# Django中使用数据库
一、Django 的数据以Model的操作方式

    1、在model.py中定义需要使用的类
    2、详细的设置每一个在类中的变量，即数据表中的每一个字段
    3、使用python manage.py makemigrations mainsite 创建数据库和Django间的中间文件
    4、使用python manage.py migrate 同步更新数据库的内容
    5、在程序中使用Python的方法操作所定义的数据类，等于是在操作数据库中的数据表。
二、启动admin数据库管理界面（配置步骤）

    创建超级用户的账号和密码用于管理数据库
        python manage.py createsuperuser
    登录127.0.0.1:8000/admin

三、读取数据库中的内容
    
    






