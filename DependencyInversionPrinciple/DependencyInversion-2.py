# befor

# class NewsPerson:
#     """This is a high-level module"""
#     @staticmethod
#     def publish(news: str) -> None:
#         """
#         :param news:
#         :return:
#         """
#         print(NewsPaper().publish(news=news))
# class NewsPaper:
#     """This is a low-level module"""
#     @staticmethod
#     def publish(news: str) -> None:
#         """
#         :param news:
#         :return:
#         """
#         print(f"{news} Hello newspaper")
# person = NewsPerson()
# print(person.publish("News Paper"))


# after 

class NewsPerson:
   """This is a high-level module"""
   @staticmethod
   def publish(news: str, publisher=None) -> None:
       print(publisher.publish(news=news))

class NewsPaper:
   """This is a low-level module"""
   @staticmethod
   def publish(news: str) -> None:
       print("{} news paper".format(news))

class Facebook:
   """This is a low-level module"""
   @staticmethod
   def publish(news: str) -> None:
       print(f"{news} - share this post on {news}")
       
person = NewsPerson()
person.publish("hello", NewsPaper())
person.publish("facebook", Facebook())