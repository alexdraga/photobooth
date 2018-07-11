from base_config import BaseConfig


class FlickrSettingsConfig(BaseConfig):
    @property
    def request_token_url(self):
        return self.config.get("flickr", {}).get("request_token_url")

    @property
    def access_token_url(self):
        return self.config.get("flickr", {}).get("access_token_url")

    @property
    def upload_api_url(self):
        return self.config.get("flickr", {}).get("upload_api_url")

    @property
    def authorize_url(self):
        return self.config.get("flickr", {}).get("authorize_url")

    @property
    def key(self):
        return self.config.get("flickr", {}).get("key")

    @key.setter
    def key(self, value):
        self.config["flickr"]["key"] = value
        self.save_config()

    @property
    def secret(self):
        return self.config.get("flickr", {}).get("secret")

    @secret.setter
    def secret(self, value):
        self.config["flickr"]["secret"] = value
        self.save_config()

    @property
    def oauth_token(self):
        return self.config.get("flickr", {}).get("oauth_token")

    @oauth_token.setter
    def oauth_token(self, value):
        self.config["flickr"]["oauth_token"] = value
        self.save_config()

    @property
    def oauth_token_secret(self):
        return self.config.get("flickr", {}).get("oauth_token_secret")

    @oauth_token_secret.setter
    def oauth_token_secret(self, value):
        self.config["flickr"]["oauth_token_secret"] = value
        self.save_config()
