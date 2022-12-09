from colorama import Fore

from config_reader import email, password
from pychatgpt import Options, Chat

chat_history = {}
options = Options()
options.track = False

chat: Chat = Chat(email=email, password=password, options=options)
if __name__ == "__main__":
    """
    Conversation_id and previous_convo_id in chat.ask() can be specified in chat.ask()
    """

    # Init
    answer, previous_convo, convo_id = None, None, None

    q1 = "HelloWorld"
    q2 = "What do the above words mean?"

    print(f"{Fore.BLUE}First question.")

    answer, previous_convo, convo_id = chat.ask(q1)
    print(f"{Fore.GREEN}you: {q1} \n"
          f"{Fore.CYAN}ChatGPT: {answer}, {previous_convo}, {convo_id}")

    """
    First question.
        you: HelloWorld 
        ChatGPT: Hello there! It's nice to meet you. Is there something specific you would like to talk about or discuss? I'm here to help with any questions you may have., 86c22f1d-58dd-43b4-981d-3bb120ab157b, f3102bb2-9213-45be-9b26-4ab96a342b6e
    """

    print(f"{Fore.WHITE}-----------------------------")
    # No conversation transfer
    print(f"{Fore.BLUE}No conversation transfer")

    answer = chat.ask(q2)
    print(f"{Fore.GREEN}you: {q2} \n"
          f"{Fore.CYAN}ChatGPT: {answer[0]}")

    """
    No conversation transfer
        you: What do the above words mean? 
        ChatGPT: The words "Assistant" and "OpenAI" in the first sentence refer to the Assistant, which is a large language model trained by OpenAI, a leading organization in the field of artificial intelligence research. The words "knowledge cutoff" and "current date" in the second sentence refer to the date up to which the Assistant has been trained and the current date, respectively. The phrase "browsing disabled" in the third sentence means that the Assistant does not have access to the internet and therefore cannot browse or search for information online.
    """

    print(f"{Fore.WHITE}-----------------------------")

    # Conversation take over available
    print(f"{Fore.BLUE}Conversation take over available")

    answer = chat.ask(q2, previous_convo_id=previous_convo, conversation_id=convo_id)
    print(f"{Fore.GREEN}you: {q2} \n"
          f"{Fore.CYAN}ChatGPT: {answer[0]}")

    """
    Conversation take over available
        you: What do the above words mean? 
        ChatGPT: The words "Hello World" are often used as a simple way to test the basic functionality of a new computer program or software. The words themselves don't have any specific meaning, but they are commonly used to start a conversation or introduce oneself to someone new. For example, you could say "Hello World, my name is John" to introduce yourself to someone. Is there something else you would like to know?
    """

    print(f"{Fore.WHITE}-----------------------------")

    pass
