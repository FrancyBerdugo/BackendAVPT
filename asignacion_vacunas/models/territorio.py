from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class TerritorioManager(BaseUserManager):

    def create_territorio(self, username, password=None):      
        if not username:
            raise ValueError('Users must have an username')
        territorio = self.model(username=username)
        territorio.set_password(password)
        territorio.save(using=self._db)
        return territorio

    def create_superterritorio(self, username, password):        
        territorio  = self.create_territorio(
            username=username,
            password=password,
        )
        territorio.is_admin = True
        territorio.save(using=self._db)
        return territorio

def user_directory_path(instance, filename):
    return 'Profiles/{0}/{1}'.format(instance.title, filename)

class Territorio(AbstractBaseUser, PermissionsMixin):
    
    cod_territorio = models.IntegerField(primary_key=True, unique=True)
    username       = models.CharField('username', max_length = 20, unique=True)
    password       = models.CharField('password', max_length = 256, default='0')
    nom_territorio = models.CharField('nom_territorio', max_length = 20, default='0')

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = TerritorioManager()
    USERNAME_FIELD = 'username'
