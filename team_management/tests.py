from django.test import TestCase


class TestUserProfile(TestCase):
    def setUp(self):
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "email@example.com"
        }

    def test_create_user(self):
        response = self.client.post('/api/user/', self.user_data)
        self.assertEqual(response.status_code, 201)

    def test_create_user_with_existing_email(self):
        self.client.post('/api/user/', self.user_data)
        response = self.client.post('/api/user/', self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_get_user(self):
        response = self.client.post('/api/user/', self.user_data)
        user_id = response.data['pk']
        response = self.client.get(f'/api/user/{user_id}')
        self.assertEqual(response.status_code, 200)


class TestTeam(TestCase):
    def setUp(self):
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "email@example.com"
        }
        self.team_data = {
            "name": "Team 1",
            "users": []
        }
        self.user = self.client.post('/api/user/', self.user_data).data

    def test_create_team(self):
        response = self.client.post('/api/team/', self.team_data)
        self.assertEqual(response.status_code, 201)

    def test_create_team_with_users(self):
        self.team_data['users'] = [self.user['pk']]
        response = self.client.post('/api/team/', self.team_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(self.user, response.data['users'])

    def test_create_team_with_existing_name(self):
        self.client.post('/api/team/', self.team_data)
        response = self.client.post('/api/team/', self.team_data)
        self.assertEqual(response.status_code, 400)

    def test_get_team(self):
        response = self.client.post('/api/team/', self.team_data)
        team_id = response.data['pk']
        response = self.client.get(f'/api/team/{team_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_team(self):
        response = self.client.post('/api/team/', self.team_data, content_type='application/json')
        team_id = response.data['pk']
        self.team_data['pk'] = team_id
        self.team_data['name'] = 'Team 2'
        response = self.client.put('/api/team/', self.team_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Team 2')

    def test_remove_users_from_team(self):
        self.team_data['users'] = [self.user['pk']]
        response = self.client.post('/api/team/', self.team_data)
        team_id = response.data['pk']
        self.team_data['pk'] = team_id
        self.team_data['users'] = []
        response = self.client.put('/api/team/', self.team_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['users'], [])


if __name__ == "__main__":
    import unittest

    unittest.main()
