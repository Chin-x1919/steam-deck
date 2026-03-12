# steam-deck
stupidly build stream deck form pico and push button

idea is if button is push pico will sent F13 or something like that to keyboard and pc software side will detect and
sent run this works on mac on linux it should works but on windows? noidea

---

## Demo

https://github.com/user-attachments/assets/3b0e0bc4-b9ed-4de4-8874-fb506a8a25e8

---

## What you need

Hardware:
- raspberry pi pico
- breadboard
- push button or whatever item that you can interact with and it can short 2 switch
- some wire

Software:
- whatever IDE(nanno kate vscode notepad whatever)
- curcit python
- adafruit_hid lib

---

## How?

- install curcit python into pico
- coppy my code and past it on pico
- connect this(hardware)

  
| Pico | Hardware1 | Hardware2 |
| --- | ----------- | -------- |
| GP2 | Push button | GND(LOW) |
| GP3 | Push button | GND(LOW) |
| GP4 | Push button | GND(LOW) |
| GP5 | Push button | GND(LOW) |

- install my custom software
- boom done

---

License MIT
