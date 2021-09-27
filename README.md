# Publisher

Publiser is a Python MQTT publisher for an simple applcation that can run in multiple clients.

## Installation

Clone this repo `git clone https://github.com/er-jpg/mqtt-publisher`.

Install the depencies using pip.

```bash
pip install cayenne-mqtt paho-mqtt python-dotenv
```

Create a new `.env` file using the example on the repo. And the variables from the new device on the cayenne website.

## Usage

Run the command using the first args as the `client_id` in you cayenne device.

```bash
./publisher.py "<CLIENT_ID>"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
