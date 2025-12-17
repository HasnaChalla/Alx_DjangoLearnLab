# from django import forms
from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget
from .models import Post, Comment, Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):

    tags_str = forms.CharField(
        label='Tags',
        required=False,
        help_text='Separate tags with commas (e.g., Tech, Python)'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

    # 2. Logic to load existing tags when Editing
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Get all tag names, join them with commas
            self.fields['tags_str'].initial = ", ".join(
                t.name for t in self.instance.tags.all())

    # 3. Logic to Save the tags
    def save(self, commit=True):
        post = super().save(commit=True)

        tags_input = self.cleaned_data.get('tags_str', '')
        post.tags.clear()

        if tags_input:
            tag_names = [name.strip() for name in tags_input.split(',')]

            for name in tag_names:
                if name:
                    tag, created = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)

        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
