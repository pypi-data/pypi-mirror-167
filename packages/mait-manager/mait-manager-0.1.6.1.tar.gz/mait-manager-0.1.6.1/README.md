# mait: package manager for text adventure games.
![154_mait](https://user-images.githubusercontent.com/66521670/189254832-397db858-b949-4ffa-9593-c041cebf3a7b.gif)

### Installing is by the PIP manager [Linux]
```commandline
pip3 install mait-manager
```
### Similar for [Windows]
```commandline
py -m pip install mait-manager
```
***You invoke mait via CLI by using the following:***
```commandline
mait --help
```

# uploading.
[![upload-mait.gif](https://i.postimg.cc/BvKq5Gjq/upload-mait.gif)](https://postimg.cc/B8J9sk5y)
The above demonstrates how to upload a single file **(You can now upload folders in 0.1.5.4v!!!)**
### Uploading.
```commandline
mait upload
```
Code must be source code! Compiled sources are not allowed!
### Providing a JSON.
```json
{
  "name": "Donuts!!!",
  "short": "I do donuts",
  "long": "Now this is a long description.",
  "creator": "@Porplax",
  "exec": "python3 donut.py"
}
```
A JSON provides the command to compile/or interpret the code & **is required**.

You must put it in the parent directory of your project.