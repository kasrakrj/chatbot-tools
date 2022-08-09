from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_get_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course_id = tracker.slots["course_id"]
        student_id =  tracker.slots["student_id"]
        score = -1
        with open('/Users/kasrakaraji/RasaProjects/' + course_id + '.txt') as f:
            lines = f.readlines()
            for line in lines:
                [loop_student_id, loop_score] = line.split(' ')
                if student_id == loop_student_id:
                    score = loop_score

        if score == -1:
            dispatcher.utter_message(text="Score not found!")
        else:
            dispatcher.utter_message(text=str(score))
        return []