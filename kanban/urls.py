from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name="users_detail"),
    path('users/<int:pk>/update', views.UserUpdateView.as_view(), name="users_update")
]

# urlpatterns というリストに path() 関数を格納します。
# path() 関数は route , view , name , kwargs の4つの引数を受け取ります。
# そのうち route と view の2つは必須の引数で、他の2つは省略可能な引数です。
# route はURLパターンの文字列です。Djangoはリクエストとして受け取ったURLと、routeとして設定された文字列をリストの上から順に比較し、一致するものを特定します。（厳密にはドメイン以下を比較します）
# 例えばドメインを https://www.example.com/ とすると、今指定したパターンは ''（空の文字列） なので https://www.example.com/ そのものが特定されます。 https://www.example.com/users や https://www.example.com/home は除外されます。
# view はビュー関数を指定します。 route で指定したURLパターンで特定されたリクエストは view で指定したビューに渡されます。
# name に文字列を指定することで、URLの名称の定義が可能です。これにより、Djangoのあらゆる場所から参照することが可能となります。
# kwargs は追加の引数を辞書としてビューに渡すことができます。
# ここでは route と view name を指定しています。

# path()の第一引数の <int:pk> というのが見慣れないですが、これはデータベースの主キー（PK）のことを指します。IDのような固有の値になります。 int とあるので、整数型のPKを示します。
