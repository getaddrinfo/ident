from ident.lib.validation import Strict

class CreateWebhook(Strict):
    destination_url: str

    # TODO: filters