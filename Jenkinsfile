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
      steps { sh 'docker build -t $IMAGE_NAME .' }
    }
    stage('Unit Tests') {
      steps { sh 'docker run --rm $IMAGE_NAME pytest -q tests/test_unit_*' }
    }
    stage('Integration Tests') {
      steps { sh 'docker run --rm -p 5000:5000 $IMAGE_NAME pytest -q tests/test_integration_*' }
    }
    stage('Push Image (optional)') {
      when { expression { return env.PUSH_IMAGE == "true" } }
      steps {
        sh 'docker tag $IMAGE_NAME $REGISTRY/demoapp:latest'
        sh 'docker push $REGISTRY/demoapp:latest || true'
      }
    }
  }
}
