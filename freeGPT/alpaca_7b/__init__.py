import requests


class Completion:
    @staticmethod
    def create(prompt: str):
        """
        Creates a completion by sending a POST request to a remote server.

        Args:
            prompt (str): The prompt string to be sent for completion.

        Returns:
            str: The completion generated by the server.

        Raises:
            Exception: If unable to fetch the response from the server.
        """
        headers = {
            "Origin": "https://chatllama.baseten.co",
            "Referer": "https://chatllama.baseten.co/",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Length": "17",
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        }
        resp = requests.post(
            "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
            headers=headers,
            json={"prompt": prompt},
        ).json()
        try:
            return resp["completion"]
        except:
            raise Exception("Unable to fetch the response.")
