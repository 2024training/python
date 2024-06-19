# import datetime
# from django.test import TestCase
# from .models import Diary
# from django.contrib.auth.models import User

# class DiaryModelTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser', password='password')

#     def test_diary_creation(self):
#         '''ユーザーが設定されたか、タイトル、本文が正しいか'''
#         Diary.objects.create(user=self.user, title='A', text='B')
#         diary = Diary.objects.get(title='A')

#         self.assertEqual(diary.title, 'A')
#         self.assertEqual(diary.text, 'B')
#         self.assertEqual(diary.user, self.user)

#     def test_diary_has_date(self):
#         '''本文が正しいか、日付が設定されているか'''
#         Diary.objects.create(user=self.user, title='C', text='D')
#         diary = Diary.objects.get(title='C')
#         self.assertEqual(diary.text, 'D')
#         self.assertIsInstance(diary.date, datetime.date)

#     def test_save_and_retrieve(self):
#         '''タイトルが正しいか、本文が正しいか'''
#         Diary.objects.create(user=self.user, title='E', text='F')
#         diary = Diary.objects.get(title='E')
#         self.assertEqual(diary.title, 'E')
#         self.assertNotEqual(diary.title, 'zzz')
#         self.assertEqual(diary.text, 'F')

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Diary

class DiaryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # テストに必要な初期データのセットアップ
        user = get_user_model().objects.create_user(username='testuser', password='12345')
        Diary.objects.create(title='Test Diary', text='This is a test diary entry', user=user)

    def test_diary_content(self):
        '''タイトルの確認'''
        diary = Diary.objects.get(title='Test Diary')
        expected_object_name = f'{diary.title}'
        self.assertEqual(expected_object_name, 'Test Diary')

    def test_diary_date_default(self):
        '''日付の確認'''
        diary = Diary.objects.get(title='Test Diary')
        expected_date = timezone.now().date()
        self.assertEqual(diary.date, expected_date)

    def test_diary_updated_at_blank_null(self):
        '''更新日時の確認'''
        diary = Diary.objects.get(title='Test Diary')
        self.assertIsNone(diary.updated_at)

    def test_diary_user_relationship(self):
        '''usernameの確認'''
        diary = Diary.objects.get(title='Test Diary')
        self.assertEqual(diary.user.username, 'testuser')

    def test_diary_str_method(self):
        '''文字列表現の確認'''
        diary = Diary.objects.get(title='Test Diary')
        self.assertEqual(str(diary), diary.title)