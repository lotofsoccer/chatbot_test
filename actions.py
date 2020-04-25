# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted
import pandas as pd
import json

class Actiontuvan(Action):

     def name(self) -> Text:
         return "action_tuvan_tochat"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


         with open('dmnganh.json', encoding="utf8") as f:
             data = json.load(f)

         columns = ["Nhóm ngành",
                "Mã số",
                "Tên ngành",
                "Mã tổ hợp",
                "Thời gian đào tạo",
                "Danh hiệu",
                "Chỉ tiêu dự kiến",
                "Điểm TT 2018",
                "Việc làm sau khi tốt nghiệp",
                "Tố chất cần có",
                "Lương"]
         op = "Tố chất cần có"
         nganh_new = tracker.get_slot("nganh_tc")
         df = pd.DataFrame(data, columns=columns)

         tn = df["Tên ngành"].tolist()

         tc = df["Tố chất cần có"].tolist()

         for i in df["Tên ngành"]:
             if (i == nganh_new):
                 for j in df:
                     if (j == op):
                         dispatcher.utter_message("Để học ngành {} thì {}".format(i,(tc[tn.index(nganh_new)])))
         return[]