from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
import tkinter as tk

dane = open('C:\\Users\\Admin\\PycharmProjects\\chat\\config.txt', 'r').read()
dane = dane.split('\n')
print(dane)


def spis():
    global bazatk
    global mailtk
    global haslotk
    bazatk = wpis1.get()
    mailtk = wpis2.get()
    haslotk = wpis3.get()
    newconfig = open('C:\\Users\\Admin\\PycharmProjects\\chat\\config.txt', 'w')
    newconfig.write(bazatk)
    newconfig.write('\n')
    newconfig.write(mailtk)
    newconfig.write('\n')
    newconfig.write(haslotk)

def zaladuj():
    global bazatk
    global mailtk
    global haslotk
    bazatk = dane[0]
    mailtk = dane[1]
    haslotk = dane[2]
    sygnalizacja3 = tk.Label(bg='green', width=10)
    sygnalizacja3.grid(row=3, column=1)
    print(dane)

def start_rulety():
    global l
    l=0
    okno.destroy()
    browse = webdriver.Chrome()

    browse.get('https://margobet.pl/a/roulette')

    email=mailtk
    haslo=haslotk

    time.sleep(2)

    przycisk = browse.find_element_by_xpath('/html/body/div[4]/div[2]')
    przycisk.click()

    time.sleep(2)
    logowanie=browse.find_element_by_xpath('/html/body/div[4]/div[3]/div[6]')
    logowanie.click()

    login=browse.find_element_by_xpath('//*[@id="email"]')
    login.send_keys(email)

    password = browse.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(haslo)

    time.sleep(15)
    while True:
        kasa = browse.find_element_by_xpath('/html/body/div[4]/div[3]/div[10]/div/div[1]').get_attribute('innerText')
        kasa = kasa.replace(',','')


        baza = int(kasa)
        print(baza)

        clear = browse.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div[4]/div/button[1]')

        kwota = browse.find_element_by_xpath('//*[@id="amount"]')
        clear.click()


        blue = browse.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div[5]/div[3]/div[1]/div')

        red = browse.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div[5]/div[1]/div[1]/div')
        timer = browse.find_element_by_xpath('//*[@id="roulette_timer"]').get_attribute('innerText')
        if int(timer)<15:
            kwota.send_keys(Keys.BACK_SPACE)
            kwota.send_keys(str(bazatk))
            if l%2==0:
                red.click()
                print('red')
                l=l+1
            else:
                blue.click()
                l=l+1
            time.sleep(int(timer)+10)
            print(kasa, baza)
        kasa = browse.find_element_by_xpath('/html/body/div[4]/div[3]/div[10]/div/div[1]').get_attribute('innerText')
        kasa = kasa.replace(',','')

        while int(kasa)<int(baza):
            kasa = browse.find_element_by_xpath('/html/body/div[4]/div[3]/div[10]/div/div[1]').get_attribute('innerText')
            kasa = kasa.replace(',','')
            timer = browse.find_element_by_xpath('//*[@id="roulette_timer"]').get_attribute('innerText')
            podw = browse.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div[4]/div/button[2]')
            time.sleep(1)
            if int(timer)<15:
                podw.click()
                print('red2')
                if l%2==0:
                    red.click()
                    l=l+1
                else:
                    blue.click()
                    l=l+1


                time.sleep(int(timer)+10)



    print('...',end='')
    input()

    browse.quit()

okno = tk.Tk()
okno.geometry('500x500')
okno.resizable(False, False)
okno.title('Chuj na szybie')
okno.config(bg='#fce1fb')

napisy1 = tk.Label(okno, text='Baza', width=20)
napisy1.grid(row=0, column=0)
napisy2 = tk.Label(okno, text='Mail', width=20)
napisy2.grid(row=0, column=1)
napisy3 = tk.Label(okno, text='Haslo', width=20)
napisy3.grid(row=0, column=2)


wpis1 = tk.Entry(okno, width=20)
wpis1.grid(row=1, column=0)
wpis2 = tk.Entry(okno, width=20)
wpis2.grid(row=1, column=1)
wpis3 = tk.Entry(okno, width=20)
wpis3.grid(row=1, column=2)

przycisk1 = tk.Button(text='Zatwierdź nowy config', width=20, command=spis)
przycisk1.grid(row=2, column=0)
przycisk2 = tk.Button(text='Wczytaj config', width=20, command=zaladuj)
przycisk2.grid(row=2, column=1)
przycisk3 = tk.Button(text='Start', width=20, command=start_rulety)
przycisk3.grid(row=2, column=2)


sygnalizacja1 = tk.Label(text='', bg='#fce1fb')
sygnalizacja1.grid(row=3,column=0)

sygnalizacja2 = tk.Label(text='', bg='red', width=10)
sygnalizacja2.grid(row=3, column=1)



tk.mainloop()

