from django.urls import path
#from .view import testlistview, testdetailview
from rest_framework.routers import DefaultRouter
from .view import testviewset

#registers the testviewset to the main urls 
#ex http://localhost:8000/api 
#ex http://localhost:8000/api/1 
router = DefaultRouter()
router.register(r'', testviewset, base_name='test')
urlpatterns = router.urls

#above code more efficient then bottom
'''
urlpatterns = [
    path('',testlistview.as_view()),
    path('<pk>',testdetailview.as_view())
]
'''
'''
from .view import (
    testListView,
    testDetailView,
    testCreateView,
    testUpdateView,
    testDeleteView
)



urlpatterns = [
    path('', testListView.as_view()),
    path('create/', testCreateView.as_view()),
    path('<pk>', testDetailView.as_view()),
    path('<pk>/update/', testUpdateView.as_view()),
    path('<pk>/delete/', testDeleteView.as_view())
]
'''