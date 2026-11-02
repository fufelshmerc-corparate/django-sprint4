from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse


class OnlyAuthorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        obj = self.get_object()
        if obj.author != request.user:
            return redirect(self._denied_url(obj))
        return super().dispatch(request, *args, **kwargs)

    def _denied_url(self, obj):
        post_id = getattr(obj, 'post_id', None) or obj.pk
        return reverse('blog:post_detail', args=(post_id,))
