# Day 47 — DRF Generic Views, `ModelViewSet` & Routers

## 🎯 Learning Objectives
- Master the view hierarchy in DRF: `APIView` -> `GenericAPIView` -> Concrete Generic Views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) -> `ModelViewSet`.
- Master the standard CRUD actions of `ModelViewSet`: `list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`.
- Add custom non-CRUD endpoints using the `@action` decorator (`detail=True` vs `detail=False`).
- Master DRF Routers (`DefaultRouter` and `SimpleRouter`) to eliminate manual URL pattern declarations.
- Understand when to use `ModelViewSet` (standard resources) vs when to avoid it (complex domain actions).

---

## 📚 Core Backend Concepts

### 1. The Power of `ModelViewSet`
A single class handles all standard REST operations:
```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Custom action: POST /api/v1/articles/{id}/publish/
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.is_published = True
        article.save()
        return Response({"status": "Article published"})

    # Custom action: GET /api/v1/articles/recent/
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_articles = self.get_queryset().filter(is_published=True)[:5]
        serializer = self.get_serializer(recent_articles, many=True)
        return Response(serializer.data)
```

### 2. Automatic Routing with `DefaultRouter`
```python
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
```
`DefaultRouter` automatically generates 6 standard endpoints:
- `GET /api/v1/articles/` (`list`)
- `POST /api/v1/articles/` (`create`)
- `GET /api/v1/articles/{pk}/` (`retrieve`)
- `PUT /api/v1/articles/{pk}/` (`update`)
- `PATCH /api/v1/articles/{pk}/` (`partial_update`)
- `DELETE /api/v1/articles/{pk}/` (`destroy`)

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Deconstruct ViewSets, Routers, `@action`, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build ViewSet dispatchers in [`practice.py`](practice.py), and fix router traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Mini-DRF ModelViewSet & Router Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
