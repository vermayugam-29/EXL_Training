import threading
import time


#-------------------------------------------------
#-------------Without Locking (less optimal)------
#-------------------------------------------------
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            time.sleep(0.1)
            print(f"[{threading.current_thread().name}] - Creating new object.")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# -------------------------------------------------
# -------------With Locking (more optimal)---------
# -------------------------------------------------
class Singleton_2:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                time.sleep(0.1)
                print(f"[{threading.current_thread().name}] - Creating new object.")
                cls._instance = super(Singleton_2, cls).__new__(cls)
            return cls._instance

        return cls._instance


# -------------------------------------------------
# With Locking and 2 if conditions (most optimal)--
# -------------------------------------------------
class Singleton_3:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    time.sleep(0.1)
                    print(f"[{threading.current_thread().name}] - Creating new object.")
                    cls._instance = super(Singleton_3, cls).__new__(cls)
                return cls._instance

        return cls._instance


def access_broken_singleton():
    instance = Singleton_3()
    print(f"[{threading.current_thread().name}] Instance ID: {id(instance)}")


threads = []

for i in range(10):
    t = threading.Thread(target=access_broken_singleton, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()
