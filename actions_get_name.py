from typing import Any, List, Text, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetName(Action):
    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lang = domain.get("config", {}).get("language", "ru")
        name = tracker.get_slot("name")

        if name:
            message = f"Тебя зовут {name}, верно?" if lang == "ru" else f"Your name is {name}, right?"
        else:
            message = "Я пока не знаю, как тебя зовут." if lang == "ru" else "I don't know your name yet."

        dispatcher.utter_message(text=message)
        return [SlotSet("last_bot_message", message)]