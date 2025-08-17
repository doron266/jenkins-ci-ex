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
    
    stage('Build Image') {
      steps { sh 'docker build -t $IMAGE_NAME myjenkinsproject/demo-repo/' }
    }
    stage('Unit Tests') {
      steps { sh 'docker run --rm $IMAGE_NAME pytest -q ./test_unit_math.py' }
    }
    stage('Integration Tests') {
      steps { sh 'docker run --rm -p 5002:5002 $IMAGE_NAME pytest -q ./test_integration_api.py' }
    }
    stage('cloning repo and updating main') {
      steps {
               sh 'git tag -a tagName -m "Your tag comment"'
               sh 'git merge dev'
               sh 'git commit -am "Merged develop branch to master'
               sh "git push origin main"
               echo 'hello from dev'
            }
   
    }
  }
}



