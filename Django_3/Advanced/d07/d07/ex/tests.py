from django.test import TestCase
from ex.models import User, Articles, UserFavoriteArticle
from django.urls import reverse
from django.utils.translation import activate
from django.conf import settings
from django.core.exceptions import ValidationError

class PublishViewTest(TestCase):
    def test_logged_out_user(self):
        """Check if a user is redirected after trying to access to publish url without logging"""
        activate('en')
        
        publish_url = reverse('publish')
        response = self.client.get(publish_url)
        login_url = f"{settings.LOGIN_URL}?next={publish_url}"
        self.assertRedirects(response, login_url, status_code=302, target_status_code=302)

class PublicationViewTest(TestCase):
    def test_logged_out_user(self):
        """Check if a user is redirected after trying to access to publications url without logging"""
        activate('en')
        
        publish_url = reverse('publication')
        response = self.client.get(publish_url)
        login_url = f"{settings.LOGIN_URL}?next={publish_url}"
        self.assertRedirects(response, login_url, status_code=302, target_status_code=302)
        
class FavouritesViewTest(TestCase):
    def setUp(self):
        """Create two users with an article create by the first user"""
        self.user_one = User.objects.create_user(
            username='user_1',
            password='1234',
        )
        self.user_one.save()
        
        self.user_two = User.objects.create_user(
            username='user_2',
            password='1234',
        )
        self.user_two.save()
        
        self.article = Articles.objects.create(
            title='Article 1',
            synopsis='Synopsis 1',
            content='Content 1',
            author_id=self.user_one.id,
        )
        self.article.save()
        
    def test_logged_out_user(self):
        """Check if a user is redirected after trying to access to favourites url without logging"""
        activate('en')
        
        publish_url = reverse('favourites')
        response = self.client.get(publish_url)
        login_url = f"{settings.LOGIN_URL}?next={publish_url}"
        self.assertRedirects(response, login_url, status_code=302, target_status_code=302)
        
    def test_only_one_favourite(self):
        """Check if a user can only add one favourite article"""
        activate('en')
        
        self.client.login(username='user_2', password='1234')
        
        response = self.client.post(reverse('articles'), {'article_id': self.article.id, 'action': 'add'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UserFavoriteArticle.objects.filter(user=self.user_two, article=self.article).count(), 1)
                   
        with self.assertRaises(ValidationError) as context:
            self.client.post(reverse('articles'), {'article_id': self.article.id, 'action': 'add'})
            
        expected_msg = ["Error: ['This article is already in your favourites']"]
        self.assertEqual(str(context.exception), str(expected_msg))
                     
class RegisterViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='test',
            password='1234',
        )
        user.save()
    def test_access_logged_in(self):
        """Check a user cannot access to the register form when logged in"""
        activate('en')
        
        self.client.login(username='test', password='1234')
        register_url = reverse('register')
        response = self.client.get(register_url)
        self.assertEqual(response.status_code, 403)