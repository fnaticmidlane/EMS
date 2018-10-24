from django.urls import path


from .views import JoinEventView, RegistrationDetailView, RegistrationListView
urlpatterns = [
    path("events/<int:event_pk>/join/", JoinEventView.as_view(), name = "join_event"),
    path("registrations/<int:pk>/", RegistrationDetailView.as_view(), name = "registration_detail"),
    path("events/<int:event_pk>/participants/", RegistrationListView.as_view(), name = "registration_list")



]