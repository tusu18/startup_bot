# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
import requests
import urllib
import random
import pandas as pd
import json

c={"PS":"This is the most appealing source of financing, because you use your own money to jumpstart your business and don’t owe anyone else in the process\n Pros:\n \t You have total control of your business, and you may do as you please with your money \n \t There’s this satisfaction that you are using your own cash to fund the business.\n Cons: \n \t If the business fails, all the hard work that you had put into your savings will go to waste.\n \t You may miss out on otherwise valuable guidance and mentorship from angel investors and venture capitalists.\n","FF":"You can request your friends, family or close associates to help fund your business. This type of funding has more to do with the relationship itself, rather than the assessment of a feasible business plan. The aim of this type of funding is to help kick off a business to a point where it can seek and get other types of funding. \n Pros: \n Faster funding process and flexible payment methods. \n Cons: \n \t Family and friends provide the funding without assessing the viability of a business plan itself. \n \t Brings nothing to the table except for the initial capital investment.\n","CF":"This involves funding a business by taking small amounts of capital from a large number of people, usually via the internet. This type of funding makes use of the vast networks you’ve of your friends, family and colleagues via different social platforms to get the word out about the business, with the goal of attracting new investors.\n Pros: \n Has the potential of expanding a business by getting a pool of investors who can help raise funds.\n Cons: \n Requires time and dedication before results may be realized.\n","AI":"Angel investors are wealthy individuals who will provide funding in exchange for a share of equity in the business. Some investors work in groups and screen deals together before providing funds, while most work on their own.\n Pros: \n Angel investors can offer valuable advice and guidance since they have experience in the industry you’re in.\n Flexible business terms.\n Cons: \n You may be forced to give up control of your business to some extent.\n","VC":"Venture capitalists are investors who put in a considerable amount of money in exchange for equity in the business, and get returns when the business goes public or is acquired by another company. Venture capitalists are all about the money, and only invest in businesses that have the potential of providing good returns on their investment \n Pros:\n Venture capitalists not only provide funding, but can offer expertise and mentorship to help develop the business \n Venture capital funding gives the business immediate credibility and opens other doors to a wide network of important individuals, such as future investors and partners.\n Cons: \n You may be forced to give up a large chunk of your business due to the significant amount of funding provided.\n","BL":"Bank loans are a popular source of funding for many startups. Before applying for a bank loan, it’s important to ensure that you are well educated about the various options available, and the interest rates that come with each option.\n Pros: \n There are different funding options depending on your needs.\n The funding process is relatively quick if you qualify.\n You don’t have to give up control of your business.\n Cons: \n Requires a lot of documentation, which can be tiring and time-consuming.\n You need educate yourself about the best option available for you; otherwise, you might end up choosing a deal that will eventually hurt your business.\n The money has to be paid back whether the business succeeds or not, failing which may lead to loss of your assets, if any.\n","SBA": "This involves funding from a government administration devoted to assisting small businesses to succeed. SBA’s help small businesses get capital and ensures that a certain percentage of contracts are awarded to the small businesses.\n Pros: \n Helps improve the relationship between lenders and borrowers.\n Increased chances of obtaining a bank loan if the SBA loan is properly managed.\n Cons: \n Strict qualification guidelines.\n"}
d1=pd.read_csv("f_incub.csv")
df=pd.read_csv("mentor_finnnaal.csv")
class SubscribeUser(Action):
     def name(self):
         return "get_signup_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         subscribe = tracker.get_slot('sup')
         if subscribe == "signup":
             response = "You're successfully subscribed"
         dispatcher.utter_message(response)
         
         key = "7f61c1d316be4c15bdcd375fa8c4299d"
         url = "http://api.ipstack.com/check" +"?access_key=" + key
         response = requests.get(url).json()
         
         return [SlotSet("sup", subscribe)]
class ipaddrs(Action):
     def name(self):
         return "get_ip_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         key = "7f61c1d316be4c15bdcd375fa8c4299d"
         url = "http://api.ipstack.com/check" +"?access_key=" + key
         response = requests.get(url).json()
         if response['country_code']=="IN":
             ip=response['ip']
             city=response['city']
             zip=response['zip']
             region=response['region_name']
             reg_code=response['region_code']
         else:
             resp="Sorry you are not from India or else you are using VPN..please turn it off"
             dispatcher.utter_message(resp)
         return [SlotSet("ip", ip),SlotSet("city", city),SlotSet("zip", zip),SlotSet("rgname", region),SlotSet("regcode", reg_code)] 

class incubatorclose(Action):
     def name(self):
         return "get_incubator_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         city = tracker.get_slot('city')
         t=d1[d1['location'].str.contains(city.lower(), regex=False)]
         Incname=t["name"].iloc[0]
         Incloc=t["location"].iloc[0]
         Incarea=t["idea"].iloc[0]
         Incaccpt=t["acceptance_rate"].iloc[0]
         return [SlotSet("Incname", Incname),SlotSet("Incloc", Incloc),SlotSet("Incarea", Incarea),SlotSet("Incaccpt", Incaccpt)]


