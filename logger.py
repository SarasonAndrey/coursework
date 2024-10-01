# from logging import DEBUG, StreamHandler, basicConfig, getLogger
# from unittest import result
#
# import FileHandler
#
# logger = getLogger()
# FORMAT = "%(asctime)s : %(name)s : %(levelname)s : %(massage)s"
# file_handler = FileHandler
# file_handler.setLevel(DEBUG)
# console = StreamHandler()
# console.setLevel(DEBUG)
# basicConfig(level=DEBUG, format=FORMAT)
# logger = getLogger(__name__)
#
#
# def start():
#     while True:
#         expression = input("Введите выражение для вычисления")
#         logger.debug("Exception is %s", expression)
#         if not expression:
#             logger.info("empty expression, stopping...")
#             break
#         result = calculate(expression)
#         if result is None:
#             logger.info("No result back, stopping...")
#             break
#
#
# def calculate(exp: str) -> str:
#     logger.debug("Get expression %s", exp)
#     try:
#         result = exp
#         logger.debug("Evaluated %s", exp)
#         return result
#     except Exception as e:
#         logger.error("Exception %s", e)
#         return None
#
#
# if __name__ == "__main__":
#     logger.info("start servis")
#     start()
#     logger.info("stop servis")
#     print(f"Result is {result}")
