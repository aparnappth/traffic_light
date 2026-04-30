# Traffic Light Project (Raspberry Pi)

This project simulates a basic traffic light using three LEDs connected to a Raspberry Pi.

## 🔧 Hardware Setup

### GPIO Pin Connections

| LED Color | GPIO Pin |
|----------|---------|
| Red      | GPIO 22 |
| Yellow   | GPIO 27 |
| Green    | GPIO 18 |

Each LED is connected with a **separate resistor (220Ω–330Ω)** to GND.

### Circuit

GPIO → LED → Resistor → GND

---

## ▶️ How to Run

```bash
python3 traffic_light.py
