pipeline {
  agent any

  environment {
    IMAGE_NAME = "demoapp:latest"
    FILE_NAME= "Jenkinsfile"
    DRIVER_NAME = "ours"
    PUSH_IMAGE = "false"   // set to "true" to push to local registry
    COMMIT_MASSAGE = "#1"
  }

  stages {
    stage('checkot') { steps { checkout scm } }
    stage('cloning repo') {
      steps { 
              sh 'cd /var/jenkins_home/workspace'
              sh 'git clone https://github.com/doron266/jenkins-ci-ex.git && cd jenkins-ci-ex'
            }
    }
    stage('Build Image') {
      steps { sh 'docker build -t $IMAGE_NAME myjenkinsproject/demo-repo/' }
    }
    stage('Unit Tests') {
      steps { sh 'docker run --rm $IMAGE_NAME pytest -q ./test_unit_math.py' }
    }
    stage('Integration Tests') {
      steps { sh 'docker run --rm -p 5002:5002 $IMAGE_NAME pytest -q ./test_integration_api.py' }
    }
   
      }
    }
}

