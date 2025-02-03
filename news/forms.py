from django.forms import ModelForm
from .models import Article, PhotoPost

class ArticleForm(ModelForm):
    class Meta:
        # モデルのクラス
        model = Article
        # フォームで使用するモデルのフィールドを指定
        fields = ['title', 'image1', 'main_centence']

class PhotoPostForm(ModelForm):
    class Meta:
        # モデルのクラス
        model = PhotoPost
        # フォームで使用するモデルのフィールドを指定
        fields = ['category', 'title', 'comment', 'image1', 'image2']