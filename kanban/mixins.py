from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    # raise_exception = True で、制限に引っかかった場合に例外を発生させるように設定します。

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']
    # test_func(self) メソッドでTrueかFalseを返します。このメソッド内で「特定の条件（ページのPKとユーザーのPKが等しい）」を判定し、ブーリアン型で返します。
