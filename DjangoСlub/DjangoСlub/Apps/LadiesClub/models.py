from django.db import models

class News(models.Model):
    news_header = models.CharField(verbose_name = 'Заголовок', max_length = 100, blank=False)
    news_text = models.TextField(verbose_name = 'Основной текст', blank=False)
    news_dates = models.TextField(verbose_name = 'Даты проведения', blank=False)
    news_image = models.ImageField(verbose_name = 'Превью', upload_to='images/', blank=False)

    def __str__(self):
        return self.news_header

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
