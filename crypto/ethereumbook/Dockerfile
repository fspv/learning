FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y software-properties-common curl sudo

# Ethereum packages
RUN add-apt-repository ppa:ethereum/ethereum
RUN apt-get update
RUN apt-get install -y solc ethereum

# Nodejs packages
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

# Install truffle
ENV NODE_OPTIONS="--openssl-legacy-provider"
RUN apt-get install -y make gcc g++
# RUN npm config set registry http://registry.npmjs.org/
# Prefer ipv4 by default
RUN sed -i -e 's/.*precedence ::ffff:0:0\/96  100/precedence ::ffff:0:0\/96  100/g' /etc/gai.conf
RUN npm install -g truffle
RUN npm install -g ganache-cli

# Create workdir
RUN mkdir /src/
WORKDIR /src/
RUN cd /src/

# Add files
RUN apt-get install -y git
RUN git clone https://github.com/OpenZeppelin/openzeppelin-contracts.git

# Install tools
RUN apt-get install -y screen
