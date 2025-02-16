import requests
import unittest
from unittest.mock import Mock, patch


class UserService:
    def get_user_data(self, user_id):
        response = requests.get(f"https://example.com/users/{user_id}")
        return response.json()


def main():
    userService = UserService()
    print(userService.get_user_data(1))


class TestUserService(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_data(self, mock_get):
        # モックのレスポンスを設定
        mock_response = Mock()
        mock_response.json.return_value = {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
        }
        mock_get.return_value = mock_response

        # テスト実行
        service = UserService()
        result = service.get_user_data(1)

        # 検証
        self.assertEqual(result["name"], "Test User")

        # APIコール検証
        mock_get.assert_called_once_with("https://example.com/users/1")

    @patch("requests.get")
    def test_api_error_handling(self, mock_get):
        # HTTPエラーをシミュレート
        mock_get.side_effect = requests.exceptions.HTTPError("Not Found")

        service = UserService()

        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_user_data(999)


if __name__ == "__main__":
    main()
