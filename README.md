# question-answer-system

## Setup

### Spin up localstack
`mkdir /tmp/localstack`

`docker-compuse up`

### Install Serverless Framework
`curl -o- -L https://slss.io/install | bash`
or `npm install serverless -g`

TODO: add package.json file instead

`npm install serverless-localstack -g`

### Initialize Serverless Project
`serverless`