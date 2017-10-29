from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
from .models import *


# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_published_recently_future(self):
        q = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertIs(q.was_published_recently(), False)

    def test_was_published_recently_past(self):
        q = Question(pub_date=timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59))
        self.assertIs(q.was_published_recently(), True)

    def test_was_published_recently_recent(self):
        q = Question(
            pub_date=timezone.now() - datetime.timedelta(days=1, seconds=1))
        self.assertIs(q.was_published_recently(), False)


def create_question(question_text, days):
    '''create question with the given text and published the ginven number of days offsets to now'''
    return Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days))


class QuetionIndexViewTests(TestCase):
    def test_no_question(self):
        r = self.client.get(reverse('polls:index'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'No polls are available.')
        self.assertQuerysetEqual(r.context['latest_question_list'], [])

    def test_past_question(self):
        q = create_question('past question', -1)
        r = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(r.context['latest_question_list'],
                                 ['<Question: past question>'])

    def test_future_question(self):
        q = create_question('future question', 1)
        r = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(r.context['latest_question_list'], [])

    def test_future_and_past_question(self):
        q = create_question('future question', 1)
        qq = create_question('past question', -1)
        r = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(r.context['latest_question_list'],
                                 ['<Question: past question>'])

    # multiple question


class QuestionDetailTest(TestCase):
    def test_future_question(self):
        q = create_question('future question', 1)
        r = self.client.get(reverse('polls:detail', args=(q.id, )))
        # should be 404
        self.assertEqual(r.status_code, 404)

    def test_past_question(self):
        q = create_question('past question', -1)
        r = self.client.get(reverse('polls:detail', args=(q.id, )))
        self.assertContains(r, 'past question')
