from django.contrib import admin

from .models import Post, Comment, PageDescription, Gallery, PhotoForGallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'photo')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    # generates slug automatically based on the title
    prepopulated_fields = {'slug': ('title',)}

    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)  # Decorator registers the comment into the Admin area
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(PageDescription)
class PageHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'photo', 'status', 'author', 'created_on')
    actions = ['publish_home', 'unpublish_home']

    def publish_home(self, request, queryset):
        queryset.update(status=1)

    def unpublish_home(self, request, queryset):
        queryset.update(status=0)

    readonly_fields = ('slug',)

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = PageDescription.objects.all().count()
        if count < 2:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PhotoForGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'photo', 'status')
    actions = ['publish_home', 'unpublish_home']

    def publish_home(self, request, queryset):
        queryset.update(status=1)

    def unpublish_home(self, request, queryset):
        queryset.update(status=0)


class PhotoInline(admin.TabularInline):
    model = PhotoForGallery
    # controls the number of extra forms the formset will display in addition to the initial forms.
    extra = 0
    list_display = ('photo', 'status')
#    template = "admin/blog/gallery/edit_inline/tabular.html"

# @admin.register(Gallery)


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

    list_display = ('title', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title']
    actions = ['publish_image', 'unpublish_image']

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Gallery.objects.all().count()
        if count < 10:
            return True
        return False

    def publish_image(self, request, queryset):
        queryset.update(status=1)

    def unpublish_image(self, request, queryset):
        queryset.update(status=0)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
       # print(obj.photoforgallery_set.get(id=7).photo)
       # obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            print(afile)
            obj.photoforgallery_set.create(photo=afile)


admin.site.register(Gallery, GalleryAdmin)
