<div style="text-align: center">
<img width="400" src=".github/img/logo.png" />
<h1>PyLabRobot</h1>
</div>

## What is PyLabRobot?

PyLabRobot is a hardware agnostic, pure Python library for lab automation.

Here's a quick example showing how to move 100uL of liquid from well A1 to A2:

```python
from pylabrobot import LiquidHandler
from pylabrobot.liquid_handling.backends import STAR

lh = LiquidHandler(backend=STAR())
lh.setup()
lh.load_layout("layout.json")

lh.pickup_tips(lh.get_resource("tips")["A1:H8"])
lh.aspirate(lh.get_resource("plate")["A1"], volume=100)
lh.dispense(lh.get_resource("plate")["A2"], volume=100)
lh.return_tips()
```

## Resources

### Documentation

[docs.pylabrobot.org](https://docs.pylabrobot.org)

- [Installation](https://docs.pylabrobot.org/installation.html)
- [Getting Started](https://docs.pylabrobot.org/basic.html)
- [API Reference](https://docs.pylabrobot.org/pylabrobot.html)

### Support

- [forums.pylabrobot.org](https://forums.pylabrobot.org) for questions and discussions.
- [GitHub Issues](https://github.com/pylabrobot/pylabrobot/issues) for bug reports and feature requests.

## Papers

- [A high-throughput platform for feedback-controlled directed evolution](https://www.biorxiv.org/content/10.1101/2020.04.01.021022v1), _preprint_

- [Flexible open-source automation for robotic bioengineering](https://www.biorxiv.org/content/10.1101/2020.04.14.041368v1), _preprint_

_Developed for the Sculpting Evolution Group at the MIT Media Lab_
