from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from usefulthings.models import Wont
from users.models import User


class WontTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.wont = Wont.objects.create(
            place="тест",
            time="07:00:00",
            action="тест",
            period=1,
            time_to_action=timedelta(seconds=60),
        )

    def test_wont_create(self):
        url = reverse("usefulthings:wont-create")
        data = {"place": "test",
                "time": "05:00:00",
                "action": "test",
                "period": 1,
                "time_to_action": timedelta(seconds=60)
                }
        response = self.client.post(url, data)
        print(response.json())
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Wont.objects.all().count(), 2)

    def test_wont_list(self):
        url = reverse("usefulthings:wont-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Wont.objects.all().count(), 1)

    def test_wont_retrieve(self):
        url = reverse("usefulthings:wont-retrieve", kwargs={"pk": self.wont.id})
        self.wont.owner = self.user
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.wont.action)

    def test_wont_partial_update(self):
        url = reverse("usefulthings:wont-partial-update", kwargs={"pk": self.wont.id})
        data_partial_update = {
            "time": "05:05:00",
            "time_to_action": timedelta(seconds=65)
        }
        response = self.client.patch(url, data_partial_update)
        print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time"), "05:05:00")

    def test_wont_delete(self):
        url = reverse("usefulthings:wont-delete", kwargs={"pk": self.wont.id})
        self.wont.owner = self.user
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Wont.objects.all().count(), 0)
