from datetime import datetime

import pytz
from django.contrib.auth.models import User
from django.test import TestCase

from Posts.models import Post


def create_test_post(title, offset, author):
    test_timestamp = datetime.timestamp(datetime.now(pytz.UTC))

    post = Post.objects.create(
        title=title,
        author=author,
        type=0,
        date_created=datetime.fromtimestamp(test_timestamp - offset, pytz.UTC)
    )
    print('Created new post at: {} ({})'.format(datetime.timestamp(post.date_created), post.date_created))


class SpammersTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user'
        )

    def tearDown(self):
        print('\nNow it is: {} ({})\n'.format(datetime.timestamp(datetime.now(pytz.UTC)), datetime.now(pytz.UTC)))

    def test_user_is_spammer(self):
        print('### Expect to be a spammer\n')

        create_test_post('Post 1', 90, self.test_user)
        create_test_post('Post 2', 80, self.test_user)
        create_test_post('Post 3', 10, self.test_user)
        create_test_post('Post 4', 5, self.test_user)

        result = Post.author_is_spammer(self.test_user.username)

        self.assertTrue(result)

    def test_user_is_no_spammer(self):
        print('### Expect to be no spammer\n')

        create_test_post('Post 1', 200, self.test_user)
        create_test_post('Post 2', 180, self.test_user)
        create_test_post('Post 3', 160, self.test_user)
        create_test_post('Post 4', 140, self.test_user)

        result = Post.author_is_spammer(self.test_user.username)

        self.assertFalse(result)
