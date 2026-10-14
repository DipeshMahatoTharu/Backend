# Day 46 — Django REST Framework (DRF) Serializers & `APIView`

## 🎯 Learning Objectives
- Understand the core purpose of Serializers: converting complex Django Model instances into native Python datatypes (which easily render into JSON) and deserializing JSON payloads back into validated Python dictionaries.
- Compare `serializers.Serializer` (explicit field definitions) vs `serializers.ModelSerializer` (auto-generated from models).
- Master the validation lifecycle: field-level `validate_<fieldname>()` and object-level `validate()`.
- Master `.is_valid(raise_exception=True)`, `.save()`, `.create()`, and `.update()`.
- Build clean, stateless API endpoints by subclassing `rest_framework.views.APIView`.

---

## 📚 Core Backend Concepts

### 1. The Serialization & Deserialization Two-Way Street
- **Serialization (Read)**: `Model Instance -> Serializer(instance) -> serializer.data -> JSON Response`.
- **Deserialization (Write)**: `JSON Request -> Serializer(data=request.data) -> is_valid() -> serializer.save() -> Database Record`.

### 2. Validation Flow in DRF
```python
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate(self, attrs):
        if "free" in attrs.get("title", "").lower() and attrs.get("price") > 0:
            raise serializers.ValidationError("Products with 'free' in title must have price 0.")
        return attrs
```

### 3. Subclassing `APIView`
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Deconstruct Serializers, validation lifecycles, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build serializers and APIView dispatchers in [`practice.py`](practice.py), and fix serialization bugs in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the DRF Serializer & APIView Controller in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
