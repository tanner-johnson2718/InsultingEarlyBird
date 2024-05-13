# InsultingEarlyBird

## Our Product and Our Vision
The insulting early bird is the only product on the market that can open your blind shades at 0530AM local time with up to 10ms accuracy and will yell encoouraging insults at you until you turn it off.

## Key Components of Our Tech Stack

Here at insulting early bird we pride ourselves on the most powerful tech stach to yet be assembled by humankind.

* Pi 4B 2gb
* Big Tree Tech skr mini e3 v3
* 2x Stepper w/ threaded rod w/ suffcient length to open blind shade
* Scrap Wood
* Plastic Junk
* [Todo link to Shade Interface Arm](..)
* [Todo link to Stepper Phase Syncnotron](..)

## Install / Config
* PI lite OS
* On pi use kauih to get Klipper, Mainsail, Mainsail
* Printer Cfg under `~/printer_data/config/printer.cfg'
* Follow [link](https://www.klipper3d.org/Installation.html) to install klipper firmware on skr.
  * [Extra skr e3 v3 instructions can be found in its config file](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/blob/master/firmware/V3.0/Klipper/SKR-mini-E3-V3.0-klipper.cfg)
  * Can Use ttyACM0 as dev
  * Use above skr mini e3 v3 cfg, but make temp ranges on extruder and heat bed like crazy ranges to avoid ADC range errors
  * Set Z Stepper to range of -1000 to 1000
  * Added following to cfg

```
[force_move]
enable_force_move: True
```
