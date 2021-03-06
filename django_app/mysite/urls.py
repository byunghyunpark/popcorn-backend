"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from member.apis.mypage import MyComments, MyFamousLines, MyInfo, MyLikeMovie
from member.views import ConfirmEmailView, PasswordResetView, PasswordResetConfirmView
from movie.apis.box_office import BoxOfficeAPIView, BoxOfficeAPIViewIOS
from movie.apis.comment import NewCommentAPIView, BestComment
from movie.apis.favorites import GenreView, MakingCountryView, GradeView, UserFavorites, DeleteFavorite
from movie.apis.magazine import SampleMagazineAPIView
from movie.apis.movie_recommend import CarouselMovieRecommend, MainMovieList, FavoriteMovieRecommend, \
    FavoriteMovieRecommendIOS

urlpatterns = [
    # 어드민페이지
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 메인페이지
    url(r'^main/box-office/$', BoxOfficeAPIView.as_view(), name='box_office'),
    url(r'^main/box-office/ios/$', BoxOfficeAPIViewIOS.as_view(), name='box_office_ios'),
    url(r'^main/comments/$', NewCommentAPIView.as_view(), name='new_comments'),
    url(r'^main/magazines/$', SampleMagazineAPIView.as_view(), name='magazine_samples'),
    url(r'^main/movie-recommends/$', MainMovieList.as_view(), name='movie_recommends'),
    url(r'^main/movie-recommends/carousel/$', CarouselMovieRecommend().as_view(), name='carousel_movie_recommends'),
    url(r'^main/user-favorites/$', UserFavorites.as_view(), name='user_favorites'),
    url(r'^main/movie-recommends/favorites/$', FavoriteMovieRecommend.as_view(), name='movie_recommend_favorite'),
    url(r'^main/movie-recommends/favorites/ios/$', FavoriteMovieRecommendIOS.as_view(), name='movie_recommend_favorite'),
    url(r'^main/best-comment/', BestComment.as_view(), name='best_comment'),
    # 취향페이지
    url(r'^favorite/genre/$', GenreView.as_view(), name='favorites_genre'),
    url(r'^favorite/grade/$', GradeView.as_view(), name='favorites_grade'),
    url(r'^favorite/making-country/$', MakingCountryView.as_view(), name='favorites_making_cuntry'),
    # 회원페이지
    url(r'^accounts/', include('allauth.urls')),
    url(r'^member/', include('rest_auth.urls')),
    url(r'^member/registration/', include('rest_auth.registration.urls')),
    url(r'^member/password/reset/$', PasswordResetView.as_view(), name='rest_password_reset'),
    url(r'^member/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^member/my-comments/', MyComments.as_view(), name='my_comment'),
    url(r'^member/my-famous/', MyFamousLines.as_view(), name='my_famous'),
    url(r'^member/my-info/', MyInfo.as_view(), name='my_info'),
    url(r'^member/my-like-movie/', MyLikeMovie.as_view(), name='my_like_movie'),
    url(r'^member/delete-favorite/', DeleteFavorite.as_view(), name='delete_favorite'),
    # 테스트페이지
    url(r'^test-api/', include('test_app.urls', namespace='test')),
    # 영화페이지
    url(r'^movie/', include('movie.urls.apis', namespace='movie')),
]
