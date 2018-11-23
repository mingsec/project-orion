from django.shortcuts               import render
from django.http                    import HttpResponseRedirect, Http404
from django.urls                    import reverse
from django.contrib.auth.decorators import login_required
from .models                        import Topic, Entry, Blog
from .forms                         import TopicForm, EntryForm, BlogForm
from xpinyin                        import Pinyin

import datetime

# Create your views here.
#在此处创建你的视图函数

def index(request):
    """Learning_log网站的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics  = Topic.objects.order_by('date_added')
    context = {'topics':topics}

    return render(request, 'learning_logs/topics.html', context)

def entries(request, topic_name):
    """显示单个主题及其所有的科目"""
    topic   = Topic.objects.get(name=topic_name)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic':topic,'entries':entries}

    return render(request, 'learning_logs/entries.html', context)

def blogs(request,topic_name, entry_name):
    """显示单个主题下某个科目的所有条目"""
    entry   = Entry.objects.get(name=entry_name)
    topic   = entry.topic
    blogs   = entry.blog_set.order_by('-date_modify')
    context = {'topic':topic, 'entry':entry, 'blogs':blogs}

    return render(request, 'learning_logs/blogs.html', context)

@login_required
def new_topic(request):
    """创建新的主题"""
    pinyin = Pinyin()

    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的表单
        form = TopicForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            #获取post数据
            all_data = form.clean()   
            new_topic      = form.save(commit=False)
            new_topic.name = pinyin.get_initials(new_topic.text, splitter='')
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_name):
    """在特定的主题中创建新的科目"""
    pinyin = Pinyin()

    topic = Topic.objects.get(name=topic_name)

    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的表单
        form = EntryForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry       = form.save(commit=False)
            new_entry.topic = topic
            new_entry.name  = pinyin.get_initials(new_entry.text, splitter='')
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:entries', args=[topic.name]))

    context = {'topic':topic, 'form':form}

    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def new_blog(request, topic_name, entry_name):
    """在特定主题中的某个科目下创建新的条目"""
    pinyin = Pinyin()

    topic = Topic.objects.get(name=topic_name)
    entry = Entry.objects.get(name=entry_name)

    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的表单
        form = BlogForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog       = form.save(commit=False)
            new_blog.entry = entry
            new_blog.owner = request.user
            new_blog.name  = pinyin.get_initials(new_blog.title, splitter='')
            new_blog.save()
            return HttpResponseRedirect(reverse('learning_logs:blogs', args=[topic_name, entry_name]))

    context = {'topic':topic,'entry':entry, 'form':form}

    return render(request, 'learning_logs/new_blog.html', context)

@login_required
def edit_blog(request, topic_name, entry_name, blog_name):
    """在编辑特定主题中的某个科目下的某个条目"""
    topic = Topic.objects.get(name=topic_name)
    entry = Entry.objects.get(name=entry_name)
    blog  = Blog.objects.get(name=blog_name)

    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的表单
        form = BlogForm(instance=blog)
    else:
        #当操作为提交数据时，则对数据进行处理
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            edit_blog             = form.save(commit=False)
            edit_blog.date_modify = datetime.datetime.now()
            edit_blog.save()
            return HttpResponseRedirect(reverse('learning_logs:blogs', args=[topic.name, entry.name]))

    context = {'topic':topic,'entry':entry, 'blog':blog,'form':form}

    return render(request, 'learning_logs/edit_blog.html', context)

@login_required
def my_blogs(request):
    """显示当前用户创建的所有条目"""
    blogs = Blog.objects.filter(owner=request.user)

    entries = []
    topics  = []

    test_all = []
    
    for blog in blogs:
        test     = []

        entry = blog.entry
        topic = entry.topic

        test = [blog, entry, topic ]
        test_all.append(test)

    context = {'test_all':test_all}

    return render(request, 'learning_logs/my_blogs.html', context)