class mentorec(Action):
     def name(self):
         return "get_mentors_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         field = tracker.get_slot('ff')
         mentor_name=df[df["info"].str.contains(field,regex=False)]["name"].iloc[random.randint(0,5)]
         mentor_info=df[df["name"].str.contains(mentor_name,regex=False)]["area"].iloc[0]
         mentor_area=df[df["name"].str.contains(mentor_name,regex=False)]["info"].iloc[0]

         return [SlotSet("mentor_name", mentor_name),SlotSet("mentor_info", mentor_info),SlotSet("mentor_area", mentor_area)]


class asktyp(Action):
     def name(self):
         return "get_typ_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         typ = tracker.get_slot('typ')
         if str.lower(typ) == "mentor":
            response = "Hey Mentor thanks for hopping by"
         if str.lower(typ) == "startup":
                response = "Hey Mentee thanks for hopping by"
         dispatcher.utter_message(response)
         return [SlotSet("typ", typ)]         
class GetField(Action):
     def name(self):
         return "get_field_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
         field=tracker.get_slot("ff")
         response = "So your Field is {field}"
         dispatcher.utter_message(response)
         return [SlotSet("ff", field)]

class Stocksearch(Action):
    def name(self):
         return "get_stocks_now" 
    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
        user_stocks = tracker.get_slot('stocks')
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
        querystring = {"q":{user_stocks},"pageNumber":"1","pageSize":"4","autoCorrect":"true","safeSearch":"true"}
        headers = {
        'x-rapidapi-key': "4710f54048msh23d35c944cbfc54p1a6e59jsn022db5130eb0",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        results=response.json()
        p=[]
        for x in results["value"]:
            p.append([x["body"],x["url"]])
        response1 = "Take some info:\n{}".format(p[1][0],end="")
        dispatcher.utter_message(response1)
        dispatcher.utter_message(buttons = [
                {"payload": "{}".format(p[1][1],end=""), "title": "More Info"},
            ])
        return []
class Vcname(Action):
    def name(self):
        return "get_vc_now"
    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
        s=['R&S Major Firm-Paytm',
        'Softbank Major Firm-Supr Daily',
        'JJL Major Firm-Paytm',
        'Skillcity Major Firm-Country Delight',
        'Wayne Industries Major Firm-Calvision',
        'Stark Industries Major Firm-Rapido',
        'Caltech Major Firm-Stupisid',
        'Raghul Major Firm-SSBT',
        'DPITDS Major Firm-Rapido',
        'Lasket MAjor Firm-Nameo']
        vc = tracker.get_slot('vc')
        response="{}".format(*random.choices(s),end="")
        dispatcher.utter_message(response)
        return [SlotSet("vc", vc)] 
class Govinfo(Action):
    def name(self):
         return "get_scheme_now" 
    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
        user_stocks = tracker.get_slot('sch')
        import requests
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
        querystring = {"q":{user_stocks},"pageNumber":"1","pageSize":"4","autoCorrect":"true","safeSearch":"true"}
        headers = {
        'x-rapidapi-key': "4710f54048msh23d35c944cbfc54p1a6e59jsn022db5130eb0",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        results=response.json()
        p=[]
        for x in results["value"]:
            p.append([x["body"],x["url"]])
        response1 = "Take some info:\n{}".format(p[1][0],end="")
        dispatcher.utter_message(response1)
        dispatcher.utter_message(buttons = [
                {"payload": "{}".format(p[1][1],end=""), "title": "More Info"},
            ])

        return []

class Startupinfo(Action):
    def name(self):
         return "get_startup_now" 
    def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
        user_i = tracker.get_slot('strtp')
        url="https://api.data.gov.in/resource/59579351-613b-489e-b2e7-2b4740c3a941?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
        response = requests.request("GET", url)
        result=response.json()
        response=pd.DataFrame.from_records(result["records"]).head(5).to_json()
        dispatcher.utter_message(response)
        return [SlotSet("strtp", user_i)]        

class Fundinfo(Action):
     def name(self):
         return "get_fundinfo_now"
     def run(self, 
            dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text,Any]):
 # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
         fund = tracker.get_slot('funds')
         if str.lower(fund) == "personal savings":
             response = c["PS"]
         elif str.lower(fund) == "family and friends":
             response = c["FF"]
         elif str.lower(fund) == "crowdfunding":
             response = c["CF"]
         elif str.lower(fund) == "angel investors":
             response = c["AI"]
         elif str.lower(fund) == "venture capital":   
             response = c["VC"]
         elif str.lower(fund) == "bank loans":
             response = c["BL"]
         else:
             response = c["SBA"]
         response1=fund+" :"
         dispatcher.utter_message(response1)
         dispatcher.utter_message(response)
         return [SlotSet("funds", fund)]
