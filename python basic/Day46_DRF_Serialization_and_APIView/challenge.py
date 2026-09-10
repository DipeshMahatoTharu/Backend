"""
Day 46 Daily Challenge: Standalone DRF Serializer & APIView Controller Engine

Problem:
Implement a standalone Serializer class that supports:
1. Field validation and type casting (Integer, Char, Float).
2. Field-level `validate_<field>()` methods.
3. Object-level `validate()` method.
4. `.is_valid(raise_exception=True)` populating `.validated_data` or `.errors`.
5. `.save()` triggering `.create()` or `.update()`.
"""
from typing import Dict, Any, Optional

class ValidationError(Exception):
    def __init__(self, detail: Any):
        self.detail = detail
        super().__init__(str(detail))

class BaseSerializer:
    def __init__(self, instance: Any = None, data: Optional[Dict[str, Any]] = None):
        self.instance = instance
        self.initial_data = data
        self.validated_data: Dict[str, Any] = {}
        self.errors: Dict[str, str] = {}
        self._is_valid: Optional[bool] = None

    def is_valid(self, raise_exception: bool = False) -> bool:
        if self.initial_data is None:
            raise AssertionError("Cannot call is_valid() without data")

        self.errors.clear()
        self.validated_data.clear()

        fields = getattr(self, "fields", {})
        temp_data = {}

        # 1. Field extraction & basic types
        for fname, ftype in fields.items():
            if fname not in self.initial_data:
                self.errors[fname] = "This field is required."
            else:
                raw_val = self.initial_data[fname]
                try:
                    temp_data[fname] = ftype(raw_val)
                except (ValueError, TypeError):
                    self.errors[fname] = f"Invalid type for {ftype.__name__}."

        # 2. Field-level validate_<field>
        for fname, val in temp_data.items():
            validator = getattr(self, f"validate_{fname}", None)
            if validator:
                try:
                    temp_data[fname] = validator(val)
                except ValidationError as ve:
                    self.errors[fname] = str(ve.detail)

        # 3. Object-level validate
        if not self.errors:
            try:
                temp_data = self.validate(temp_data)
            except ValidationError as ve:
                self.errors["non_field_errors"] = str(ve.detail)

        if self.errors:
            self._is_valid = False
            if raise_exception:
                raise ValidationError(self.errors)
            return False

        self.validated_data = temp_data
        self._is_valid = True
        return True

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        return attrs

    def save(self) -> Dict[str, Any]:
        if not self._is_valid:
            raise AssertionError("You must call is_valid() before calling save().")
        if self.instance is not None:
            return self.update(self.instance, self.validated_data)
        return self.create(self.validated_data)

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def update(self, instance: Dict[str, Any], validated_data: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError


# Concrete Serializer
class ArticleSerializer(BaseSerializer):
    fields = {"title": str, "views": int, "is_published": bool}

    def validate_title(self, value: str) -> str:
        if len(value.strip()) < 5:
            raise ValidationError("Title must be at least 5 characters.")
        return value.strip()

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if attrs.get("views") < 0:
            raise ValidationError("Views cannot be negative.")
        return attrs

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        record = dict(validated_data)
        record["id"] = 101
        return record

    def update(self, instance: Dict[str, Any], validated_data: Dict[str, Any]) -> Dict[str, Any]:
        instance.update(validated_data)
        return instance


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Test Valid Create
    payload = {"title": "Mastering Django", "views": 50, "is_published": True}
    s = ArticleSerializer(data=payload)
    assert s.is_valid(raise_exception=True) is True
    assert s.validated_data["title"] == "Mastering Django"
    saved = s.save()
    assert saved["id"] == 101

    # 2. Test Field Validation Error
    bad_payload = {"title": "Tiny", "views": 10, "is_published": True}
    s_bad = ArticleSerializer(data=bad_payload)
    assert s_bad.is_valid() is False
    assert "at least 5 characters" in s_bad.errors["title"]

    # 3. Test Object-Level Validation Error
    neg_views = {"title": "Negative Views Post", "views": -5, "is_published": True}
    s_neg = ArticleSerializer(data=neg_views)
    assert s_neg.is_valid() is False
    assert "cannot be negative" in s_neg.errors["non_field_errors"]

    # 4. Test Update
    existing = {"id": 1, "title": "Old Title", "views": 100, "is_published": False}
    upd_payload = {"title": "Updated Brand New Title", "views": 150, "is_published": True}
    s_upd = ArticleSerializer(instance=existing, data=upd_payload)
    assert s_upd.is_valid() is True
    res_upd = s_upd.save()
    assert res_upd["title"] == "Updated Brand New Title"
    assert res_upd["id"] == 1

    print("All ArticleSerializer challenge tests passed successfully!")
