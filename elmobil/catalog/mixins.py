from django.db import models


class VerboseNamePluralMixin:
    @property
    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural


class StrTitleMixin:
    def __str__(self):
        return str(self.title)


class IterMixin:
    def __iter__(self):
        for field in self._meta.fields:
            name = field.verbose_name
            value = field.value_to_string(self)
            if name == "ID" or value == "None":
                continue
            if value == "True":
                value = "✓"
            elif value == "False":
                value = "✗"
            if isinstance(field, models.ForeignKey):  # check ForeignKey
                field_name = field.name
                value = getattr(self, field_name)
            yield f"{name}:   {value}   {None or field.help_text}"
