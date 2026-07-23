import requests


class CommentPublisher:

    def publish(self, comments_url, markdown, github_token):

        response = requests.post(

            comments_url,

            headers={

                "Authorization": f"Bearer {github_token}",

                "Accept": "application/vnd.github+json"

            },

            json={

                "body": markdown

            }

        )

        response.raise_for_status()

        return response.json()
