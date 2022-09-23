from django.db import models

# Create your models here.

class StickerPack(models.Model):
    name = models.CharField(null=False, max_length=60, unique=True)
    price = models.IntegerField()
    user = models.ForeignKey("accounts.User", null=False, on_delete=models.CASCADE)


class Sticker(models.Model):
    sticker_pack = models.ForeignKey("stickers.StickerPack", null=False, on_delete=models.CASCADE)
    image_url = models.CharField(null=False, max_length=176)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sticker_pack', 'image_url'], name='unique_sticker'),
        ]


class UserSticker(models.Model):
    sticker_pack = models.ForeignKey("stickers.StickerPack", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", null=False, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'sticker_pack'], name='unique_user_sticker'),
        ]