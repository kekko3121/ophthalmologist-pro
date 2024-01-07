# ophthalmologist-pro

Tecnologie web project

## Project description

This project aims to create a progressive web app that can assist the ophthalmologist during the specialist examination by keeping track of the measurements taken. At the end of the eye examination, pwa generates the eye prescription automatically according to the data entered by the doctor. Once the prescription has been generated, it is always accessible through the portal by both the doctor and the customer.

We recommend viewing the video presentation to better understand the initial idea.
We thank you for your attention.

For more information you can see [here](https://www.canva.com/design/DAFzecUFK9o/LKdGAOtrRE8llqDKK-iyHQ/edit?utm_content=DAFzecUFK9o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton "Project slides")

## Installation

Before getting started, make sure you have the following dependencies installed:

Debian:

```bash
  sudo apt install wkhtmltopdf
```

or Arch

```bash
  yay -S wkhtmltopdf
```

Install my webapp with python

```bash
  python3 install pip
  cd ophthalmologist-pro
  pip3 install -r requirements.txt
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/kekko3121/ophthalmologist-pro.git
```

Go to the project directory

```bash
  cd ophthalmologist-pro/Web_Server/
```

Start the server

```bash
  gunicorn -b <ip>:<port> run:app
```

## Authors

- [@kekko3121](https://github.com/kekko3121)
- [@TonIann7](https://github.com/TonIann7)
- [@luajez](https://github.com/luajez)

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)