pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')  // set this in Jenkins
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/sakeemanee/flask_CD.git'
      }
    }

    stage('Build Images') {
      steps {
        sh 'docker build -t your-dockerhub-user/user-service ./user-service'
        sh 'docker build -t your-dockerhub-user/order-service ./order-service'
      }
    }

    stage('Push Images') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        sh 'docker push your-dockerhub-user/user-service'
        sh 'docker push your-dockerhub-user/order-service'
      }
    }
  }
}
i
