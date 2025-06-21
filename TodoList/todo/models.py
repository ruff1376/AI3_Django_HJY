from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICE = [
        ('WAIT', '대기'),
        ('ING', '진행'),
        ('DONE', '완료'),
    ]
    
    no = models.AutoField(primary_key=True)     # 자동 증가 필드(PK)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(
                        max_length=20,
                        choices=STATUS_CHOICE,
                        default='WAIT'
                        )
    is_completed = models.BooleanField(default=False)   # 할 일 완료 여부
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # 상태에 따라 is_completed 자동 설정
        if self.status == 'DONE':
            self.is_completed = True
        else:
            self.is_completed = False
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} : {}".format(self.title, self.status)