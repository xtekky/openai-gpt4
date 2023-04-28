from enum import Enum

from openai_rev import forefront
from openai_rev import openaihosted
from openai_rev import quora
from openai_rev import theb
from openai_rev import you


class Provider(Enum):
    """An enum representing  different providers."""

    You = 'you'
    Poe = 'poe'
    ForeFront = 'fore_front'
    Theb = 'theb'
    OpenAiHosted = 'openai_hosted'


class Completion:
    """This class will be used for invoking the given provider"""

    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        """
        Invokes the given provider with given prompt and addition arguments and returns the string response

        :param provider: an enum representing the provider to use while invoking
        :param prompt: input provided by the user
        :param kwargs:  Additional keyword arguments to pass to the provider while invoking
        :return: A string representing the response from the provider
        """
        if provider == Provider.Poe:
            return Completion.__poe_service(prompt, **kwargs)
        elif provider == Provider.You:
            return Completion.__you_service(prompt, **kwargs)
        elif provider == Provider.ForeFront:
            return Completion.__fore_front_service(prompt, **kwargs)
        elif provider == Provider.Theb:
            return Completion.__theb_service(prompt, **kwargs)
        elif provider == Provider.OpenAiHosted:
            return Completion.__openai_hosted(prompt, **kwargs)
        else:
            raise Exception('Provider not exist, Please try again')

    @staticmethod
    def __you_service(prompt: str, **kwargs) -> str:
        return you.Completion.create(prompt, **kwargs).text

    @staticmethod
    def __poe_service(prompt: str, **kwargs) -> str:
        return quora.Completion.create(prompt=prompt, **kwargs).text

    @staticmethod
    def __fore_front_service(prompt: str, **kwargs) -> str:
        return forefront.Completion.create(prompt=prompt, **kwargs).text

    @staticmethod
    def __theb_service(prompt: str, **kwargs):
        return ''.join(theb.Completion.create(prompt=prompt))

    @staticmethod
    def __openai_hosted(prompt: str, **kwargs):
        return openaihosted.Completion.create(
            systemprompt=kwargs.get('systemprompt', ''), text=prompt, assistantprompt=kwargs.get('assistantprompt', '')
        ).text
