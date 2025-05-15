class SeoMixin:
    meta_description = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta_description"] = self.get_meta_description()
        return context

    def get_meta_description(self):
        if self.meta_description:
            return self.meta_description

        if hasattr(self, "title_page"):
            return f"{self.title_page}. Актуальные рейтинги и сравнения электромобилей."

        if hasattr(self, "object"):
            return f"{self.object.title}. Полные характеристики, отзывы и сравнения."

        return "Информация об электромобилях: подробные характеристики."
