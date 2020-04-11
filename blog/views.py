from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post, PageDescription, PhotoForGallery, Gallery
from .forms import CommentForm

#Home and Zirkuspage


class HomeDetail(generic.DetailView):
    # viewing subset of object (in PageHome)
    queryset = PageDescription.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Photos
        context['gallery_list'] = PhotoForGallery.objects.filter(status=1)
        return context


class GalleryList(generic.ListView):
    queryset = Gallery.objects.filter(status=1)
    template_name = 'photo.html'
    context_object_name = 'gallery_list'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    # pagination
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'post.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
