
from django import forms

from .models import Car, CarBody, Drive, Segment

EMPTY_CHOICE = [("", "-----")]


class FilterForm(forms.ModelForm):
    performance__drive_id = forms.ChoiceField(
        label="Привод",
        choices=EMPTY_CHOICE,
        required=False,
    )
    miscellaneous__segment_id = forms.ChoiceField(
        label="Сегмент",
        choices=EMPTY_CHOICE,
        required=False,
    )
    miscellaneous__car_body__id = forms.ChoiceField(
        label="Кузов",
        choices=EMPTY_CHOICE,
        required=False,
    )

    class Meta:
        model = Car
        fields = ("manufacturer",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["performance__drive_id"].choices = EMPTY_CHOICE + [
            (drive.id, drive.title)
            for drive in Drive.objects.order_by("title")
        ]

        self.fields["miscellaneous__segment_id"].choices = EMPTY_CHOICE + [
            (segment.id, f"{segment.title} - {segment.char_class}")
            for segment in Segment.objects.order_by("title")
        ]

        self.fields["miscellaneous__car_body__id"].choices = EMPTY_CHOICE + [
            (body.id, body.title)
            for body in CarBody.objects.order_by("title")
        ]
