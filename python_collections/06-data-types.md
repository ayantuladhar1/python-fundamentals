# Built-in Data Types
Variables can store data of different types and different types can do different things.
Python has the following data types built-in by default, in these categories.

|Text Type|str|
|---------|---|
|Numeric Types| int, float|
|Sequence Types| list, tuple|
|Mapping Type| dict|
|Set Types| set|
|Boolean Type| bool|


|Example | Data Type|
|----------|------------|
|x = "Hello World" | str |
|x = 20 | int |
|x = 20.5 |	float |
|x = 1j |complex |
|x = ["apple", "banana", "cherry"] | list |
|x = ("apple", "banana", "cherry") | tuple |
|x = range(6) | range |
|x = {"name" : "John", "age" : 36} | dict |
|x = {"apple", "banana", "cherry"} | set |
|x = frozenset({"apple", "banana", "cherry"})| frozenset|
|x = True |	bool |
|x = b"Hello" | bytes|
|x = bytearray(5)| bytearray|
|x = None| NoneType|

<img width="983" height="194" alt="image" src="https://github.com/user-attachments/assets/2f0d8a27-35e7-4e08-abc3-30c0bc546ac8" />

<img width="969" height="218" alt="image" src="https://github.com/user-attachments/assets/b0c44912-824c-4c3e-8965-118a9741e5d2" />

<img width="1009" height="229" alt="image" src="https://github.com/user-attachments/assets/7d5d519d-d860-482b-8c9c-26cff6e8e1b1" />

<img width="1013" height="225" alt="image" src="https://github.com/user-attachments/assets/06cd1501-6a2c-47af-9e79-f7ec06318490" />

<img width="1184" height="210" alt="image" src="https://github.com/user-attachments/assets/e66676ba-0dfa-42f1-ab85-23053088ed11" />

<img width="1188" height="220" alt="image" src="https://github.com/user-attachments/assets/dcad8d20-a9bd-4b87-adc3-492895adf198" />

<img width="1195" height="222" alt="image" src="https://github.com/user-attachments/assets/c6b73ee2-6e7f-4d78-9960-9c9f258adc11" />

<img width="1161" height="206" alt="image" src="https://github.com/user-attachments/assets/60964fef-6ddb-4cc4-8aae-9396895a9b03" />

<img width="1189" height="221" alt="image" src="https://github.com/user-attachments/assets/bf9a9cee-768c-46f6-8ee3-ed53bfd2c42e" />

<img width="1338" height="222" alt="image" src="https://github.com/user-attachments/assets/db24ce65-25a9-4efc-a260-bbfbd5a1cdc4" />

<img width="995" height="219" alt="image" src="https://github.com/user-attachments/assets/e3292957-816b-499e-85bc-00c94592f287" />

<img width="1259" height="228" alt="image" src="https://github.com/user-attachments/assets/aa098038-a8c6-46f2-875d-98e068925574" />

<img width="1092" height="234" alt="image" src="https://github.com/user-attachments/assets/ad4c7828-7fa2-4ba6-9e2c-32afa8c2780d" />

<img width="1036" height="230" alt="image" src="https://github.com/user-attachments/assets/41518a44-38b2-4c31-b129-284b80114932" />

## Setting the Specific Data Type
If you want to specify the data type, you can use thew following constructor functions:

|Example | Data Type|
|----------|------------|
|x = str("Hello World")| str|
|x = int(20)| int|
|x = float(20.5)| float|
|x = complex(1j)| complex|
|x = list(("apple", "banana", "cherry"))| list|
|x = tuple(("apple", "banana", "cherry"))| tuple|
|x = range(6)| range|
|x = dict(name = "John", age = 36)| dict|
|x = set(("apple", "banana", "cherry"))| set|
|x = frozenset(("apple", "banana", "cherry"))| frozenset|
|x = bool(5)| bool|
|x = bytearray(5)| bytes|
|x = memoryview(bytes(5))| memoryview|

<img width="963" height="225" alt="image" src="https://github.com/user-attachments/assets/655106be-54a4-43a2-8172-d813cd297eb0" />

<img width="971" height="225" alt="image" src="https://github.com/user-attachments/assets/e6651faa-f2c3-4cd5-94d2-899a9584e3f8" />

<img width="1000" height="228" alt="image" src="https://github.com/user-attachments/assets/d65c7a55-d1a7-44e0-a9d9-1ea1fc2794e4" />

<img width="1044" height="233" alt="image" src="https://github.com/user-attachments/assets/f412a195-1903-464b-ac2a-636dc2dc3183" />

<img width="1178" height="206" alt="image" src="https://github.com/user-attachments/assets/22144732-1076-4c3a-9119-0feb7cb73fe9" />

<img width="1189" height="236" alt="image" src="https://github.com/user-attachments/assets/80758740-0510-48c0-a434-7b90eca19f28" />

<img width="1084" height="231" alt="image" src="https://github.com/user-attachments/assets/ab19ed3e-e942-4b52-8d62-5ec22b0ec90b" />

<img width="1149" height="222" alt="image" src="https://github.com/user-attachments/assets/5882d5c6-691c-435f-8db1-f6cb2ffbf29b" />

<img width="1182" height="231" alt="image" src="https://github.com/user-attachments/assets/b69b0ad0-24c9-4471-b218-9de4b2a08089" />

<img width="1340" height="222" alt="image" src="https://github.com/user-attachments/assets/f4e5746d-dfdc-45f2-858f-9cdde98bed9e" />

<img width="974" height="218" alt="image" src="https://github.com/user-attachments/assets/1c7787c4-5e4e-4091-92dc-c9683ad042e2" />

<img width="1107" height="224" alt="image" src="https://github.com/user-attachments/assets/6fa4b069-ad2a-4c67-a0e1-be8136fc4b27" />

<img width="1246" height="220" alt="image" src="https://github.com/user-attachments/assets/2e886d9b-4605-41b4-8d8a-7271b39f14dc" />

<img width="1080" height="207" alt="image" src="https://github.com/user-attachments/assets/8ed5f2cf-6838-4217-a354-422621d61ec4" />
