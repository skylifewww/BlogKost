from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from article.models import *
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.template import loader, Context, RequestContext


# Create your views here.
articles_of_course = {} 

def return_path_f(request):
    request.session.modified = True
    if 'return_path' in request.session:
        del request.session['return_path']
        request.session['return_path'] = request.META.get('HTTP_REFERER', '/')
    else:
        request.session['return_path'] = request.META.get('HTTP_REFERER', '/')


def articles(request):

    return_path_f(request)

    args = {}
    args['tags'] = Tag.objects.all()
    args['articles'] = Article.objects.all()
    args['username'] = auth.get_user(request).username     
    args["categories"] = Category.objects.all()  
    args["authors"] = Author.objects.all()     

    return render_to_response("articles.html", args)


def article(request, category_id, article_id=1):
    
    all_comments = Comments.objects.filter(comments_article_id=article_id)
    current_category = Category.objects.get(id=category_id)
    course_articles = Article.objects.filter(article_category__in=current_category.get_descendants(include_self=True))

    for article in course_articles:
        articles_of_course[article.article_number] = article

    len_dict = len(articles_of_course)

    args = {}

    args.update(csrf(request))

    return_path_f(request)

    args["len_dict"] = len_dict
    args["article"] = Article.objects.get(id=article_id)
    args["author"] = Author.objects.filter(id=article_id)
    args['current_category'] = current_category
    args['tags'] = Tag.objects.all()
    args["comments"] = all_comments
    args["form"] = CommentForm
    args["username"] = auth.get_user(request).username
    args["categories"] = Category.objects.all()  
    args["authors"] = Author.objects.all()   

    return render_to_response("article.html", args, context_instance=RequestContext(request))


def article_left_right(request, art_page_number, category_id):

    art_page_number = int(art_page_number)
    current_category = Category.objects.get(id=category_id)
    article = articles_of_course[art_page_number]
    article_id = article.id
    all_comments = Comments.objects.filter(comments_article_id=article_id)
   
    args = {}
    args.update(csrf(request))

    return_path_f(request)

    args["article"] = article
    args["author"] = Author.objects.filter(id=article_id)
    args['current_category'] = current_category
    args['tags'] = Tag.objects.all()
    args["comments"] = all_comments
    args["form"] = CommentForm
    args["username"] = auth.get_user(request).username
    args["categories"] = Category.objects.all()  
    args["authors"] = Author.objects.all()   

    return render_to_response("article.html", args, context_instance=RequestContext(request))


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(request.META.get('HTTP_REFERER', '/'))
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(request.META.get('HTTP_REFERER', '/'))


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        user = auth.get_user(request)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_user = user
            form.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def category(request, category_id=1):
    
    current_category = Category.objects.get(id=category_id)
    root_category_id = current_category.get_root().id
    
    args = {}
    args['tags'] = Tag.objects.all()
    args['current_category'] = current_category
    args['root_category_id'] = root_category_id
    args['categories'] = Category.objects.all()
    args['authors'] = Author.objects.all()
    args['articles'] = Article.objects.filter(article_category__in=current_category.get_descendants(include_self=True))
    args['username'] = auth.get_user(request).username
    
    return render_to_response('articles.html', args, context_instance=RequestContext(request))    


def authors(request, author_id=1):

    current_author = Author.objects.get(id=author_id)
    root_author_id = current_author.get_root().id
    args = {}
    args['tags'] = Tag.objects.all()
    args['current_author'] = current_author
    args['root_author_id'] = root_author_id
    args['authors'] = Author.objects.all()
    args['categories'] = Category.objects.all()
    args['articles'] = Article.objects.filter(article_author_id=author_id)
    args['username'] = auth.get_user(request).username

    return render_to_response('articles.html', args, context_instance=RequestContext(request))    


def tags(request, tag_id=1):
    
    current_tag = Tag.objects.get(id=tag_id)
    args = {}
    args['tags'] = Tag.objects.all()
    args['current_tag'] = current_tag
    args['authors'] = Author.objects.all()
    args['categories'] = Category.objects.all()
    args['articles'] = Article.objects.filter(article_tag__tag_name__exact=current_tag)
    args['username'] = auth.get_user(request).username

    return render_to_response('articles.html', args, context_instance=RequestContext(request))    

# def articles(request, page_number=1):
#     all_article = Article.objects.all()
#     current_page = Paginator(all_article, 3)

#     return_path_f(request)

#     args = {}
#     args['tags'] = Tag.objects.all()
#     args['articles'] = current_page.page(page_number)
#     args['username'] = auth.get_user(request).username
#     args['art_page_number'] = page_number       
#     args["categories"] = Category.objects.all()  
#     args["authors"] = Author.objects.all()     

#     return render_to_response("articles.html", args)


# def article(request, article_id=1, art_page_number=1):
#     all_comments = Comments.objects.filter(comments_article_id=article_id)

#     args = {}
#     args.update(csrf(request))

#     return_path_f(request)

#     args["article"] = Article.objects.get(id=article_id)
#     args["author"] = Author.objects.filter(id=article_id)
#     args['tags'] = Tag.objects.all()
#     args["comments"] = all_comments
#     args["form"] = CommentForm
#     args["username"] = auth.get_user(request).username
#     args["art_page_number"] = art_page_number
#     args["categories"] = Category.objects.all()  
#     args["authors"] = Author.objects.all()   

#     return render_to_response("article.html", args, context_instance=RequestContext(request))



# def category(request, category_id=1, page_number=1):
    
#     current_category = Category.objects.get(id=category_id)
#     root_category_id = current_category.get_root().id
#     all_article = Article.objects.filter(article_category__in=current_category.get_descendants(include_self=True))
#     current_page = Paginator(all_article, 3)
    
#     args = {}
#     args['tags'] = Tag.objects.all()
#     args['current_category'] = current_category
#     args['root_category_id'] = root_category_id
#     args['categories'] = Category.objects.all()
#     args['authors'] = Author.objects.all()
#     args['articles'] = current_page.page(page_number)
#     args['art_page_number'] = page_number
#     args['username'] = auth.get_user(request).username
    
#     return render_to_response('articles.html', args, context_instance=RequestContext(request))    


# def authors(request, author_id=1, page_number=1):
#     all_article = Article.objects.filter(article_author_id=author_id)

#     current_author = Author.objects.get(id=author_id)
#     root_author_id = current_author.get_root().id
#     current_page = Paginator(all_article, 3)
#     args = {}
#     args['tags'] = Tag.objects.all()
#     args['current_author'] = current_author
#     args['root_author_id'] = root_author_id
#     args['authors'] = Author.objects.all()
#     args['categories'] = Category.objects.all()
#     args['articles'] = current_page.page(page_number)
#     args['art_page_number'] = page_number
#     args['username'] = auth.get_user(request).username

#     return render_to_response('articles.html', args, context_instance=RequestContext(request))    


# def tags(request, tag_id=1, page_number=1):
    
#     current_tag = Tag.objects.get(id=tag_id)
#     args = {}
#     args['tags'] = Tag.objects.all()
#     all_article = Article.objects.filter(article_tag__tag_name__exact=current_tag)
#     current_page = Paginator(all_article, 3)
#     args['current_tag'] = current_tag
#     args['authors'] = Author.objects.all()
#     args['categories'] = Category.objects.all()
#     args['articles'] = current_page.page(page_number)
#     args['art_page_number'] = page_number
#     args['username'] = auth.get_user(request).username

#     return render_to_response('articles.html', args, context_instance=RequestContext(request))    


