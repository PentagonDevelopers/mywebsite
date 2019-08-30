from django.conf.urls import url
from . import views

app_name = 'managetrainer'

urlpatterns = [
    url(r'^$', views.TrainerDetails.as_view(), name="home"),

    # url(r'^(?P<emp_id>[a-zA-Z0-9]+)$', views.TrainerInfo.as_view(), name="details"),

    url(r'^(?P<pk>[a-zA-Z0-9]+)$', views.TrainerInfo.as_view(), name="details"),

    url(r'^update/(?P<pk>[a-zA-Z0-9]+)$', views.UpdateForm.as_view(), name="update"),

    url(r'^(?P<pk>[a-zA-Z0-9]+)/delete/$', views.DeleteForm.as_view(), name="delete"),

    # url(r'^(?P<emp_id>[a-zA-Z0-9]+)/change$', views.trainer_change, name="change"),
    #
    #url(r'^form/register$', views.register_page, name='register'),
    #
    #url(r'^add/trainer$', views.add_trainer, name='add_trainer'),

    url(r'^form/register$', views.CreateForm.as_view(), name='register'),
    url(r'^form/userregister$', views.UserFormView.as_view(), name='user_register'),
]
