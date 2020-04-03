# Screen Sharing app using socket with Transfer Control Protocol (TCP)

This repository provides a simple python implementation of sharing screen of you computer.

**SETUP**

- Clone this repository to your local machine using
```
git clone https://github.com/anirudhganwal06/remote-me.git
cd remote-me
```

- Following libraries should be already installed on your machine
  - cv2 `pip install opencv-python`
  - mss `pip install mss`
  - numpy `pip install numpy`

- Now run `python user.py` to run the server(user) whose screen needs to be shared.
- After running the server, run `python controller.py` for connecting it to the user server already running at port 3000.
- The connection is set and user should start sharing its screen in a _Controller Screen_ window.
