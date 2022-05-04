# FAQ

* **Compile a smart contract**
  ```
  solc -o test.out --bin --ast-compact-json --asm test.sol
  ```
* **Download openzeppelin**
  ```
  git clone https://github.com/OpenZeppelin/openzeppelin-contracts.git
  ```
* **Build and run docker**
  ```
  sudo docker build --build-arg user=${USER} --build-arg uid=$(id -u ${USER}) -t eth .
  sudo docker run --ipc=host --security-opt apparmor:unconfined --device /dev/fuse --cap-add ALL -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=${DISPLAY} -h ${HOSTNAME} -v ${HOME}/.Xauthority:${HOME}/.Xauthority -v $(pwd)/:$(pwd) --net=host -it eth bash
  ```
