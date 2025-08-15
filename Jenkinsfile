pipeline {
  agent any

  environment {
    IMAGE_NAME = "demoapp:ci"
    REGISTRY = "localhost:5000"
    PUSH_IMAGE = "false"   // set to "true" to push to local registry
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Image') {
      steps { sh 'docker build -t $IMAGE_NAME myjenkinsproject/demo-repo/' }
    }
    stage('Unit Tests') {
      steps { sh 'docker run --rm $IMAGE_NAME pytest -q myjenkinsproject/demo-repo/tests/test_unit_math.py' }
    }
    stage('Integration Tests') {
      steps { sh 'docker run --rm -p 5001:5001 $IMAGE_NAME pytest -q myjenkinsproject/demo-repotests/test_integration_api.py' }
    }
    stage('pushing image') {
      steps { echo 'from dev branch- image pushed' }
      }
    }
}

