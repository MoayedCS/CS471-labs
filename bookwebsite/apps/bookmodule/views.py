# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book , Product
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import BookForm , ProductForm
from apps.usermodule.models import Student, Address , Student2
from apps.usermodule.forms import StudentForm , Student2Form
from django.contrib.auth.decorators import login_required
def index(request):
       return render(request, "bookmodule/index.html")
def index2(request, val1 = 0 ): # add the view function (index2)
       return HttpResponse("value1 = "+str(val1))
def list_books(request):
       return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
       return render(request, 'bookmodule/one_book.html')
def aboutus(request):
       return render(request, 'bookmodule/aboutus.html')
def html5(request):
       return render(request,'bookmodule/html5.html')
def formatting(request):
       return render(request,'bookmodule/formatting.html')
def listing(request):
       return render(request,'bookmodule/listing.html')
def tables(request):
       return render(request,'bookmodule/tables.html')
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
def __getBooksList():
       book1= {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
       book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
       book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
       return [book1, book2, book3]
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='and') \
                          .filter(edition__gte=2) \
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
def lab8_task1(request):
      mybooks = Book.objects.filter(Q(price__lte=80))
      return render(request,'bookmodule/lab8.html',{'books':mybooks})
def lab8_task2(request):
      mybooks = Book.objects.filter(Q(edition__gt = 3) & (Q(title__icontains='qu')| Q(author__icontains='qu')))
      return render(request,'bookmodule/lab8.html',{'books':mybooks})
def lab8_task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8.html', {'books': mybooks})
def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8.html', {'books': mybooks})
def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        average=Avg('price'),
        maximum=Max('price'),
        minimum=Min('price')
    )
    return render(request, 'bookmodule/lab8_stats.html', {'stats': stats})
def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_cities.html', {'cities': cities})
def lab9p1_listbooks(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/lab9p1_list.html', {'books': mybooks})
def lab9p1_addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('lab9p1_listbooks')

    return render(request, 'bookmodule/lab9p1_add.html')
def lab9p1_editbook(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('lab9p1_listbooks')
    return render(request, 'bookmodule/lab9p1_edit.html', {'book': book})
def lab9p1_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab9p1_listbooks')
@login_required
def lab9p2_listbooks(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/lab9p2_list.html', {'books': mybooks})
@login_required
def lab9p2_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('lab9p2_listbooks')
@login_required
def lab9p2_addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9p2_listbooks')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab9p2_add.html', {'form': form})
@login_required
def lab9p2_editbook(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9p2_listbooks')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab9p2_edit.html', {'form': form, 'book': book})
@login_required
def lab10_liststudents(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab10_students_list.html', {'students': students})


@login_required
def lab10_addstudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab10_liststudents')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab10_student_form.html', {'form': form, 'action': 'Add'})


@login_required
def lab10_editstudent(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab10_liststudents')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/lab10_student_form.html', {'form': form, 'action': 'Edit'})


@login_required
def lab10_deletestudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('lab10_liststudents')
@login_required
def lab10_liststudents2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab10_students2_list.html', {'students': students})


@login_required
def lab10_addstudent2(request):
    if request.method == "POST":
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab10_liststudents2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/lab10_student2_form.html', {'form': form, 'action': 'Add'})


@login_required
def lab10_deletestudent2(request, id):
    student = Student2.objects.get(id=id)
    student.delete()
    return redirect('lab10_liststudents2')


@login_required
def lab10_editstudent2(request, id):
    student = Student2.objects.get(id=id)
    if request.method == "POST":
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab10_liststudents2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/lab10_student2_form.html', {'form': form, 'action': 'Edit'})
@login_required
def lab10_listproducts(request):
    products = Product.objects.all()
    return render(request, 'bookmodule/lab10_products_list.html', {'products': products})


@login_required
def lab10_addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lab10_listproducts')
    else:
        form = ProductForm()
    return render(request, 'bookmodule/lab10_product_form.html', {'form': form, 'action': 'Add'})


@login_required
def lab10_editproduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('lab10_listproducts')
    else:
        form = ProductForm(instance=product)
    return render(request, 'bookmodule/lab10_product_form.html', {'form': form, 'action': 'Edit'})


@login_required
def lab10_deleteproduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('lab10_listproducts')
