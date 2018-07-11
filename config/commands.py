from base_config import BaseConfig


class CommandsConfig(BaseConfig):
    @property
    def approve(self):
        return self.config.get("commands", {}).get("approve")

    @property
    def disapprove(self):
        return self.config.get("commands", {}).get("disapprove")

    @property
    def pause(self):
        return self.config.get("commands", {}).get("pause")

    @property
    def resume(self):
        return self.config.get("commands", {}).get("resume")

    @property
    def stop(self):
        return self.config.get("commands", {}).get("stop")

    @property
    def status(self):
        return self.config.get("commands", {}).get("status")

    @property
    def info(self):
        return self.config.get("commands", {}).get("info")

    @property
    def help(self):
        return self.config.get("commands", {}).get("help")

    @property
    def add_admin(self):
        return self.config.get("commands", {}).get("add_admin")

    @property
    def delete_admin(self):
        return self.config.get("commands", {}).get("delete_admin")

    @property
    def edit_admin_pass(self):
        return self.config.get("commands", {}).get("edit_admin_pass")

    @property
    def clean_admin(self):
        return self.config.get("commands", {}).get("cleanadmin")

    @property
    def clean_errors_(self):
        return self.config.get("commands", {}).get("clean_errors")

    @property
    def clean_unknown(self):
        return self.config.get("commands", {}).get("clean_unknown")

    @property
    def chat_message(self):
        return self.config.get("commands", {}).get("chat_message")

    @property
    def token(self):
        return self.config.get("commands", {}).get("token")

    @property
    def message(self):
        return self.config.get("commands", {}).get("message")

    @property
    def message_admin(self):
        return self.config.get("commands", {}).get("message_admin")

    @property
    def send_errors(self):
        return self.config.get("commands", {}).get("errors")

    @property
    def send_unknown(self):
        return self.config.get("commands", {}).get("unknown")

    @property
    def set_group_chat(self):
        return self.config.get("commands", {}).get("set_group_chat")

    @property
    def auth_flickr(self):
        return self.config.get("commands", {}).get("auth_flickr")

    @property
    def edit_key(self):
        return self.config.get("commands", {}).get("edit_key")

    @property
    def edit_secret(self):
        return self.config.get("commands", {}).get("edit_secret")
