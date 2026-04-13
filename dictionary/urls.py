from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet, WordViewSet, PhraseViewSet, CategoryViewSet, CrossReferenceViewSet

router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'words', WordViewSet)
router.register(r'phrases', PhraseViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'crossreferences', CrossReferenceViewSet)

urlpatterns = router.urls