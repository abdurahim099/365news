from django.db.models import manager

class CategoryManager(manager.Manager):
    def get_category(self,category_name):
        try:
            self.get(name_icontains = category_name)
        except Exception as e:
            return None
