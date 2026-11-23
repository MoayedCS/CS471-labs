from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.index, name= "books.index"),
     path('index2/<int:val1>/',views.index2),
     path('list_books/', views.list_books, name= "books.list_books"),
     path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
     path('aboutus/', views.aboutus, name="books.aboutus"),
     path('html5/links',views.html5,name ="books.html5"),
     path('html5/text/formatting',views.formatting,name="books.formatting"),
     path('html5/listing',views.listing,name="books.listing"),
     path('html5/tables',views.tables,name="books.tables"),
     path('search',views.search,name='books.search'),
     path('simple/query', views.simple_query, name='simple_query'),
     path('complex/query', views.complex_query, name='complex_query'),
     path('lab8/task1', views.lab8_task1, name='lab8_task1'),
     path('lab8/task2', views.lab8_task2, name='lab8_task2'),
     path('lab8/task3', views.lab8_task3, name='lab8_task3'),
     path('lab8/task4', views.lab8_task4, name='lab8_task4'),
     path('lab8/task5', views.lab8_task5, name='lab8_task5'),
     path('lab8/task7', views.lab8_task7, name='lab8_task7'),
     path('lab9_part1/listbooks', views.lab9p1_listbooks, name='lab9p1_listbooks'),
     path('lab9_part1/addbook', views.lab9p1_addbook, name='lab9p1_addbook'),
     path('lab9_part1/editbook/<int:id>', views.lab9p1_editbook, name='lab9p1_editbook'),
     path('lab9_part1/deletebook/<int:id>', views.lab9p1_deletebook, name='lab9p1_deletebook'),
     path('lab9_part2/listbooks', views.lab9p2_listbooks, name='lab9p2_listbooks'),
     path('lab9_part2/addbook', views.lab9p2_addbook, name='lab9p2_addbook'),
     path('lab9_part2/editbook/<int:id>', views.lab9p2_editbook, name='lab9p2_editbook'),
     path('lab9_part2/deletebook/<int:id>', views.lab9p2_deletebook, name='lab9p2_deletebook'),
     path('lab10/students', views.lab10_liststudents, name='lab10_liststudents'),
     path('lab10/students/add', views.lab10_addstudent, name='lab10_addstudent'),
     path('lab10/students/edit/<int:id>', views.lab10_editstudent, name='lab10_editstudent'),
     path('lab10/students/delete/<int:id>', views.lab10_deletestudent, name='lab10_deletestudent'),
     path('lab10/students2', views.lab10_liststudents2, name='lab10_liststudents2'),
     path('lab10/students2/add', views.lab10_addstudent2, name='lab10_addstudent2'),
     path('lab10/students2/edit/<int:id>', views.lab10_editstudent2, name='lab10_editstudent2'),
     path('lab10/students2/delete/<int:id>', views.lab10_deletestudent2, name='lab10_deletestudent2'),
     path('lab10/products', views.lab10_listproducts, name='lab10_listproducts'),
     path('lab10/products/add', views.lab10_addproduct, name='lab10_addproduct'),
     path('lab10/products/edit/<int:id>', views.lab10_editproduct, name='lab10_editproduct'),
     path('lab10/products/delete/<int:id>', views.lab10_deleteproduct, name='lab10_deleteproduct'),
     ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
