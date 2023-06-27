from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import reverse

class BlogPostTest(TestCase):
     @classmethod
     def setUpTestData(cls):
          cls.user=User.objects.create(username='user1')
          cls.post1=Post.objects.create(title="post1", text='this is my post', status=Post.STATUS_CHOICES[0][0], author=cls.user)   #published
          cls.post2=Post.objects.create(title="post2", text='this is my new post', status=Post.STATUS_CHOICES[1][0], author=cls.user)   #draft
    

     def test_post_model_str(self):
          self.assertEqual(str(self.post1.title),"post1")



     def test_post_list_url(self):
          response= self.client.get('/blog/')
          self.assertEqual(response.status_code, 200)

     def test_post_list_url_by_name(self):
          response=self.client.get(reverse('posts_list'))
          self.assertEqual(response.status_code, 200)

     def test_post_title_on_blog_list_page(self):
          response=self.client.get(reverse('posts_list'))
          self.assertContains(response, "post1")

     def test_post_detail_on_page(self):
          response=self.client.get(reverse('post_detail', args=[self.post1.id]))
          self.assertContains(response, "post1" )
          self.assertContains(response, self.post1.text)

     def test_post_detail_false_id_error(self):
          response= self.client.get('/blog/10/')
          self.assertEqual(response.status_code, 404)

     def test_post_list_Draft(self):
          response=self.client.get(reverse('posts_list'))
          self.assertNotContains(response, self.post2.text)
          self.assertContains(response, self.post1.text)

     def test_post_create_view(self):
          response=self.client.post(reverse('add_new_post'), {'title' : "post2", 'text' : 'this is my new post', 'status': 'drf', 'author':self.user.id} )
          self.assertEqual(response.status_code,302)
          self.assertEqual(Post.objects.last().title,"post2")
          self.assertEqual(Post.objects.last().text,'this is my new post')

     def test_post_update_view(self):
            response=self.client.post(reverse('post_update',args=[self.post2.id]), {'title':'moosa', 'text': 'akilo','status': 'pub', 'author':self.user.id})
            self.assertEqual(response.status_code,302)
            self.assertEqual(Post.objects.last().title,"moosa")
            self.assertEqual(Post.objects.last().text,'akilo')

     def test_post_delete_view(self):
            response=self.client.post(reverse('post_delete',args=[self.post2.id]))
            self.assertEqual(response.status_code,302)

     





   
             